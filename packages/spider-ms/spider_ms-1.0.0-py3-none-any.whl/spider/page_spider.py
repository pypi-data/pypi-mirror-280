import random
from spider.browser import BaseBrowser


class BasePageCrawler(BaseBrowser):
    start_url: str = ''
    data_list_loc: str = ''
    next_page_btn_loc: str = ""
    next_button_distance: int = 200
    split_str: str = '\n'
    pages: int = 1
    data_extract_loc: dict = {}

    def is_clickable(self, selector):
        try:
            element = self.page.locator(selector)
            is_disabled = element.evaluate("element => element.disabled")
            if any([element.is_enabled(), element.is_visible(), is_disabled]):
                return True
        except Exception as e:
            print(f"An error occurred while checking the element: {e}")
            return False

    @staticmethod
    def extract_data(page, loc):
        """解析数据"""
        try:
            if loc[0] == 'text':
                value = page.locator(loc[1]).inner_text()
            else:
                value = page.locator(loc[1]).get_attribute(loc[0])
            return value
        except Exception as e:
            print("表达式：{},数据提取失败:{}".format(loc, e))
            return ''

    def rollover_to_bottom(self):
        """慢慢的滚动到页面底部"""
        s = 0
        while True:
            height = random.randint(200, 800)
            s += height
            js = f'window.scrollBy(0,{height})'
            self.page.evaluate(js)
            page_height = self.page.evaluate('() => document.body.scrollHeight')
            self.page.wait_for_timeout(random.randint(1, 3))
            if page_height - s < self.next_button_distance:
                break

    def rollover_load(self):
        """滚动加载内容"""

    def check(self):
        if not self.start_url:
            print("提示抓取的入口start_url没有配置")
            exit()
        if not self.data_list_loc:
            print("提示数据列表的定位器没有配置")
            exit()

    def spider(self):
        """爬虫入口"""
        self.check()
        self.page.goto(self.start_url)
        self.page.wait_for_load_state(state='networkidle')
        self.opened()
        self.auto_next_page()

    def auto_next_page(self):
        for i in range(self.pages):
            self.page.wait_for_load_state(state='networkidle')
            self.next_page_open()
            self.rollover_to_bottom()
            list(map(self.save_data, self.parser_data()))
            self.page.wait_for_timeout(self.TIME_INTERVAL)
            if self.next_page_btn_loc:
                self.page.click(self.next_page_btn_loc)

    def parser_data(self):
        """parser page data"""
        lists = self.page.locator(self.data_list_loc)
        for li in lists.all():
            if len(self.data_extract_loc):
                items = dict()
                for key, loc in self.data_extract_loc.items():
                    value = self.extract_data(li, loc)
                    items.__setitem__(key, value)
            else:
                items = li.inner_text().split(self.split_str)
                items = [item for item in items if item]
            yield items

    def next_page_open(self):
        """next page open"""

    def save_data(self, data: [dict, list, str]):
        """sava data"""
        print(data)

    def opened(self):
        """page opened"""
        print("------page open---------")

    def end(self):
        """spider end"""
        self.page.close()
