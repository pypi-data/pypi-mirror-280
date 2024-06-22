from setuptools import setup, find_packages

setup(
    name='amtrak_analysis',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'statsmodels',
    ],
    package_data={
        'amtrak_analysis': ['data/*.csv'],
    },
    include_package_data=True,
    description='A library for Amtrak data analysis and smoothing methods',
    url='https://github.com/yourusername/amtrak_analysis',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)