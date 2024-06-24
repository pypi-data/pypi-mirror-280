from typing import Dict, List, Set

from .client import Client
from .utils import Logger

class Versions:

    @staticmethod
    def bitcoinmining_sdk():
        try:
            import importlib.metadata
            VERSION_SDK = importlib.metadata.version('bitcoinmining_sdk')
        except: VERSION_SDK = '0.0.1'
        try:
            return VERSION_SDK, int(VERSION_SDK.replace('.', ''))
        except:
            return VERSION_SDK, 0

    @staticmethod
    def tuyul_online_sdk():
        try:
            import importlib.metadata
            VERSION_SDK = importlib.metadata.version('tuyul_online_sdk')
        except: VERSION_SDK = '0.0.1'
        try:
            return VERSION_SDK, int(VERSION_SDK.replace('.', ''))
        except:
            return VERSION_SDK, 0

    @staticmethod
    def bprogrammers_sdk():
        try:
            import importlib.metadata
            VERSION_SDK = importlib.metadata.version('bprogrammers_sdk')
        except: VERSION_SDK = '0.0.1'
        try:
            return VERSION_SDK, int(VERSION_SDK.replace('.', ''))
        except:
            return VERSION_SDK, 0

    @staticmethod
    async def get_versions(BASE_URL: str, names: Set[str]):
        async with Client.ClientSession(Client.TypeReq.AIOHTTP) as session:
            async with session.post('{}/version'.format(BASE_URL), json=dict(method = 'GET')) as response:
                if response.status == 200:
                    Result: dict  = (await response.json())
                    if Result.get('status'):
                        #message: str = Result.get('message')
                        data: List[Dict[str, any]] = Result.get('data')
                        for ls in data:
                            if str(ls.get('name')).replace('-', '_').lower() == 'bitcoinmining_sdk' and 'bitcoinmining_sdk' in names:
                                version_code, version = Versions.bitcoinmining_sdk()
                                if version < ls.get('version'):
                                    if version_code != ls.get('version_code'):
                                        Logger.info(f"Update Available for BitcoinMining SDK: {ls.get('version_code')} | Your Version {version_code}")
                                        Logger.info('Please install new version SDK with command (pip install -U bitcoinmining-sdk)')
                                    else:
                                        Logger.info(f"BitcoinMining SDK is up to date: {version_code}")
                                else:
                                    Logger.info(f"BitcoinMining SDK is up to date: {version_code}")
                            elif str(ls.get('name')).replace('-', '_').lower() == 'tuyul_online_sdk' and 'tuyul_online_sdk' in names:
                                version_code, version = Versions.tuyul_online_sdk()
                                if version < ls.get('version'):
                                    if version_code != ls.get('version_code'):
                                        Logger.info(f"Update Available for Tuyul Online SDK: {ls.get('version_code')} | Your Version {version_code}")
                                        Logger.info('Please install new version SDK with command (pip install -U tuyul-online-sdk)')
                                    else:
                                        Logger.info(f"Tuyul Online SDK is up to date: {version_code}")
                                else:
                                    Logger.info(f"Tuyul Online SDK is up to date: {version_code}")
                            elif str(ls.get('name')).replace('-', '_').lower() == 'bprogrammers_sdk' and 'bprogrammers_sdk' in names:
                                version_code, version = Versions.bprogrammers_sdk()
                                if version < ls.get('version'):
                                    if version_code != ls.get('version_code'):
                                        Logger.info(f"Update Available for BProgrammers SDK: {ls.get('version_code')} | Your Version {version_code}")
                                        Logger.info('Please install new version SDK with command (pip install -U bprogrammers-sdk)')
                                    else:
                                        Logger.info(f"BProgrammers SDK is up to date: {version_code}")
                                else:
                                    Logger.info(f"BProgrammers SDK is up to date: {version_code}")
