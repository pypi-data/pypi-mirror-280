'''
Python lib for verifying chsi data.
'''
import sys
import json
import bs4
import requests

DEFAULT_TIMEOUT = 60
VERIFY_URL_BASE = 'https://www.chsi.com.cn/xlcx/bg.do'


def parse_error(doc: bs4.BeautifulSoup) -> str:
    '''
    Parse the error message from the response.
    '''
    error_node = doc.select_one('.result-error h2')
    if error_node:
        return error_node.text.strip()
    error_node = doc.select_one('.mainCnt span#msgDiv')
    if error_node:
        return error_node.text.strip()
    return None


def verify(vcode: str, lang: str='zh') -> dict:
    '''
    Verify the code from chsi.com.cn.
    '''
    url = f'{VERIFY_URL_BASE}?vcode={vcode}&lang={lang}'
    resp = requests.get(url, timeout=DEFAULT_TIMEOUT)
    doc = bs4.BeautifulSoup(resp.text, 'html.parser')
    info = []
    result_error = parse_error(doc)
    if result_error is not None:
        return {
            'status': False,
            'error': result_error,
            'info': info
        }
    title_node = doc.select_one('#resultTable h4')
    if title_node:
        info.append(['title', title_node.text.strip()])
    update_time_node = doc.select_one('#resultTable .update-time')
    if update_time_node:
        info.append(['update_time', update_time_node.text.strip().split('：')[1]])
    for item in doc.select('div.report-info-item'):
        label = item.select_one('div.label').text.strip()
        value = item.select_one('div.value').text.strip()
        info.append([label, value])
    return {
        'status': True,
        'error': '',
        'info': info
    }


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m chsi vcode")
        sys.exit(1)
    print(json.dumps(verify(sys.argv[1]), ensure_ascii=False, indent=2))
