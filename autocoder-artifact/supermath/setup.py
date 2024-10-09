from setuptools import setup, find_packages

setup(
    name='supermath',
    version='0.1',
    packages=find_packages(include=['my_package', 'my_package.*']),
    description='A simple package for basic mathematical calculations',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/supermath',
)
