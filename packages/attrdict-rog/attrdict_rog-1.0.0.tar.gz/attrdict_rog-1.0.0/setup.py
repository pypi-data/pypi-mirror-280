"""
To install AttrDict:

    python setup.py install
"""
from setuptools import setup


DESCRIPTION = "A dict with attribute-style access"

try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    LONG_DESCRIPTION = DESCRIPTION


setup(
    name="attrdict_rog",
    version="1.0.0",
    author="Michael Roger ZONGO",
    author_email="michaelrogerzongo@gmail.com",
    packages=("attrdict_rog",),
    url="https://github.com/root-gift/attrdict-rog.git",
    license="MIT License",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: 7 - Inactive",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    install_requires=(
        'six',
    ),
    tests_require=(
        'nose>=1.0',
        'coverage',
    ),
    zip_safe=True,
)
