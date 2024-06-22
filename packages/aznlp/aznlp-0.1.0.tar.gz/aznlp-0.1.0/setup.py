from setuptools import setup, find_packages

setup(
    name='aznlp',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            
        ],
    },
    author='Tifosi AI',
    author_email='abdullahkazimov@icloud.com',
    description='🇦🇿 AZNLP - Natural Language Processing (NLP) library for Azerbaijani Language',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tifosiai/aznlp',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
