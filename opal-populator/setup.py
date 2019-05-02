from setuptools import setup

setup(
    name='opal-populator',
    version='0.0.1',
    packages=['populator'],
    description='A command line interface for LifeCycle',
    url='https://github.com/lifecycle-project/data',
    author='Sido Haakma',
    author_email='sido@haakma.org',
    license='GNU Lesser General Public License 3.0',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'populator = populator.__main__:main'
        ]
    },
    install_requires=['Opal==2.13.1', 'Click==7.0']
)
