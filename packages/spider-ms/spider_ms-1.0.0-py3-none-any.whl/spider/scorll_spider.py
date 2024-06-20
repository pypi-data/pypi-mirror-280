import time
from spider import BasePageCrawler


class ScrollLoaderSpider(BasePageCrawler):
    """滚动点击动态加载爬虫"""
    loaders: int = 10
    loader_more_loc: str = ''

    def __init__(self, url=None):
        super().__init__()
        if url:
            self.start_url = url

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.num = 0
        return instance

    def scroll_ele_view(self, i):
        print(f"第{i + 1}次加载更多数据")
        element = self.page.locator(self.loader_more_loc)
        element.scroll_into_view_if_needed()
        self.page.click(self.loader_more_loc)

    def spider(self):
        self.check()
        self.page.goto(self.start_url)
        self.page.wait_for_load_state(state='networkidle')
        self.opened()
        self.rollover_to_bottom()
        for i in range(self.loaders):
            self.page.wait_for_load_state(state='networkidle')
            list(map(self.save_data, self.parser_data()))
            time.sleep(self.TIME_INTERVAL)
            self.scroll_ele_view(i)

    def parser_data(self):
        lists = self.page.locator(self.data_list_loc)
        datas = lists.all()[self.num:]
        for li in datas:
            if len(self.data_extract_loc):
                items = dict()
                for key, loc in self.data_extract_loc.items():
                    value = self.extract_data(li, loc)
                    items.__setitem__(key, value)
            else:
                items = li.inner_text().split(self.split_str)
                items = [item for item in items if item]
            self.num += 1
            yield items
