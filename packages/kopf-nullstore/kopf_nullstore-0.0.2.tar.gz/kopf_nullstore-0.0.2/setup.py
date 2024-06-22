from setuptools import setup, find_packages

setup(
    name='kopf-nullstore',
    version=open('VERSION').read(),
    packages=find_packages(),
    install_requires=[
        'kopf',
    ],
    author='David Collom',
    author_email='david@collom.co.uk',
    description='A Null Store package for kopf.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/davidcollom/kopf-nullstore',  # Update with your actual repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
