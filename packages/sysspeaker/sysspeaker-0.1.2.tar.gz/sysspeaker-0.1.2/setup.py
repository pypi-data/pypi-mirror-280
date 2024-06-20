from setuptools import setup, find_packages

setup(
    name="sysspeaker",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[],  
    author="rudra_826",
    author_email="rudrapanda8206@gmail.com",
    description="A simple python package to get the system speak output.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/pandarudra/sysspeaker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)