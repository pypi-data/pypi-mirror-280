from setuptools import setup, find_packages

setup(
    name='ElsaMenu',
    version='1.0.0',
    author='Elsalamander',
    author_email='edilinguanotto@gmail.com',
    description='Easy menu with python3',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://gitlab.com/Elsalamander1/elsamenu',
    packages=find_packages(where='elsa_menu'),
    package_dir={'': 'elsa_menu'},
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
