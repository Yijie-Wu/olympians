# -*- encoding:utf-8 -*-
"""
Author: Yijie.Wu
Email: 1694517106@qq.com
"""

from setuptools import find_packages
from setuptools import setup

setup(
    name="aegis",
    version="0.2",
    description="An automation test framework",
    long_description=open("readme.md.md", 'r').read(),
    long_description_content_type="text/markdown",
    author='Yijie.Wu',
    author_email="1694517106@qq.com",
    url="https://github.com/Yijie-Wu/olympians",
    project_urls={
        "Github": "https://github.com/Yijie-Wu/olympians",
    },
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={"aegis": "aegis"},
    include_package_data=True,
    license="WTFPL",
    zip_safe=False,
    keywords="Automation Test Framework",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Testing :: Unit",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
        "License :: OSI Approved :: MIT",
        "Natural Language :: Chinese (Simplified)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    ]
)