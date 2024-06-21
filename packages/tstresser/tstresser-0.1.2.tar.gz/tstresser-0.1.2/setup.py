from setuptools import setup, find_packages

setup(
    name='tstresser',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'matplotlib==3.9.0',
        'pytest==8.2.2',
        'requests==2.32.3',
        'requests-oauthlib==2.0.0',
        'tqdm==4.66.4'
    ],
    entry_points={
        'console_scripts': [
            'tstresser=tstresser.cli:main'
        ]
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A CLI-based stress tester for APIs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/deestarks/t-stresser',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
