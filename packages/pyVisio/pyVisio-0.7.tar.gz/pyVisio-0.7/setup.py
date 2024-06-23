from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "docs" / "pypi.md").read_text()

setup(
    name='pyVisio',
    version='0.7',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'plotly',
        'pandas',
        'numpy',
        'statsmodels',
        'weasyprint',
        'jinja2'
    ],
    extras_require={
        'pygobject': ['pygobject']
    },
    author='Hüseyin Kaya',
    author_email='kaya87826@gmail.com',
    description='Interactive and dynamic data visualization library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kayahuseyinn/pyVisio',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

)
