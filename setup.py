from setuptools import setup

testing_extras = [
    'pytest',
    'pytest-cov'
]


setup(
    name='python-flask-api',
    version='0.1',
    packages=['apps'],
    url='http://github.com/fsilvalucas/python-flask-api',
    license='',
    author='Lucas F. Silva',
    author_email='lucaslfsls@gmail.com',
    description='A python API with flask and MongoDB',
    keywords='API, MongoDB',
    include_package_data=True,
    zip_safe=False,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'testing': testing_extras,
    },
)
