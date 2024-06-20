from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='SunoAI', 
    version='1.0.6',
    description='Python API for interacting with the Suno AI music generator - Unofficial',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Malith-Rukshan/Suno-API',
    author='Malith Rukshan',
    author_email='hello@malith.dev',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.7',
    install_requires=[
        'requests', 'pydantic'
    ], 
)
