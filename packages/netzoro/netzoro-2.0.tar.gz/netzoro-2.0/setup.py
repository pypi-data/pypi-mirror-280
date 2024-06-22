from setuptools import setup, find_packages

setup(
    name='netzoro',
    version='2.0',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    package_data={
        'netzoro': ['files/*.py', 'files/*.ipynb']
    },
)
