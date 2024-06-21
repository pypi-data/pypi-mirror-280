from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='easyqt',
    version='0.3',
    packages=find_packages(),
    author='Jonathan Mafi',
    author_email='jmafi3d@gmail.com',
    install_requires=[
        'PyQt5'
    ],
    description="A collection of custom built pyqt widgets and wrappers for quick, easy and fun GUI development",
    readme="README.md",
    python_requires='>=3.6',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
