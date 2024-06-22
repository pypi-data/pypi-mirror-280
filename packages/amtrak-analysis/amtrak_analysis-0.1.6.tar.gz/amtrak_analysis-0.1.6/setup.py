from setuptools import setup, find_packages
import codecs

setup(
    name='amtrak_analysis',
    version='0.1.6',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'statsmodels',
    ],
    package_data={
        'amtrak_analysis': ['data/Amtrak.csv'],
    },
    description='A Python package for analyzing and visualizing Amtrak ridership data',
    long_description=codecs.open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
