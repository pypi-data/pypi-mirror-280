from setuptools import setup, find_packages

setup(
    name='key_encryption_gui',
    version='1.0.2',  
    packages=find_packages(),  
    py_modules=['key_encryption_gui'], 
    install_requires=[
        'cryptography>=40.0.2'
    ],
    entry_points={
        'console_scripts': [
            'key_encryption_gui=key_encryption_gui:main_entry',
        ],
    },
    author='burnem',  
    author_email='dfkburnem@gmail.com',  
    description='A GUI for encrypting private keys',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dfkburnem/Key-Encryption-GUI',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
    ],
    python_requires='>=3.6,<4',
)
