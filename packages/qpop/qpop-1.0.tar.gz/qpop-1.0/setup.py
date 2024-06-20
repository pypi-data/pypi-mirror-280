from setuptools import setup, find_packages

setup(
    name="qpop",
    version="1.0",
    packages=find_packages(),
    install_requires=['inputimeout'],
    entry_points={
        'console_scripts': [
            'qpop = qpop.runner:main',
        ],
    }
)
