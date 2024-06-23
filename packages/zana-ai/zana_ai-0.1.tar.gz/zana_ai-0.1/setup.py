# setup.py

from setuptools import setup, find_packages

setup(
    name="zana-ai",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pyyaml",
        "colorama",
        "python-tgpt"
    ],
    entry_points={
        'console_scripts': [
            'phind=zana_ai.phind:main',
        ],
    },
    author="Zanabal",
    author_email="zanabal.nowshad@gmail.com",
    description="A package for PHIND chatbot functionality",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ZanaNowshad/zana-ai",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
