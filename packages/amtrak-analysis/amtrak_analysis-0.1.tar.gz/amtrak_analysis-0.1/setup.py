from setuptools import setup, find_packages

setup(
    name='amtrak_analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'statsmodels',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A library for Amtrak data analysis and smoothing methods',
    url='https://github.com/yourusername/amtrak_analysis',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)