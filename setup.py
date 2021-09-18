import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cloud-runtimes-python",
    version="0.0.1",
    author="group.rxcloud",
    author_email="wshten@gmail.com",
    description="Cloud Runtimes API for Python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/reactivegroup/cloud-runtimes-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
