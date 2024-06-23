from setuptools import setup

setup(
    name="hyaa",
    version="0.1",
    py_modules=["hyaa"],
    install_requires=[
        "Click",
        "requests",
    ],
    entry_points="""
        [console_scripts]
        hyaa=hyaa:random_quote
    """,
)
