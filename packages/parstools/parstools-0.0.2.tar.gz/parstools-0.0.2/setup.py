"""Installation script."""
import textwrap as _tw
import typing as _ty

import setuptools as _stp


PACKAGE_NAME: _ty.Final[str] =\
    'parstools'
VERSION: _ty.Final[str] =\
    '0.0.2'
_VERSION_FILE: _ty.Final[str] =\
    f'{PACKAGE_NAME}/_version.py'
PYTHON_REQUIRES: _ty.Final[str] =\
    '>=3.11'
_CLASSIFIERS: _ty.Final[list[
        str]] = [
    'Development Status :: 2 - Pre-Alpha',
    'License :: Public Domain',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3 :: Only',
    ]
_KEYWORDS: _ty.Final[list[
        str]] = [
    'algorithms',
    'grammar',
    'lexer',
    'lexing',
    'LR(1)',
    'LR parser',
    'parsers',
    'parsing',
    ]


def _install_parstools(
        ) -> None:
    """Install package `parstools`."""
    _dump_version(VERSION, _VERSION_FILE)
    with open('README.md', 'r') as fd:
        long_description = fd.read()
    _stp.setup(
        name=PACKAGE_NAME,
        version=VERSION,
        license='Public Domain',
        description='Parsing algorithms',
        long_description=long_description,
        long_description_content_type='text/markdown',
        python_requires=PYTHON_REQUIRES,
        packages=[
            PACKAGE_NAME,
            f'{PACKAGE_NAME}._lr'],
        package_dir={
            PACKAGE_NAME:
                PACKAGE_NAME},
        classifiers=_CLASSIFIERS,
        keywords=_KEYWORDS,
        author='Ioannis Filippidis',
        author_email='jfilippidis@gmail.com',
        )


def _dump_version(
        version:
            int,
        filepath:
            str
        ) -> None:
    """Write `version` to `filepath`."""
    print(_tw.dedent(f'''
        Writing version of
        package {PACKAGE_NAME}
        to file: `{filepath}`
        '''))
    text = f'version = "{version}"'
    with open(filepath, 'w') as fd:
        fd.write(text)


if __name__ == '__main__':
    _install_parstools()
