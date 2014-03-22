from setuptools import setup, find_packages
import re
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()

def get_version(config_fname):
    pattern = re.compile(r'#define AppVersion "(\d.\d.\d)"')
    with open(config_fname) as config:
        for line in config:
            m = pattern.match(line)
            if m:
                return m.group(1)
        else:
            raise ValueError("%s does not contain a valid version")

version = get_version(os.path.join(here, 'version.iss'))

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies

    # PyQt4
    # Hg
]


setup(name='openhea',
    version=version,
    description="",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='open-ihm provides an open source software program for the analysis of data collected using the Individual Household Model Approach: international-development development',
    author='Brown Msiska, Tiwonge Manda, Evidence for Development, University of Wolverhampton',
    author_email='tiomanda@gmail.com',
    url='http://code.google.com/p/open-ihm/',
    license='LGPL',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['openihm=openihm:openihm']
    }
)
