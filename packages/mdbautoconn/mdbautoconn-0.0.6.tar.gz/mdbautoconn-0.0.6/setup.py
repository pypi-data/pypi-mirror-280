from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."


"""def get_requirement(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.3"
REPO_NAME = "mongodbconnectorpkg"
PKG_NAME = "databaseautomation"
AUTHOR_USER_NAME = "Pranavbp525"
AUTHOR_EMAIL = "pranav.bp525@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting to a database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    projct_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    install_requires=get_requirement("./requirements_dev.txt"),


)"""


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.6"
REPO_NAME = "mongodbconnectorpkg"
PKG_NAME = "mdbautoconn"
AUTHOR_USER_NAME = "Pranavbp525"
AUTHOR_EMAIL = "pranav.bp525@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    )

