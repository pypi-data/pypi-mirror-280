from setuptools import setup, find_packages
import pathlib


def read_requirements():
    requirements_file = pathlib.Path(__file__).parent / "requirements.txt"
    with requirements_file.open() as req_file:
        return req_file.read().splitlines()


setup(
    name="breathmetrics",
    version="0.0.2",
    packages=find_packages(),
    install_requires=read_requirements(),
    author="Shashank",
    author_email="shashankchandrashekar2000@gmail.com",
    description="A breathing analysis tool",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
