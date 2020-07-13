# setup.py file

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata_iambrookedrake",
    version="0.1.1",
    author="Brooke Drake",
    author_email="iambrookedrake@gmail.com",
    description="Common DS Utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iambrookedrake/lambdata_iambrookedrake",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)