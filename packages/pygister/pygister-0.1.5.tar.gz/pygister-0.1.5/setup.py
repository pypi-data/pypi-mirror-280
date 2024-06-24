from setuptools import find_packages, setup

# read from VERSION file

with open("VERSION", "r") as version_file:
    version = version_file.read().strip()


setup(
    name="pygister",
    version=version,
    description="A Python tool to interact with GitHub Gists",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Farshid Ashouri",
    author_email="farsheed.ashouri@gmail.com",
    url="https://github.com/ourway/pygister",
    packages=find_packages(where="src/"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "requests",
        "click",
        "python-dotenv",
    ],
    extras_require={
        "dev": [
            "pytest",
            "isort",
            "black",
            "mypy",
        ],
    },
    entry_points={
        "console_scripts": [
            "pygist=pygister:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
