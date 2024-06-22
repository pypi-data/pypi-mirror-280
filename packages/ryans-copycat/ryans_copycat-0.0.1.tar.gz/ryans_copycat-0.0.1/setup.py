from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = "0.0.1"

# Setting up
setup(
    name="ryans-copycat",
    version=VERSION,
    author="Ryan Li",
    author_email="<mail@go.com>",
    description="Ryan's Copy Cat",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=["copy", "cat"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.9",
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
)
