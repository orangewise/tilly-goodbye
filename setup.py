from setuptools import setup

setup(
    name="tilly-goodbye",
    version="0.0.1",
    url="https://github.com/tilly-pub/tilly-goodbye",
    py_modules=["tilly_goodbye"],
    install_requires=[
        "tilly",
        "setuptools"
    ],
    entry_points={
        "tilly": ["goodbye = tilly_goodbye"],
    },
)