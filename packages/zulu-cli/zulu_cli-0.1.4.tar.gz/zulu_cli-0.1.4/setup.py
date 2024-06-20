from setuptools import setup, find_packages

setup(
    name="zulu-cli",
    version="0.1.4",
    packages=find_packages(),
    install_requires=[
        "pyyaml",
    ],
    entry_points={
        'console_scripts': [
            'zulu=zulu.main:main',
        ],
    },
    author="Zulu Labs",
    author_email="anderson@zuluapp.io",
    description="A CLI tool to help tech team to improve tasks",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/zuluapp/zulu-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)