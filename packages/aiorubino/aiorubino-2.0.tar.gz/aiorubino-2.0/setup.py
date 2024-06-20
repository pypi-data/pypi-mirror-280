from setuptools import setup, find_packages

setup(
    name="aiorubino",
    version="2.0",
    author="AmirAli Irvany",
    author_email="irvanyamirali@gmail.com",
    description="aiorubino is an api-based library for Rubino messengers",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/irvanyamirali",
    install_requires=["aiohttp"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
