from setuptools import setup
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='SimplyEDA',
    version='0.1.6',  # Update the version number
    description='A simple library for exploratory data analysis',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/kitranet/SimpleEDA',
    author='M.R.Vijay Krishnan',
    author_email='vijaykrishnanmr@gmail.com',
    py_modules=['SimplyEDA'],
    install_requires=[
        'seaborn',
        'matplotlib',
        'numpy',
        'pandas',
        'statsmodels'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='EDA data-analysis',
    python_requires='>=3.6',
)