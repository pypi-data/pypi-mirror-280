from setuptools import find_packages, setup

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="plasgate",
    version="1.0.0",
    description="Helper library for working with tests",
    packages=find_packages(),
    install_requires=[
        # add dependencies here.
        # e.g. 'numpy>=1.11.1
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)

