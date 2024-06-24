import setuptools  # 导入setuptools打包工具

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="loongfei_utils",  # 用自己的名替换其中的YOUR_USERNAME_
    version="1.0.8",  # 包版本号，便于维护版本,保证每次发布都是版本都是唯一的
    author="龙飞",  # 作者，可以写自己的姓名
    author_email="fcfwork@163.com",  # 作者联系方式，可写自己的邮箱地址
    description="python工具包",  # 包的简述
    long_description=long_description,  # 包的详细介绍，一般在README.md文件内
    long_description_content_type="text/markdown",
    url="https://gitee.com/fcf_python/python-utils",  # 自己项目地址，比如github的项目地址
    packages=["loongfei_utils","loongfei_utils/utils"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 对python的最低版本要求
)