from setuptools import find_packages, setup

setup(
   name='setup-reward-repo',
   version='0.1.0',
   description='Demonstration of custom reward functions',
   package_dir={"": "src"},
   packages=find_packages("src"),
   install_requires=['syllables'],
)
