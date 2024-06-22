from setuptools import setup, find_packages

# python setup.py sdist bdist_wheel
# twine upload dist/*
# pip install .
# ctrl + shift + v

setup(
    name="memory_manager",
    version="0.31",
    packages=find_packages(),
    install_requires=[
        "pymem"
    ],
    author="FURYMOB",
    author_email="",
    description="Memory manager for hooking and manipulating game memory",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=['videogame', 'memory', 'addresses', 'manager', 'triggers'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
