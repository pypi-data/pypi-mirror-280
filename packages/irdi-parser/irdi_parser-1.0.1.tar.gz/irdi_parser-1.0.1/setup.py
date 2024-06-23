from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='irdi-parser',
    version='1.0.1',
    description='A parser for International Registration Data Identifier (IRDI) strings.',
    long_description='The IRDI Parser is a Python program designed to parse IRDI (International Registration Data '
                     'Identifier) strings based on the international standards ISO/IEC 11179-6, ISO 29002 and ISO/IEC '
                     '6523. It is used in the ECLASS standard. The program uses regular expressions to extract '
                     'various components of an IRDI string and returns them in a structured format.',
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