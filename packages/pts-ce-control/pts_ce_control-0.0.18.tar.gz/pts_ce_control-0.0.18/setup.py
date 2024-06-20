from setuptools import find_packages, setup
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pts_ce_control",
    version="0.0.18",
    description="Controls the PTS Cell Emulator",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/julianpass/cell-emulator-control-app",
    author="Pass Testing Solutions GmbH",
    author_email="info@pass-testing.de",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(include=['pts_ce_control']),
    include_package_data=True,
    install_requires=['python-can>=4.0.0', 'dash==2.5.1', 'cantools>=37.0.7', 'tabulate==0.8.10', 'uptime==3.0.1'],
    entry_points={
        "console_scripts": [
            "pts_ce_control=pts_ce_control.__main__:main",
        ]
    },
)
