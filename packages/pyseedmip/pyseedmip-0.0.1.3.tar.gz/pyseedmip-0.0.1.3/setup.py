from setuptools import setup, Extension, find_packages

setup(
    name="pyseedmip",
    version="0.0.1.3",
    aduthor="seed",
    description="seedmip for python",
    packages=find_packages(),   # automatically find all python packages
    package_data={'pyseedmip': ['pyseedmip.cpython-39-x86_64-linux-gnu.so']},
)
