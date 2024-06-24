from setuptools import find_packages, setup

setup(
    name="pygister",
    version="0.1.0",
    description="A Python tool to interact with GitHub Gists",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Farshid Ashouri",
    author_email="farsheed.ashouri@gmail.com",
    url="https://github.com/ourway/pygister",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "requests",
    ],
    extras_require={
        "dev": [
            "pytest",
            "isort",
            "black",
            "mypy",
            "python-dotenv",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
