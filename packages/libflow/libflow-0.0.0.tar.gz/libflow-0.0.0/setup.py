from setuptools import setup, find_packages

setup(
    name="libflow",
    version="0.0.0",
    description="Libflow library",
    author_email="yiwanfu2017@gmail.com",
    license="Apache License, Version 2.0",
    packages=find_packages(exclude=("tests",)),
    python_requires='>=3.10',
    include_package_data=True,
    install_requires = open('requirements.txt').readlines(),
)
