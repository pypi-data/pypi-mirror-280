from setuptools import setup

setup(
    name="hyaa",
    version="0.4",
    py_modules=["hyaa"],
    install_requires=[
        "Click",
        "requests",
    ],
    entry_points="""
        [console_scripts]
        hyaa=hyaa.main:main
    """,
)
