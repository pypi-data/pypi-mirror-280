from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="kzw_fib_py",
    version="0.0.1",
    author="kzw3933",
    author_email="3099097649@qq.com",
    description="Calculates a Fibonacci number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kzw3933/kzw-fib-py",
    install_requires=[],
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