from setuptools import setup, find_packages

setup(
    name='ishan_x509',
    version='0.1.0',
    description='x509 certificates',
    author='Ishan Gupta',
    author_email='ishangupta2312@gmail.com',
    # url='github',
    packages=find_packages(),
    install_requires=[
        'cryptography',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
