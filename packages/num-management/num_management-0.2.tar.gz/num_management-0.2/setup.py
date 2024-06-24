from setuptools import setup, find_packages

setup(
    name="num_management",
    version="0.2",
    packages=find_packages(),
    description="This Library is used for manage numbers with different methods. Method int2str is included in this library.",
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