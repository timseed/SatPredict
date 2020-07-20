from setuptools import setup, find_packages

requirements = 'wheel', 'ephem', 'requests',
for p in find_packages():
    print("Installing package "+str(p))
setup(
    name='ham',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True, #Uses Manifest.IN
    url='',
    license='Public',
    author='tim',
    author_email='tim@sy-edm.com',
    description='Ham Radio Sat tracking Module.',
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest',
            'pytest-pep8',
            'pytest-cov',
            'sphinx',
            'recommonmark',
            'black',
            'pylint',
        ]},
    #Dev can be triggered by
    #python setup.py sdist
    #pip install dist/ham-0.0.1.tar.gz[dev]
    #
)

