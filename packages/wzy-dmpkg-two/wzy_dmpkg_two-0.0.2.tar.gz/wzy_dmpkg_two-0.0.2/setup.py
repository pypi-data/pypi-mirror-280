# setup.py

from setuptools import setup, find_packages

setup(
    name='wzy_dmpkg_two',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'numpy'
    ],
    description='Any description you can put',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Dr. Zhiyuan Wang',
    author_email='wang1399@e.ntu.edu.sg',
    url='https://github.com/Dr-WangZhiyuan/wzy_dmpkg_two',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
