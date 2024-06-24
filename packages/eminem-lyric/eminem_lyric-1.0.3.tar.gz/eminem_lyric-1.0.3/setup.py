from setuptools import setup, find_packages

# Read the contents of README.md file to set as the long description
with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='eminem_lyric',
    version='1.0.3',
    packages=find_packages(),
    description='A Python package for fetching Eminem song lyrics.',
    long_description=long_description,  # Use README.md content as long description
    # Specify that long description is in Markdown format
    long_description_content_type='text/markdown',
    author='Emads',
    author_email='ems22.dev@gmail.com',
    url='https://github.com/emads22/eminem-lyric-package',
    license='MIT',
    install_requires=[
        'requests',
    ],
    keywords=['eminem', 'lyric', 'lyrics', 'api'],
    classifiers=[
        # License
        'License :: OSI Approved :: MIT License',

        # Operating System
        'Operating System :: OS Independent',

        # Programming Language
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',

        # Development Status
        'Development Status :: 5 - Production/Stable',

        # Intended Audience
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: End Users/Desktop',

        # Topic
        'Topic :: Software Development',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Utilities',
    ]
)
