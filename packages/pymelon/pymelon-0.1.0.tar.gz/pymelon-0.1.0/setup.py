from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pymelon",
    version="0.1.0",
    description="A data manipulation library for JSON and lists of dictionaries.",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaz-alli/pyberry",
    author="Jaz Allibhai",
    author_email="jaz.allibhai@gmail.com",
    license="MIT",
)
