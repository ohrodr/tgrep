from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='tgrep',
      version=version,
      description="Time series grep with regular expression filtering",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='grep time regex',
      author="Robb O'Driscoll",
      author_email='https://twitter.com/oh_rodr',
      url='https://twitter.com/oh_rodr',
      license='Apache 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points={
      'console_scripts':
          ['tgrep = tgrep.tgrep:run'],
}
      )
