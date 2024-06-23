from setuptools import setup, find_packages

def _find_packages():
  packages = find_packages(where='termtalk')
  packages.append('termtalk')
  return packages

with open('README.md', 'r') as f:
  description = f.read()

setup(
  name='termtalk',
  version= '0.2.0',
  packages= _find_packages(),
  # packages= find_packages(),
  install_requires=[
      'pyrebase4>=4.8.0'
  ],
  entry_points={
    "console_scripts":[
      "termtalk = termtalk:start"
    ]
  },
  author='Dzadafa',
  author_email=' Dzakwan Daris <dzakwandarisfakhruddin@gmail.com>',
  license='MIT Licencse',
  classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
  ],
  description='Use to chat with Public random on Terminal',
  long_description=description,
  long_description_content_type='text/markdown',
  include_package_data=True,
  package_dir={
    'termtalk':'termtalk',
  }
)