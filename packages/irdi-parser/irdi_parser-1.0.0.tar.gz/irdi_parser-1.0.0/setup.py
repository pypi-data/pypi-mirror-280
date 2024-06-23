from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='irdi-parser',
    version='1.0.0',
    description='A parser for International Registration Data Identifier (IRDI) strings.',
    author="Moritz Sommer",
    author_email="moritz.sommer@rwth-aachen.de",
    url='https://github.com/moritzsommer/irdi-parser',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)