import re
import time
from abc import ABC, abstractmethod
import os
from faker import Faker
import requests
from moviepy.video.io import ffmpeg_tools
from playwright.sync_api import Response
from spider.page_spider import BasePageCrawler

fk = Faker()


class ImagesSpider(BasePageCrawler, ABC):
    """图片爬虫"""
    image_start_path: str = ""
    image_save_path: str = ''

    def create_save_dir(self):
        if self.image_save_path and not os.path.exists(self.image_save_path):
            os.makedirs(self.image_save_path)

    def spider(self):
        self.create_save_dir()
        self.page.goto(self.start_url)
        self.page.wait_for_load_state(state='load', timeout=10000)
        self.opened()
        self.page.wait_for_timeout(10000)

    def response_handler(self, response: Response):
        """监听响应对象"""
        types = response.headers.get('content-type')
        url = response.url
        if self.image_save_path and types in ['image/jpeg', 'image/png', 'image/jpg', 'image/avif', 'image/webp']:
            if self.filter_images(url):
                body = response.body()
                self.save_images(url, body)

    def save_images(self, url, content):
        url_path, name = os.path.split(url.split('?')[0])
        print('资源地址:', url)
        print("文件名称:", name)
        filepath = os.path.join(self.image_save_path, name)
        if not os.path.exists(filepath):
            with open(filepath, 'wb') as f:
                f.write(content)
                print(f'文件 {name} 保存成功')
        else:
            print(f'文件 {name} 已存在')

    def filter_images(self, url):
        """过滤图片"""
        if url.startswith(self.image_start_path):
            return True


class VideoSpider(BasePageCrawler):
    """视频爬虫"""
    __historical_url: list = []
    __merge_media_names = set()
    # 视频保存路径
    video_save_path: str = ''
    # 视频地址前缀
    video_start_path: str = ''
    # 下载的视频类型
    file_types: list = []
    # 从url中提取文件名的规则
    file_name_pattern: str = '*************&&&&&&&&&&&&'
    audio_tag: str = '8888888888887*********%%%%%%%%%'
    video_tag: str = '8888888888887*********%%%%%%%%%'

    def create_save_dir(self):
        if self.video_save_path and not os.path.exists(self.video_save_path):
            os.makedirs(self.video_save_path)

    def spider(self):
        self.create_save_dir()
        self.page.goto(self.start_url, timeout=30000)
        self.page.wait_for_timeout(3000)
        self.opened()
        self.page.wait_for_timeout(10000)

    def response_handler(self, response: Response):
        """处理响应对象"""
        url = response.url
        types = response.headers.get('content-type')
        if url in self.__historical_url:
            return
        self.__historical_url.append(url)
        if types not in self.file_types:
            return
        if self.filter(response):
            filename = self.get_filename(url, types)
            file_path = os.path.join(self.video_save_path, filename)
            if not os.path.exists(file_path):
                print('视频地址:', url)
                self.download_video(url, file_path, response.request)
                if self.__merge_media_names:
                    # 合并文件
                    self.merge_medias(self.__merge_media_names.pop())
            else:
                print(f"视频已经存在，:{file_path}")
        else:
            print("不符合过虑规则，未进行下载地址：", url)

    def merge_medias(self, name):
        """合并文件"""
        f1 = os.path.join(self.video_save_path, f'{name}.audio')
        f2 = os.path.join(self.video_save_path, f'{name}.video')
        if os.path.isfile(f1) and os.path.isfile(f2):
            f3 = os.path.join(self.video_save_path, f'{name}.mp4')
            ffmpeg_tools.ffmpeg_merge_video_audio(f1, f2, f3)
            os.remove(f1)
            os.remove(f2)
            print(f"将{name}.audio和{name}.video合并为视频文件{name}.mp4")

    def filter(self, response):
        return True

    def get_filename(self, url, types):
        """生成文件名：文件名需要时唯一的"""
        name = re.search(self.file_name_pattern, url)
        name = name.group(1) if name else str(int(time.time() * 1000))
        # 区分 音频文件还是视频文件
        if self.audio_tag in url:
            self.__merge_media_names.add(name)
            return f'{name}.audio'
        if self.video_tag in url:
            self.__merge_media_names.add(name)
            return f'{name}.video'
        img_type = types.split('/')[1]
        filename = f'{name}.{img_type}'
        return filename

    @staticmethod
    def download_video(url, filepath, request_info):
        """下载视频"""
        try:
            # 将视频文件下载到本地
            response = requests.get(url, stream=True, headers={'User-Agent': fk.user_agent()})
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
        except Exception as e:
            print("文件下载失败..................")
            print(e)
        else:
            print(f"视频下载成功,保存路径为:{filepath}")
