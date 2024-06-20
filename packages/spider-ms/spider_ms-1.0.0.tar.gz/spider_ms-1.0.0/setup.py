from setuptools import setup, find_packages

with open("readme.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setup(
    name='spider_ms',
    version='1.0.0',
    author='MuSen',
    author_email='121292678@qq.com',
    url='https://github.com/musen123',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["moviepy==1.0.3", "pillow==10.3.0", "playwright== 1.44.0",
                      "faker==25.8.0", "requests==2.32.3"
                      ],
    packages=find_packages(),
    package_data={
        "": ["*.html", '*.md'],
    },
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
