from setuptools import setup, find_packages

setup(
    name='myredditbot2',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'topusers=myredditbot2.topusers:main',
        ],
    },
)
