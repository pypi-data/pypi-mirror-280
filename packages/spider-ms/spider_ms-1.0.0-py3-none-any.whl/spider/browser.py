import platform
import random
import re, os
import time
from abc import ABC, abstractmethod
from playwright.sync_api import sync_playwright, Page, BrowserContext


class BaseBrowser(ABC):
    DEBUG = False
    BROWSER: str = 'chrome'
    IS_LOCAL_BROWSER: bool = False
    BROWSER_PATH: str = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    USER_DIR: str = r'C:\Users\zengyanzhi\AppData\Local\Google\Chrome\User Data'
    PORT = 19789
    IS_LOAD_IMAGE = True
    IS_HEADLESS: bool = True
    TIME_INTERVAL: int = random.randint(1, 3)

    @abstractmethod
    def spider(self):
        """抽象方法"""

    @staticmethod
    def kill_chrome():
        if platform.system() == 'Windows':
            os.popen('taskkill /F /IM chrome.exe')
        else:
            os.popen('killall chrome')
        time.sleep(1)

    @property
    def startup_parameters(self):
        return dict(
            user_data_dir=self.USER_DIR,
            executable_path=self.BROWSER_PATH,
            args=['--disable-blink-features=AutomationControlled'],
            headless=self.IS_HEADLESS
        )

    def get_browser_type(self, playwright):
        if self.BROWSER == 'firefox':
            return playwright.firefox
        elif self.BROWSER == 'Safari':
            return playwright.webkit
        else:
            return playwright.chromium

    def open_local_browser(self):
        chrome_path = r'"C:\Program Files\Google\Chrome\Application\chrome.exe"'
        debugging_port = f"--remote-debugging-port={self.PORT}"
        command = f"{chrome_path} {debugging_port}"
        os.popen(command)
        time.sleep(2)

    def __open_browser(self, playwright):
        browser_type = self.get_browser_type(playwright)
        if self.DEBUG:
            self.open_local_browser()
            self.browser = playwright.chromium.connect_over_cdp(f"http://127.0.0.1:{self.PORT}")
            self.context: BrowserContext = self.browser.contexts[0]
            self.page: Page = self.context.pages[0]
        elif self.IS_LOCAL_BROWSER:
            try:
                self.browser = browser_type.launch_persistent_context(**self.startup_parameters)
            except Exception:
                self.kill_chrome()
                self.__open_browser(playwright)
            self.context: BrowserContext = self.browser.pages[0].context
            self.page: Page = self.browser.pages[0]
        else:
            self.browser = browser_type.launch(headless=self.IS_HEADLESS)
            self.context: BrowserContext = self.browser.new_context()
            self.page: Page = self.context.new_page()
        if not self.IS_LOAD_IMAGE:
            self.page.route(re.compile(r"(\.png)|(\.jpg)|(\.jpeg)"), lambda x, y: x.abort())
        self.api_request = self.context.request
        self.page.on("response", self.response_handler)
        self.page.on("request", self.requests_handler)
        print("已经为你准备好执行环境，开始加载页面")

    def main(self):
        try:
            with sync_playwright() as playwright:
                self.__open_browser(playwright)
                js = "Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});"
                self.page.add_init_script(js)
                self.spider()
                self.browser.close()
            print("数据已经抓取完毕..........")
        except KeyboardInterrupt:
            print("程序被手动终止..........")

    def response_handler(self, request):
        pass

    def requests_handler(self, request):
        pass
