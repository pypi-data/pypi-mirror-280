from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()
  
setup(
    name='hack0',
    version='0.0.0.1',
    author='ZerProg studio',
    # install_requires=['tqdm'],
    description='Module under development.',
    long_description=readme(),
    packages=find_packages()
)
# python setup.py sdist bdist_wheel
# twine upload --repository pypi dist/*
# pypi-AgEIcHlwaS5vcmcCJGM1ZGU0YTg5LWU2Y2EtNDIxZC04MjhkLTc0MDE5YmJkOTk4MgACKlszLCI4ZTBkMTQzZi0xMjRhLTQ3NDUtOGFiZi0zMzlmZTVjYWQwMTUiXQAABiBKQmzIf19biKn9BOPUEHpSlluXvhrVBci6tVm1nHjKNw