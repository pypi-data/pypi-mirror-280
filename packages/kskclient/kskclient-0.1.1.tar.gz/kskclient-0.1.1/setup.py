from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="kskclient",
    version="0.1.1",
    author="Kiran",
    author_email="kirankulkarni682@gmail.com",
    description="A client library for interacting with the Qrizz API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rmialgorizz/qrizz-dsc/tree/python-sdk-dev/qrizzclient",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)