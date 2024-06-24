from setuptools import setup, find_packages

setup(
    name='eminem_lyric',
    version='1.0.1',
    packages=find_packages(),
    description='A Python package for fetching Eminem song lyrics.',
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
