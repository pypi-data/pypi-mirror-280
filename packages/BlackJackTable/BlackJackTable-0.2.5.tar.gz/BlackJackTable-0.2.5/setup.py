from setuptools import setup, find_packages

with open ("README.md", "r") as f:
    description = f.read()

setup(
    name = "BlackJackTable",
    version="0.2.5",
    packages=find_packages(),
    install_requires=[
    ],
    author="zedMar65",
    long_description=description,
    long_description_content_type="text/markdown",
)
