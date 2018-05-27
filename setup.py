import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="felux",
    version="0.0.1",
    author="Myles Eftos",
    author_email="myles@madpilot.com.au",
    description="Python library for talking to FeLUX lights",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/madpilot/pyfelux",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
