from setuptools import setup, find_packages

setup(
    name='dbx_utils',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'databricks-api'
    ],
    author='YRanjit MAity',
    author_email='ranjitmaity95@gmail.com',
    description='A utility package for managing Databricks folders and permissions',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
