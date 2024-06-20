from setuptools import setup, find_packages

setup(
    name='planet_lib',
    version='0.1',
    packages=find_packages(),
    description='Una libreria multiuso',
    author='Simoo_',
    author_email='simonecardella8@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'discord.py',
    ],
    python_requires='>=3.6',
)
