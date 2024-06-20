import random
import time
from .page_spider import BasePageCrawler


class DeepPage:
    def __init__(self, url: str, data: [dict, list], locs: dict = None, callback=None):
        self.url = url
        self.data = data
        self.locs = locs if locs else {}
        self.callback = callback


class DeepPageCrawler(BasePageCrawler):
    open_page_interval: int = 3
    # 深度url的提取规则
    deep_link_url: str = ''
    # 深度页面数据提取规则
    deep_data_extract_loc: dict = {}

    def auto_next_page(self):
        """自动翻页处理"""
        for i in range(self.pages):
            self.page.wait_for_load_state(state='networkidle')
            self.next_page_open()
            self.rollover_to_bottom()
            list(map(self.deep_page_open, self.parser_data()))
            time.sleep(self.TIME_INTERVAL)
            if self.next_page_btn_loc:
                self.page.click(self.next_page_btn_loc)

    def parser_data(self):
        """解析页面数据"""
        lists = self.page.locator(self.data_list_loc)
        for li in lists.all():
            items = dict()
            if self.data_extract_loc:
                for key, loc in self.data_extract_loc.items():
                    value = self.extract_data(li, loc)
                    items.__setitem__(key, value)
            link_url = li.locator(self.deep_link_url).evaluate('(e) => e.href')
            yield DeepPage(link_url, items)

    def deep_page_open(self, item: [DeepPage, list, dict]):
        """深度页面处理"""
        if isinstance(item, DeepPage):
            time.sleep(self.open_page_interval)
            page = self.context.new_page()
            page.goto(item.url)
            page.wait_for_load_state(state='networkidle')
            page.evaluate(f'window.scrollBy(0,{random.randint(200, 500)})')
            if item.callback:
                result = item.callback(page, item.data, item.locs)
            else:
                result = self.deep_page_callback(page, item.data, item.locs)
            page.close()
            self.deep_page_open(result)
        else:
            self.save_data(item)

    def deep_page_callback(self, page, data: [dict, list], locs=None):
        """deep page parser"""
        locs = locs if locs else self.deep_data_extract_loc
        for key, loc in locs.items():
            value = self.extract_data(page, loc)
            if isinstance(data, list):
                data.append(value)
            elif isinstance(data, dict):
                data.__setitem__(key, value)
        return data
