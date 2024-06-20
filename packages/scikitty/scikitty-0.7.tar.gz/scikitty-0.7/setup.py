from setuptools import setup, find_packages

readme = open("./READEME.md", "r")

def read_requirements():
    with open('requirements.txt') as req_file:
        return req_file.read().splitlines()

setup(
    name='scikitty',
    packages=find_packages(),
    install_requires=read_requirements(),
    version=0.7,
    description='A package to create Decision Trees like Scikitlearn.',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='John Rojas',
    author_email='john.rojas.chinchilla@gmail.com',
    url='https://github.com/JohnRojas222/SciKittyPackage/',
    download_url='https://github.com/JohnRojas222/SciKittyPackage/tarball/0.1',
    keywords=['scikitlearn', 'decision trees', 'metrics'],
    classifiers=[],
    license='MIT',
    include_package_data=True
)