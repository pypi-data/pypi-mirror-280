from setuptools import setup, find_packages

setup(
    name='call-sequencer',
    version='1.0.2',
    packages=find_packages(),
    author='Sjal Choudhari',
    author_email='sjlchoudhari@gmail.com',
    description='A Python package for sequencing function calls as blocks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SujalChoudhari/call-sequencer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
