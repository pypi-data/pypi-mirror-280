from setuptools import setup, find_packages

setup(
    name='bbp4adg',
    version='0.1.0',
    author='Borui Cai',
    author_email='borui_cai@qq.com',
    description='BoostedBuidlingProcessForADG',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/S2thend/BoostedBuidlingProcessForADG',
    packages=find_packages(),
    install_requires=[
        'numpy==1.24.4',
        'pandas==2.0.3'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
