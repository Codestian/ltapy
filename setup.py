import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ltapy", 
    version="1.0.0",
    author="Codestian",
    author_email="codestia@gmail.com",
    description="Asynchronous python library to access LTA's Datamall, primarily designed for Home Asssitant.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(include=['ltapy']),
    install_requires=['aiohttp'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)