from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="DIRAC",
    version="0.1.0",
    description="""Domain Invariant Representation through Adversarial Calibration (DIRAC), a graph neural network to integrate spatial multi-omic data into a unified domain 
    invariant embedding space and to automate cell-type annotation by transferring labels from reference multi-omic single-cell or spatial data. """,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="XU CHANG",
    packages=find_packages(include=["DIRAC"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=required,
    license="MIT",
    url="https://github.com/EsdenRun/DIRAC",
    python_requires=">=3.9",
)