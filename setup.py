from setuptools import find_packages, setup

setup(
    name="vocab",
    version="0.0.1",
    author="NewDawn0",
    author_email="newdawn.v0.0+git@gmail.com",
    description="A vocab learning tool",
    packages=find_packages(),
    install_requires=[],
    entry_points={"console_scripts": ["vocab = vocab.main:main"]},
)
