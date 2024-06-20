'''
This module is used to solve the captcha of the page.
'''
import sys
import json
import typing
import time
import urllib
import bs4
from playwright.sync_api import sync_playwright
from . import utility


def parse_captha(page) -> bytes:
    '''
    Parse the captha in page.
    '''
    timestamp = int(time.time() * 1000)
    captha_url = f'{utility.CHSI_URL}/capachaimg.jpg?ID={timestamp}'
    resp = page.request.get(captha_url)
    return resp.body()


def verify(vcode: str, lang: str='zh', context: typing.Any=None, get_browser: typing.Any=None) -> dict:
    '''
    Verify the code from chsi.com.cn using chromium.
    '''
    with sync_playwright() as p:
        browser = get_browser(p) if get_browser else p.firefox.launch()
        browser_context, page = utility.get_page_from_browser(browser)
        if context and context.get('cookies'):
            browser_context.add_cookies(context['cookies'])
        url = f'{utility.VERIFY_URL_BASE}?vcode={vcode}&lang={lang}&srcid=bgcx'
        page.goto(url)
        page.wait_for_load_state()
        try:
            page.wait_for_load_state('networkidle', timeout=10000)
        except:
            print("timeout 10000ms")
        try:
            content = page.content()
        except Exception as e:
            print("Exception: ", e)
            content = page.content()
        doc = bs4.BeautifulSoup(content, 'html.parser')
        ret = utility.verify_doc(doc)
        if (not ret['status']) and ret['captha']:
            ret['context'] = {
                'vcode': vcode,
                'lang': lang,
                'url': page.url,
                'cookies': page.context.cookies(),
                'captha_img': parse_captha(page)
            }
        browser.close()
        return ret


def resume_from_captha(captha_code: str, context: typing.Any, get_browser: typing.Any=None) -> dict:
    '''
    Resume the request from the captha.
    '''
    with sync_playwright() as p:
        browser = get_browser(p) if get_browser else p.firefox.launch()
        browser_context, page = utility.get_page_from_browser(browser)
        captha_verify_url = f'{utility.CHSI_URL}/xlcx/yzm.do'
        captha_verify_resp = page.request.post(captha_verify_url,
                                               form={'cap': captha_code, 'Submit': '继续'})
        context['cookies'] = page.context.cookies()
        responsed_text = captha_verify_resp.text()
    if urllib.parse.urlparse(captha_verify_resp.url).path != '/xlcx/bg.do':
        return verify(context['vcode'], lang=context['lang'], context=context)
    else:
        doc = bs4.BeautifulSoup(responsed_text, 'html.parser')
        return utility.verify_doc(doc)


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m chsi.captha vcode")
        sys.exit(1)
    vcode = sys.argv[1]
    ret = None
    while True:
        ret = verify(vcode)
        if ret['status']:
            break
        elif ret['captha'] is True:
            with open('captha.jpg', 'wb') as f:
                f.write(ret['context']['captha_img'])
            captha_code = input('Please input the captha code（in captha.jpg）: ')
            ret = resume_from_captha(captha_code, ret['context'])
            if ret['status']:
                break
        else:
            break
    print(json.dumps(ret, ensure_ascii=False, indent=2))