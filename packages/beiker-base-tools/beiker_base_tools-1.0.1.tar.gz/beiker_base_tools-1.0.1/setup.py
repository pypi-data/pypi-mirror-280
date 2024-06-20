from setuptools import setup, find_packages

setup(
    name='beiker_base_tools',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'mysql-connector-python',
        'pillow' ,
    ],
)