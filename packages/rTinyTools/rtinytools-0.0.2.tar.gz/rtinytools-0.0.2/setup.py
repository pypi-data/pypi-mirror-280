from setuptools import setup, find_packages
from rTools.config import __version__, __author__, __email__

setup(
    name='rTinyTools',
    version=__version__,
    author=__author__,
    author_email=__email__,
    keywords=['rTools', 'tools', 'r-rools'],
    description='A cli tools to do everything.',
    long_description="""
    rfooox's Tools
    A cli tools to do everything.
    """,
    license='MIT Licence',
    url='https://pypi.org/project/rTool/',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=['PyYAML>=6.0.1',
                      'click>=8.0.4',],
    entry_points={
        'console_scripts': [
            'rtools = rTools.main:cli',
            'rTools = rTools.main:cli',
            'r-tools = rTools.main:cli',
        ]
    }
)
