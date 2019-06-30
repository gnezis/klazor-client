import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="klazor-client",
    version="0.0.1",
    author="Wilfried L. Bounsi",
    author_email="wilcoln99@gmail.com",
    description="A package that enables to manipulate resources placed on the klazor server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wilcoln/klazor-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)