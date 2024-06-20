import codecs
from setuptools import setup, find_packages

MAJOR = 0
MINOR = 0
MICRO = 1
ISRELEASED = True
VERSION = f"{MAJOR}.{MINOR}.{MICRO}"

DESCRIPTION = "Python utils for AI"


long_description = codecs.open("README.md", encoding="utf-8").read() + "\n"


def read_file(filename):
    with open(filename, encoding="utf-8") as f:
        content = f.read()
    return content


def read_requirements(filename):
    return [
        line.strip()
        for line in read_file(filename).splitlines()
        if not line.startswith("#")
    ]


setup(
    name="rlmc",
    version=VERSION,
    keywords="python,AI,tool",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author="RayLam",
    author_email="1027196450@qq.com",
    url="https://github.com/RayLam2022/rlmc",
    # 要安装的文件夹，内要有__init__.py,而exclude可排除指定路径，例"rlmc.utils"
    packages=find_packages(exclude=["__pycache__.*", "*__pycache__", "tests.*", "tests","build.*","dist.*"]),
    # include_package_data=True,
    package_data={
        "rlmc.resource": ["*.json", "*.conf", "*.html", "*.yaml", "*.txt"],
        "rlmc": ["*"],
    },  # 一样要在文件夹内有__init__.py才会在该文件夹内查找
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "dev": ["pytest", "mypy"],
    },
    license="MIT",
    platforms="any",  # ["all","osx","windows", "linux"] 不能限制
    package_dir={"rlmc": "rlmc"},  # 左为find_packages, -> 右
    python_requires=">=3.8",
    classifiers=[
        # 发展时期
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        # "Programming Language :: Python :: 3.8",
    ],
    entry_points={"console_scripts": ["rl = rlTest.test:main"]}, #避免为test或与site-packages内文件夹同名
)
