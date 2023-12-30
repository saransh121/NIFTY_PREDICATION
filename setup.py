from setuptools import find_packages,setup

HYPEN_E = '-e .'
def readRequrimentFile(file_path):
    with open(file_path,'r') as Fileobj:
        data  = Fileobj.readlines()
    if HYPEN_E in data:
        data.remove(HYPEN_E)
    return data

setup(
    name='Nifty Predication',
    version='0.0.1',
    author='Saransh',
    author_email='saranshrayguru@gmail.com',
    packages=find_packages(),
    install_requires = readRequrimentFile('requriments.txt')
)