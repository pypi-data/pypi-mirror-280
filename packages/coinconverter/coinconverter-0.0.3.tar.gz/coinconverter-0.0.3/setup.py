from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.3'
DESCRIPTION = 'Real-time currency converter'
# Setting up
setup(
    name="coinconverter",
    version=VERSION,
    author="EdexCode",
    author_email="edexcode@gmail.com",
    license="MIT License",
    project_urls={
        "GitHub": "https://github.com/EdexCode/coinconverter"
    },
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['bs4', 'requests'],
    keywords=['python', 'currency', 'converter', 'realtime', 'convert'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)