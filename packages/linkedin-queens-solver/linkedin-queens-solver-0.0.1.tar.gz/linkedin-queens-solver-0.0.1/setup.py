from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='linkedin-queens-solver',
     version='0.0.1',
     author="utkarsh-deshmukh",
     author_email="utkarsh.deshmukh@gmail.com",
     description="lib to solve the linkedin daily challenge `Queens`",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/Utkarsh-Deshmukh/Linkedin_Queens_challenge",
     download_url="https://github.com/Utkarsh-Deshmukh/Linkedin_Queens_challenge/archive/refs/heads/main.zip",
     install_requires=['numpy', 'opencv-python'],
     license='MIT License',
     keywords='Linkedin Daily challenge Queens',
     packages=find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: BSD License",
         "Operating System :: OS Independent",
     ],
 )