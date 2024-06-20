from setuptools import setup, find_packages

setup(
    name='fallpwn',
    version='0.1.1',
    author='ltfall',
    author_email='wanqiultfall@gmail.com',
    description='A useful tool for userland pwn.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
