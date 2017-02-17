"""Setup file for justPark."""
from setuptools import setup

setup(name='tsei_scraper_just_park',
      version='0.1',
      description='TSEI Scraper for justPark',
      url='ssh://git@github.com:ZetaDelta/tsei_scraper_just_park',
      author='Alexander Funcke',
      author_email='funcke@zd.ee',
      license='NDA',
      packages=['tsei_scraper_just_park'],
      test_suite="tests",
      install_requires=['scrapy'],
      zip_safe=False)
