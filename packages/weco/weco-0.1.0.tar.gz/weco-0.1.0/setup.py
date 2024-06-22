from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md")) as f:
    long_description = f.read()

user_requirements = [
    requirement.strip()
    for requirement in open(path.join(here, "requirements.txt")).readlines()
]

setup(
    name="weco",
    version="0.1.0",
    author=["WeCo AI Team"],
    author_email="dhruv@weco.ai",
    description="A client facing API for interacting with the WeCo AI function builder service.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/WecoAI/weco",
    keywords=[
        "artificial intelligence",
        "machine learning",
        "data science",
        "function builder",
        "LLM",
    ],
    packages=find_packages(where="weco"),
    package_dir={"": "weco"},
    install_requires=user_requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
