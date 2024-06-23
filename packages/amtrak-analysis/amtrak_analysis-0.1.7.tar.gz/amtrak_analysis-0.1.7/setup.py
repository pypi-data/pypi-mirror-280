from setuptools import setup, find_packages

setup(
    name='amtrak_analysis',
    version='0.1.7',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['data/Amtrak.csv']},
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'statsmodels',
    ],

    description='A library for analyzing Amtrak ridership data',
)