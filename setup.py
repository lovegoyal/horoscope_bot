from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(name='astro_bot',
      version='0.1',
      description='A daily horoscope Telegram bot.',
      long_description=readme,
      author='Ramit Mittal'
      url='http://github.com/ramitmittal/astro_bot',
      license=license,
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      install_requires=['requests', 'bs4', 'lxml', 'telepot', 'redis'],
      entry_points={
          'console_scripts': ['astro_bot=astro_bot.cmd:start_everything']
       })
