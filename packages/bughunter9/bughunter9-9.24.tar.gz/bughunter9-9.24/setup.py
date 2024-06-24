from setuptools import setup

setup(
    name='bughunter9',
    version='9.24',
    py_modules=['bughunter9'],
    entry_points={
        'console_scripts': [
            'bughunter9 = bughunter9:main',
        ],
    },
    install_requires=[],
)

