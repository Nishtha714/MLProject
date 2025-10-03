import os
from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

# ✅ Build absolute path to requirements.txt
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REQ_FILE = os.path.join(BASE_DIR, "requirements.txt")

setup(
    name="mlproject",
    version="0.0.1",
    author="Nishtha",
    author_email="nishthadhariwal2005@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(REQ_FILE),
)
