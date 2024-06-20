from setuptools import find_packages, setup
import pathlib

with open("README.md", "r") as f:
    long_description = f.read()

with open(str(pathlib.Path(__file__).parent.absolute()) + "/kzw_fib_py/version.py", "r") as f:
    version = f.read().split("=")[1].replace("'", "")

setup(
    name="kzw_fib_py",
    version=version,
    author="kzw3933",
    author_email="3099097649@qq.com",
    description="Calculates a Fibonacci number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kzw3933/kzw-fib-py",
    install_requires=[
        "PyYAML>=4.1.2",
        "dill>=0.2.8"
    ],
    extras_require={
        'server': ["Flask>=1.0.0"]
    },
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fib-numb=kzw_fib_py.cmd.fib_numb:fib_numb',
        ],
    },
)