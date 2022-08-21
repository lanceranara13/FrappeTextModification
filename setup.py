from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in text_modification/__init__.py
from text_modification import __version__ as version

setup(
	name="text_modification",
	version=version,
	description="Text Modification",
	author="Lance Ranara",
	author_email="ranaralance0@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
