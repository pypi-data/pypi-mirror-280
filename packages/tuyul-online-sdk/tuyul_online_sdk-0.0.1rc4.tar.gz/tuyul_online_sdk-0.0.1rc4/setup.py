# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tuyul_online_sdk', 'tuyul_online_sdk.img']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp-proxy==0.1.2',
 'aiohttp==3.9.5',
 'base58==2.1.1',
 'bs4==0.0.2',
 'chardet==5.2.0',
 'colorama==0.4.6',
 'google-api-python-client==2.131.0',
 'hexbytes>=1.2.1,<2.0.0',
 'httpx[http2,socks]==0.27.0',
 'loguru==0.7.2',
 'lxml==5.2.2',
 'passlib>=1.7.4,<2.0.0',
 'pycryptodomex==3.20.0',
 'pydantic-core==2.18.4',
 'pydantic-settings==2.3.3',
 'pydantic==2.7.4',
 'pyjwt==2.8.0',
 'pyrogram==2.0.106',
 'python-dotenv==1.0.1',
 'requests-toolbelt==0.10.1',
 'requests==2.31.0',
 'rich==13.7.1',
 'sqlalchemy==2.0.30',
 'urllib3==1.26.15',
 'useragenter==1.3.1']

setup_kwargs = {
    'name': 'tuyul-online-sdk',
    'version': '0.0.1rc4',
    'description': '',
    'long_description': 'Install in Termux\n\npkg update\npkg upgrade\n\npkg install x11-repo && apt update\npkh install opencv rust python-crytography python-numpy python-lxml binutils-is-llvm\n\naarch64-linux-android-ar\n\npip install tuyul-online-sdk',
    'author': 'DesKaOne',
    'author_email': 'DesKaOne@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
