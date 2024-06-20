from setuptools import setup, find_packages

setup(
    name='gradescalculator',
    version='0.4',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'average=gradescalculator.main:main',
        ],
    },
    author='Quentin Berthet',
    author_email='quentin@berthet.ch',
    description='Un package pour calculer des notes avec des poids différents.',
    url='https://github.com/BERTHETquentin/GradesCalculator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
