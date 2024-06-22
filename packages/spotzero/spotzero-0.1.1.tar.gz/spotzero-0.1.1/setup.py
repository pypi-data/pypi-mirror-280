from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="spotzero",
    version="0.1.1",
    install_requires=["dbus-python==1.3.2", "click>=8.1"],
    description="control the spotify app with a cli or with a package",
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        "console_scripts": [
            "spotzero = spotzero.cli:cli",
        ],
    },
)
