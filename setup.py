"""
Flask-Keycloak
-------------

Keycloak API client to create/provision users on Keycloak
"""
from setuptools import setup


setup(
    name='Flask-Keycloak',
    version='1.0',
    url='http://www.keycloak.org/docs/rest-api/',
    license='MIT',
    author='Alfonso Roman',
    author_email='alroman@ucla.edu',
    description='Keycloak API client',
    long_description=__doc__,
    py_modules=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
