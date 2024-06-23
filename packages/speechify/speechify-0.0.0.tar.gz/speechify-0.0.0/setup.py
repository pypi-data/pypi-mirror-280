# setup.py

import setuptools
import speechify

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='speechify',
    version=speechify.__version__,
    author='Billy Bat',
    author_email='billybat@duck.com',
    description='Unofficial speechify TTS module',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rewrite5/speechify-tools',
    packages=setuptools.find_packages(exclude=['sphinx_docs', 'docs', 'tests']),
    python_requires='~=3.9',
    install_requires=[
        i.replace('\n', '')
        for i in open('requirements.txt', 'r').readlines()
    ],
    extras_require={
        'dev': ['setuptools', 'wheel', 'twine', 'Sphinx'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
