# setup.py

from setuptools import setup, find_packages

setup(
    name='myredditbot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    entry_points={
        'console_scripts': [
            'topcontributors=myredditbot.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A Reddit bot to fetch top contributors from a subreddit',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/myredditbot',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
