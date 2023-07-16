from setuptools import setup, find_packages

classifiers = [
    'Developer Status :: 5 - Production/Stable'
    'Intented Audience :: Developers'
    'Operating System :: Microsoft :: Windows :: Windows 10 :: Windows 11'
    'License :: MIT License'
    'Programming Language :: Python : 3'
]

setup(
    name='shiba_mysql',
    version='1.0.0',
    description='A library to interact with MySQL',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    author='Rodrigo Pino',
    license='MIT',
    classifiers=classifiers,
    keywords='mysql',
    author_email='ro.pinoo18@gmail.com',
    url='https://github.com/ShibaRoPinoo/Shiba-Py-Mysql',
    packages=['shiba'],
    install_requires=['pymysql'],
)