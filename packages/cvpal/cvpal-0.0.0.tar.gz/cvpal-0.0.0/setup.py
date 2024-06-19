from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.0'
DESCRIPTION = 'A Python library for every Computer Vision Engineer'
LONG_DESCRIPTION = """
# Introduction

Welcome to cvPal!👋

cvPal is a powerful Python package designed to assist Computer Vision engineers in performing a variety of image operations. The primary goal of cvPal is to simplify the process of image manipulation and dataset management, enabling engineers to focus on building and optimizing their machine learning pipelines.

With cvPal, you can easily handle tasks such as merging datasets, removing specific labels, counting label occurrences, and generating comprehensive reports on your dataset, all with a user-friendly interface and comprehensive documentation.

## Features
- **Dataset Merging**: Functions to seamlessly merge different datasets, each with multiple attributes.
- **Label Removal**: Functions to remove specific labels from your dataset.
- **Label Occurrence Counting**: Functions to count the occurrences of specific labels.
- **Dataset Reporting**: Functions to generate comprehensive reports on your dataset.
- **Easy Integration**: Seamlessly integrate with existing ML pipelines.
- **Comprehensive Documentation**: Detailed documentation to guide you through all features and functionalities.
"""

# Setting up
setup(
    name="cvpal",
    version=VERSION,
    author="Mohamed E. Ibrahim",
    author_email="mohamedelsayed3487@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pandas',
        'pyaml',
        'PyYAML',
        'python-dateutil',
        'numpy'
    ],
    keywords=[
        'python',
        'computer vision',
        'cv',
        'Data Reformatting',
        'YOLO',
        'Roboflow',
        'ultralytics',
        'Data preprocessing'
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
