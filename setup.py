import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="ipy2d",
    version="0.0.1",
    description="Convert IP addresses to integers",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/0xflotus/ipy2d",
    author="0xflotus",
    author_email="0xflotus+pypi@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["ipy2d"],
    include_package_data=True,
    install_requires=[]
)
