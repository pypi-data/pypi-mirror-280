from setuptools import setup

from setuptools import find_packages, setup

setup(
    name="hyaa",
    version="0.6",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "hyaa = hyaa.main:main",
        ],
    },
    author="Kapil Bhandari",
    author_email="iam.bkpl031@gmail.com",
    description="Hyaa ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iam-bkpl/rasifal",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)