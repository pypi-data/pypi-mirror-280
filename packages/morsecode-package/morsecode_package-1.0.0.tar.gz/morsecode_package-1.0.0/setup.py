from setuptools import setup, find_packages

setup(
    name='morsecode-package',
    version='1.0.0',
    description='Python package for converting text to Morse code and vice versa',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rahulaauji-30/morse.git',
    author='Rahul Parihar',
    author_email='rahulaauji71@gmail.com',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Text Processing',
    ],
    keywords='morse-code text-processing',
    python_requires='>=3.6',
)
