import setuptools
import os

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="UrlNormalization",
    version="0.1.0",
    author="dwbruijn",
    description="Package for URL Nomalization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/witslb/url-normalization",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "idna~=3.6",
        "validators~=0.22.0"
    ]
)