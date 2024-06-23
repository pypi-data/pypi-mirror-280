from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.2-beta'
DESCRIPTION = 'Easy chatbot development with Python. Create your own chatbots with just a few lines of code.'
# Setting up
setup(
    name="botcreator",
    version=VERSION,
    author="EdexCode",
    author_email="edexcode@gmail.com",
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    project_urls={
        "GitHub": "https://github.com/EdexCode/BotCreator"
    },
    license='MIT License',
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'bot', 'chatbot', 'botdeveloper', 'predefined'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)