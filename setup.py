# setup.py
from setuptools import setup, find_packages

setup(
    name='aih_django',
    version='0.1',
    packages=find_packages(),
    description='A collection of Django utilities',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Joseph',
    author_email='joseph@aiheroes.io',
    url='https://github.com/yourusername/aih-django-utils',
    install_requires=[
        'Django>=3.2',  # Specify the Django version compatibility
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
