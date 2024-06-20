from setuptools import setup, find_packages

setup(
    name='Decisiontree_Table_Converter',
    version='0.1.0',
    packages=find_packages(),
    description='Convert decision trees into decision tables',
    long_description='',  # Empty long description
    long_description_content_type='',  # Empty content type
    author='Barican Colak',
    author_email='bariscolak9277@gmail.com',
    url='https://github.com/bariscolaak/DecisionTreeTableConverter',
    install_requires=[
        'pandas',
        'scikit-learn',
        'numpy',  # Ensure these match the dependencies you use
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.11'
    ],
)
