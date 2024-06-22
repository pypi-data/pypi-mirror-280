from setuptools import setup, find_packages

setup(
    name='amtrak_analysis',
    version='0.1.5',
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
    long_description=open('README.md', encoding='utf-8').read(),  # 인코딩을 UTF-8로 지정
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
