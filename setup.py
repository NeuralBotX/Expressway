from setuptools import setup, find_packages

from pkg_resources import parse_requirements

with open("requirements.txt", encoding="utf-8") as fp:
    install_requires = [str(requirement) for requirement in parse_requirements(fp)]

setup(
    name="Expressway",
    version="1.0.0",
    author="Yunheng Wang",
    author_email="wangyunhenggxy@zjnu.edu.cn",
    description="🚀  Expressway network planning 🚦 project in Chongqing🛤️, Sichuan Province🐼",
    long_description="🚀  Expressway network planning 🚦 project in Chongqing🛤️, Sichuan Province🐼",
    license="MIT License",
    url="https://github.com/Yunheng-Wang/Expressway",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    packages=find_packages(),
    install_requires=install_requires,
)
