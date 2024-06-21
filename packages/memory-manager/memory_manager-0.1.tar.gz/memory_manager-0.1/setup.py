from setuptools import setup, find_packages

# python setup.py sdist bdist_wheel
# pip install .

setup(
    name="memory_manager",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pymem"
    ],
    author="FURYMOB",
    author_email="",
    description="Memory manager for hooking and manipulating game memory",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
