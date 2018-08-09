# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='eposfederator.libs',
    version='0.0.1',
    description='Common classes required by the eposfederator suite',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    namespace_packages=['eposfederator'],
    install_requires=['tornado', 'shapely', 'numpy', 'rtree', 'aiohttp', 'aiostream'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
