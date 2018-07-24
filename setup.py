import os

from setuptools import find_packages, setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='politico-services-api',
    version='0.1.0',
    packages=find_packages(exclude=('', 'docs',)),
    include_package_data=True,
    url='https://github.com/The-Politico/politico-services-api',
    license='MIT',
    description='A Django project.',
    python_requires='>=3',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'django',
        'flake8',
        'fabric3',
        'jinja2',
    ],
    entry_points='''
        [console_scripts]
        onespot=onespot:cli
    '''
)