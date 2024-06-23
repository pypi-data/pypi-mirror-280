from setuptools import setup, find_packages

setup(
    name='rgwml',
    version='0.0.78',
    author='Ryan Gerard Wilson',
    author_email='ryangerardwilson@gmail.com',
    description='Manipulate data with code that is less a golden retriever, and more a Samurai\'s sword',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ryangerardwilson/rgwml_py',
    packages=find_packages(),
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pandas',
        'numpy',
        'pymssql',
        'mysql-connector-python',
        'clickhouse-driver',
        'google-cloud-bigquery',
        'google-auth',
        'pandas-gbq',
        'xgboost',
        'matplotlib',
        'pillow',
        'scipy',
        'seaborn',
        'scikit-learn',
        'dask[dataframe]',
        'requests',
        'pymysql',
        'paramiko',
    ],
    entry_points={
        'console_scripts': [
            'rgwml=rgwml:main',
        ],
    },
    project_urls={
        'Homepage': 'https://github.com/ryangerardwilson/rgwml_py',
        'Issues': 'https://github.com/ryangerardwilson/rgwml_py/issues',
    },
)

