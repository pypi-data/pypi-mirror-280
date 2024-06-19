from setuptools import setup, find_packages

setup(
    name='msg91-one-api',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Harsh Jaiswal',
    author_email='harsh@walkover.in',
    description='A package for utilizing MSG91 service integration',
    url='https://github.com/Walkover-Web-Solution/msg91-python-plugins',  # Replace with your GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)