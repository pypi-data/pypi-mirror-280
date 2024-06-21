from setuptools import setup, find_packages

setup(
    name='OperationBattleshipJobCategoryClassifier',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    author='Matthew Caraway',
    author_email='your.email@example.com',
    description='A package for classifying job categories using BERT.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/OperationBattleshipJobCategoryClassifier',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
