from setuptools import setup, find_packages

setup(
    name='supermath',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    description='A package for basic mathematical calculations',
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
