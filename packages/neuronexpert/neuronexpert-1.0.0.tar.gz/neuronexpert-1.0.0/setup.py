from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='neuronexpert',
  version='1.0.0',
  author='percyve11e',
  author_email='percyve11e.me@gmail.com',
  description='This is the lib to use Neuron Expert Assistant',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url=' https://neuron.expert',
  packages=find_packages(),
  install_requires=['requests>=2.25.1', 'aiohttp'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='neuron expert ',
  project_urls={
    'GitHub': 'https://github.com/nnevdokimov'
  },
  python_requires='>=3.6'
)