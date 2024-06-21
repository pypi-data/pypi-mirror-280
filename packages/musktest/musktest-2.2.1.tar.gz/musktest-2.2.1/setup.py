"""
Author:木森
"""
from setuptools import setup, find_packages

with open("readme.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setup(
    name='musktest',
    version='2.2.1',
    author='MuSen',
    author_email='121292679@qq.com',
    url='https://github.com/musen123/MuskTest',
    description='a no code api testing framework',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["Jinja2==3.0.3",
                      "PyYAML==5.3.1",
                      "requests==2.24.0",
                      "requests-toolbelt == 0.9.1",
                      "PyMySQL== 1.0.2",
                      "rsa== 4.7.2",
                      "jsonpath== 0.82",
                      "pyasn1== 0.4.8",
                      "faker == 8.11.0",
                      ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mst = musktest.manage:main',
        ],
    },
    package_data={
        "": ["*.html", '*.md'],
    },
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
