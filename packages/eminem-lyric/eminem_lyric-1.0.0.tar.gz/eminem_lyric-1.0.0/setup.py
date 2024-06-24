from setuptools import setup, find_packages

setup(
    name='eminem_lyric',
    version='1.0.0',
    packages=find_packages(),
    description='A Python package for fetching Eminem song lyrics.',
    long_description = '''eminem_lyric is a Python package that provides a convenient interface for fetching and accessing lyrics of Eminem songs using an external lyrics API. 
It offers methods to retrieve both processed lyrics and raw lyric data, allowing users flexibility in accessing the lyrics. 
Whether you're an Eminem fan looking to explore his vast discography or a developer wanting to integrate Eminem lyrics into your applications, eminem_lyric has got you covered.''',
    author='Emads',
    author_email='ems22.dev@gmail.com',
    url='https://github.com/emads22/eminem-lyric-package',
    license='MIT',
    install_requires=[
        'requests',
    ],
    keywords=['eminem', 'lyric', 'lyrics', 'api'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
