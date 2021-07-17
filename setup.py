import setuptools
import os
import shutil

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PaFL",
    version="0.1.0",
    author="Javid Rzayev",
    author_email="rz.cavid@gmail.com",
    description="Parsing and sending terminal recording log to syslog",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Javid907/pafl",
    packages=['module'],
    scripts=['bin/run.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: *NIX OS's",
    ],
    python_requires='>=3',
)

path = "/etc/pafl"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

newPath = shutil.copy('config/template.yaml', path)
