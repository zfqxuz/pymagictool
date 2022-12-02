import setuptools

with open("README.md", "r", encoding='utf8') as fh:
  long_description = fh.read()

setuptools.setup(
  name="pymagictool",
  version="0.0.3",
  author="ZL",
  author_email="zfqxuz@gmail.com",
  description="Great Vision of a no name",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/zfqxuz/pymagictool",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: GNU General Public License v3 (GPLv3) ",
  "Operating System :: OS Independent",
  ],
)