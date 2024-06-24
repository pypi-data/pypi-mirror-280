from setuptools import setup, find_packages

setup(
    name="num_management",
    version="0.1",
    packages=find_packages(),
    description="A library to convert numbers to their word representation",
    author="Carlos Alberto Olvera Rodriguez",
    author_email="orcas40@gmail.com",
    url="https://bitbucket.org/onprem/olvera_carlos_interview-numbertostring-python/src/master/",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)