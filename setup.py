from setuptools import setup, find_packages

from matterfour import current_version

required_pkgs = (
    'requests>=2.4.0',
)

exclude_pkgs = (
    '*test*',
    '*local*',
)

setup(
    name='matterfour',
    version=current_version(),
    license='MIT',
    description='A Bot for MatterMost API v4',
    keywords="bot mattermost chat agent",
    long_description=open('README.md').read(),
    author="seLain",
    author_email='selain@nature.ee.ncku.edu.tw',
    url='http://github.com/seLain/matterfour',
    platforms=['Any'],
    packages=find_packages(exclude=exclude_pkgs),
    install_requires=required_pkgs,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
