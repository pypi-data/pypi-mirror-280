from setuptools import setup, find_packages

setup(
    name="hapag_lloyd_sdk",
    version="0.2.1",
    description="Community SDK for Hapag-Lloyd API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Aaron Frank",
    author_email="aaron.frank@gedankenfabrik.de",
    url="https://github.com/gedankenfabrik/hapag_lloyd_sdk",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pydantic",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
