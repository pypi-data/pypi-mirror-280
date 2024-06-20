from setuptools import setup, find_packages

setup(
    name="qpop",
    version="1.4",
    description="qpop -q queue.txt -g 0,1,2,3",
    long_description="qpop --queue queue.txt --gpus 0,1,2,3",
    readme='README.md',
    packages=find_packages(),
    install_requires=['inputimeout'],
    entry_points={
        'console_scripts': [
            'qpop = qpop.runner:main',
        ],
    }
)
