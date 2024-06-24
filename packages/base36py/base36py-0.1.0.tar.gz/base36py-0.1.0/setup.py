from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="base36py",
    version="0.1.0",
    author="Danishjeet Singh",
    author_email="danishjeetsingh@gmail.com",
    description="A lightweight Python library for encoding and decoding numbers between base10 and base36.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DanishjeetSingh/base36py",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)