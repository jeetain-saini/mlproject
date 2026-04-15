from setuptools import find_packages, setup

def get_requirements(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f if line.strip() != "-e ."]

setup(
    name="mlproject",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)