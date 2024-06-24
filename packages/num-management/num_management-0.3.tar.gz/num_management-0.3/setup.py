from setuptools import setup, find_packages
import os

def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name), encoding='utf-8') as f:
        return f.read()

setup(
    name="num_management",
    version="0.3",
    packages=find_packages(),
    description="This Library is used for manage numbers with different methods. Method int2str is included in this library.",
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author="Carlos Alberto Olvera Rodriguez",
    author_email="orcas40@gmail.com",
    url="https://bitbucket.org/onprem/olvera_carlos_interview-numbertostring-python/src/caor_int_to_string/",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)