from setuptools import setup, find_packages

setup(
    name='chipignite',
    version='0.0.1',
    author='Efabless corp.',
    author_email='shuttle@efabless.com',
    description='A python package for all things chipignite',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/your-repo-name',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
