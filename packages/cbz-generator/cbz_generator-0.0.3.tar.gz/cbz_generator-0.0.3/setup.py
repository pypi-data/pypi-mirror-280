from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'CBZ archiver'
LONG_DESCRIPTION = 'Utility for converting images into a CBZ archive individually or in bulk.'

# Setting up
setup(
    name="cbz_generator",
    version="0.0.3",
    author="Tyler Crosby",
    author_email="contact@tycro.io",
    description="CBZ archiver",
    long_description="Utility for converting images into a CBZ archive individually or in bulk.",
    packages=find_packages(),
    install_requires=[],  # add any additional packages that

    keywords=['python', 'CBZ'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)