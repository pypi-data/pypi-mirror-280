from setuptools import setup, find_packages

setup(
    name='lom-api',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Eiki Nishi',
    author_email='nishi@lom-inc.jp',
    maintainer='LoM.inc.',
    description='A client library for the LoM API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/lom/lom-api',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
