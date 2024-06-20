from setuptools import setup, find_packages

setup(
    name='sphere_response_package',
    version='1.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PyQt5',
        'numpy',
        'matplotlib',
        'pandas',
        'scipy',
        'qdarkstyle'
    ],
    entry_points={
        'console_scripts': [
            'sphere_main=my_sphere_package.sphere_main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A package for sphere response calculations with a PyQt5 GUI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://your.project.url',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
