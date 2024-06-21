from setuptools import setup, find_packages

setup(
	author = "Luis Enrique Quispe Paredes (lquispe@transmin.com)",
	description = "A simple package for add dev source paths to sys.path.",
	name = "pydevroutes",
	version = "0.1.2",
	packages = find_packages(include=["pydevroutes", "pydevroutes.*"]),
	)