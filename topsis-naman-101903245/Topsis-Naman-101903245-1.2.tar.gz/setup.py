from distutils.core import setup
setup(
  name = 'Topsis-Naman-101903245',         # How you named your package folder (MyLib)
  packages = ['Topsis-Naman-101903245'],   # Chose the same as "name"
  version = '1.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This package helps to find the topsis score and ranking based on that score for the given input.',   # Give a short description about your library
  author = 'Naman Gupta',                   # Type in your name
  author_email = 'your.email@domain.com',      # Type in your E-Mail
  url = 'https://github.com/naman-gupta-908/Topsis-Naman-101903245',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/naman-gupta-908/Topsis-Naman-101903245/archive/refs/tags/1.2.tar.gz',    # I explain this later on
  keywords = ['TOPSIS', 'RANKS', 'SCORE'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)