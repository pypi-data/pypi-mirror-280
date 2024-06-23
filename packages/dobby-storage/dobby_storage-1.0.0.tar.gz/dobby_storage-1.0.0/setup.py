from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dobby-storage",
    version="1.0.0",  # Update version here
    author="Ting-Yu Wang",
    author_email="g66341x@gmail.com",
    description="A package for handling various storage options.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ting-Yu/python-storage-package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'boto3',
        'pydrive2',
    ],
    include_package_data=True,
    tests_require=[
        'pytest',
    ],
    test_suite='tests',
)