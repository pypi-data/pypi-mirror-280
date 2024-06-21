from setuptools import setup, find_packages

VERSION = '2.1'
DESCRIPTION = 'Simple functions for working with time'
LONG_DESCRIPTION = "Simple functions for working with time. There aren't any dependencies yet."

setup(
    name="time-functions",
    version=VERSION,
    author="@michaelrex2012",
    author_email="<michaelgiu2012@outlook.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['alive-progress'],
    license="MIT",
    url="https://github.com/michaelrex2012/time-functions",

    keywords=['python', 'time', 'basic'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
