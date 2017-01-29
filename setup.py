from setuptools import setup

setup(
    name='lyrics',   
    version='0.1',                         
    scripts=['lyrics'] ,
    install_requires=['requests', 'beautifulsoup4'],
    entry_points={
          'console_scripts': [
              'lyrics = lyrics.show_lyrics:main'
          ]
     }

   )
