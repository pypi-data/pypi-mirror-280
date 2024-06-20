'''
This file contains utility functions.
'''
import bs4

DEFAULT_TIMEOUT = 60
CHSI_URL = 'https://www.chsi.com.cn'
VERIFY_URL_BASE = f'{CHSI_URL}/xlcx/bg.do'


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


def has_captha(doc: bs4.BeautifulSoup) -> bool:
    '''
    Check if the response has a captha.
    '''
    captch_tag = doc.select_one('input.captchTag')
    return captch_tag is not None


def verify_doc(doc: bs4.BeautifulSoup) -> dict:
    '''
    Verify the DOM of the response from chsi.com.cn.
    '''
    info = []
    result_error = parse_error(doc)
    if result_error is not None:
        return {
            'status': False,
            'captha': False,
            'error': result_error,
            'info': info
        }
    if has_captha(doc):
        return {
            'status': False,
            'captha': True,
            'error': 'captha',
            'info': []
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
        'captha': False,
        'error': '',
        'info': info
    }


def get_page_from_browser(browser):
    browser_context = browser.contexts[0]
    if not browser_context.pages:
        page = browser_context.new_page()
    else:
        page = browser_context.pages[0]
    return browser_context, page
