from setuptools import setup, find_packages

setup(
    name='amtrak_analysis',
    version='0.1.11',
    packages=find_packages(),
    include_package_data=True,
    package_data={'amtrak_analysis': ['data/Amtrak.csv']},
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'statsmodels',
    ],
    description='A library for analyzing Amtrak ridership data',
)