import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="eip712-clearsign",
    version="2.1.0rc2",
    url="https://github.com/LedgerHQ/python-eip712",
    author="Ledger",
    author_email="hello@ledger.com",
    description="Parse eip712 clear sign descriptors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["pydantic"],
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
