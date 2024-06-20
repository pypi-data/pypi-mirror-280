from setuptools import setup, find_packages

setup(
    name="qpop",
    version="1.1",
    description = "qpop --queue queue.txt --gpus 0,1,2,3",
    packages=find_packages(),
    install_requires=['inputimeout'],
    entry_points={
        'console_scripts': [
            'qpop = qpop.runner:main',
        ],
    }
)
