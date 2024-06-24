from setuptools import setup, find_packages

setup(
    name='ar2en',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyperclip',
    ],
    entry_points={
        'console_scripts': [
            'ar2en=ar2en.ar2en:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A CLI tool for converting text between Arabic and English keyboard layouts.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ar2en',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
