import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dobby_storage",
    version="0.0.3",
    author="Ting-Yu, Wang",
    author_email="g66341x@gmail.com",
    description="A storage handling package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
    install_requires=[
        'boto3',
        'pydrive',
    ],
)