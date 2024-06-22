# setup.py

from setuptools import setup, find_packages

setup(
    name="jzon",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    license="MIT",
    description="A simple library to convert dictionaries to JSON files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Tarek Ziad",
    author_email="heroesofdawn.18@gmail.com",
    url="https://github.com/Jjioo/jzon",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
