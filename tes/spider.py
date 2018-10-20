from tes.wsgi import *
from scp.models import Information
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import re


def spider():
    def get_one_page(one_url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }
        response = requests.get(one_url, headers=headers)
        if response.status_code == 200:
            return response.text
        print("存在请求失败的网页")
        return None

    def get_other_pages(one_url):
        post_data = {
            'newskindid': "201710211304556344YxBz6GmyJ8x4",
            'pageNumber': 2
        }
        response = requests.post(one_url, data=post_data)
        if response.status_code == 200:
            return response.text
        print("存在请求失败的网页")
        return None

    def get_link(one_html):
        soup = BeautifulSoup(one_html, "lxml")
        a = soup.select(".content_list a")
        url_list = set()
        for url in a:
            full_url = urljoin("http://eis.whu.edu.cn/newsDetails_zw.shtml?newskindid=\
            201710211304556344YxBz6GmyJ8x4&newsinfoid=20171219082131302wXQX6f4kwhghF", url["href"])
            url_list.add(full_url)
        return url_list

    def parse_one_page(one_html):
        clear_html = BeautifulSoup(one_html, "lxml").text

        # 正则表达式匹配并整理time
        pattern = re.compile("报告时间：(.*?)报告", re.S)
        time = re.search(pattern, clear_html)
        if time is not None:
            clear_time_4 = time.group(1).replace("\n", "").replace("\xa0", "").replace("\r", "")
        else:
            clear_time_4 = "暂无"

        # BeautifulSoup提取title
        soup = BeautifulSoup(one_html, "lxml")
        title = soup.select(".content_tex h3")[0].text

        # 正则表达式匹配并整理place
        pattern = re.compile("报告地点：(.*?)报告", re.S)
        place = re.search(pattern, clear_html)
        if place is not None:
            clear_place_4 = place.group(1).replace("\n", "").replace("\xa0", "").replace("\r", "")
        else:
            clear_place_4 = "暂无"

        # 正则表达式匹配并整理speaker
        pattern = re.compile("报\s*告\s*人：(.*?)报告", re.S)
        speaker = re.search(pattern, clear_html)
        if speaker is not None:
            clear_speaker_5 = speaker.group(1).replace("\n", "").replace("\xa0", "")
        else:
            clear_speaker_5 = "暂无"

        # 得到dict
        data_dict = {
            "title": title,
            "time": clear_time_4,
            "place": clear_place_4,
            "speaker": clear_speaker_5
        }
        return data_dict

    # 把入口页面 html 放进集合 pages
    root_page = "http://eis.whu.edu.cn/newListLogic.shtml?newskindid=201710211304556344YxBz6GmyJ8x4"
    pages = set()
    pages.add(get_one_page(root_page))

    # 把所有讲座列表页面 html 放进集合 pages
    some_htmls = get_other_pages(root_page)
    pages.add(some_htmls)

    # 获取 pages 中讲座链接列表
    lecture_links = set()
    for page in pages:
        if page is not None:
            links = get_link(page)
            lecture_links.update(links)

    # 获取讲座内容
    data_list = list()
    for lecture_link in lecture_links:
        if lecture_link is not None:
            lecture_html = get_one_page(lecture_link)
            data = parse_one_page(lecture_html)
            data_list.append(data)
    return data_list


data_l = spider()
for i in data_l:
    Information.objects.get_or_create(title=i['title'], speaker=i['speaker'], time=i['time'], place=i['place'])
print('Done!')
