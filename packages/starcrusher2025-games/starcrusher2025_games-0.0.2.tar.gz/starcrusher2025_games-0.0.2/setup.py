from setuptools import setup, find_packages

setup(
    name='starcrusher2025_games',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'pygame',
    ],
    entry_points={
        'console_scripts': [
            'starcrusher2025-games = starcrusher2025_games.game:main',
        ],
    },
    author='starcrusher2025',
    description='A game engine.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/starcrusher2025/2025_games',
    license='MIT',
)