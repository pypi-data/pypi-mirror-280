from setuptools import setup, find_packages

setup(
    name='multispectral_processor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'numpy',
        'scikit-learn',
    ],
    entry_points={
        'console_scripts': [
            'process-multispectral=multispectral_processor.processor:process_multispectral_data',
        ],
    },
    author='Muzammil Ali A',
    author_email='muzammilali3579@gmail.com',
    description='A package to process multispectral images.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/muzammilali3579/multispectral_processor.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
