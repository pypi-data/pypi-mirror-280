from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cool_pipe",
    version="0.1.0",
    author="Daniel Zholkovsky",
    author_email="daniel@zholkovsky.com",
    description="Simple pipelines for python functions and methods",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dailydaniel/cool_pipe",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
