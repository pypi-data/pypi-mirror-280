import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="auto-blur",
    version="0.0.1",
    author="Noah",
    author_email="inhwancho02@gmail.com",
    description="Auto blur lib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codernoah404/AutoBlur",
    project_urls={
        "Bug Tracker": "https://github.com/codernoah404/AutoBlur/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
