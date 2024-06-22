from setuptools import setup

setup(
    name            = 'pokemon_statics',
    author          = 'alevellop',
    url             = 'https://github.com/alevellop/pokemon_statics',
    version         = '0.0.1',
    license         = 'MIT',
    description     = 'Library of pokemon statics',
    keywords        = ['pokemon', 'data', 'api', 'csv', 'dataframe', 'pytest', 'sqlalchemy', 'aiohttp', 'pandas'],
    install_requires= ['pytest', 'sqlalchemy', 'aiohttp', 'pandas'],
    classifiers     = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
    ],
)