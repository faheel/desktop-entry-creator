from setuptools import setup
from codecs import open


# Get the long description from README.md
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='desktop-entry-creator',
    version='0.1.0',
    description='A user-friendly GUI for creating desktop entries for '
                'installed applications on Linux.',
    long_description=long_description,
    url='https://github.com/faheel/desktop-entry-creator',
    author='Faheel Ahmad',
    author_email='faheel@live.in',
    license='GPLv3',
    classifiers=[
        'Natural Language :: English',
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Topic :: Utilities',
        'Environment :: X11 Applications',
        'Intended Audience :: End Users/Desktop',
    ],
    keywords='gui linux desktop-entry desktop-entry-creator pygobject gtk',
    packages=['desktop_entry_creator'],
    package_data={
        'desktop_entry_creator': ['res/*'],
    },
    install_requires=['pygobject', 'python-slugify'],
    extras_require={
        'dev': ['pylint'],
    },
    entry_points={
        'gui_scripts': [
            'desktop-entry-creator=desktop_entry_creator.app:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/faheel/desktop-entry-creator/issues',
        'Source': 'https://github.com/faheel/desktop-entry-creator',
    },
)
