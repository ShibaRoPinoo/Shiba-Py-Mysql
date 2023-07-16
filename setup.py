from setuptools import setup, find_packages

classifiers = [
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Database',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='shiba_mysql',
    version='1.1.1',
    description='A library to interact with MySQL',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type='text/markdown',
    author='Rodrigo Pino',
    license='MIT',
    classifiers=classifiers,
    keywords=['mysql', 'database', 'SQL', 'data access', 'ORM'],
    author_email='ro.pinoo18@gmail.com',
    url='https://github.com/ShibaRoPinoo/Shiba-Py-Mysql',
    packages=find_packages(),
    install_requires=['pymysql'],
)
