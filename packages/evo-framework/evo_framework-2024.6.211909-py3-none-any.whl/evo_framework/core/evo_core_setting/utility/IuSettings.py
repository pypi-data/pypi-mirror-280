#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git |
#========================================================================================================================================
from evo_framework.core.evo_core_crypto.utility.IuCryptHash import IuCryptHash
from evo_framework.core.evo_core_crypto.utility.IuCryptChacha import IuCryptChacha
import lz4.frame
import yaml
import lz4
import base64
import os
class IuSettings:
# ------------------------------------------------------------------------------------------------
    @staticmethod
    def doEncryptSettings(mapSettings:dict) ->str:
        secretEnv =os.environ.get('CYBORGAI_SECRET')
        if secretEnv is None:
            raise Exception("ERROR_CYBORGAI_SECRET_REQUIRED")
        
        if mapSettings is None:
            raise Exception("ERROR_mapSettings_REQUIRED")
        
        strYaml=yaml.dump(mapSettings)
        dataYaml=strYaml.encode()
        arraySecret=secretEnv.split("~")
        dataKey =  base64.b64decode(arraySecret[0])
        dataNonce= base64.b64decode(arraySecret[1])
        dataCrypt=IuCryptChacha.doEncrypt(dataKey, dataYaml, dataNonce)
        dataCompress = lz4.frame.compress(dataCrypt)
        dataBase64 = base64.b64encode(dataCompress)
        return dataBase64.decode('utf-8')
    
# ------------------------------------------------------------------------------------------------   
    @staticmethod
    def doDecryptSettings(strBase64:str) ->dict:
        secretEnv =os.environ.get('CYBORGAI_SECRET')
        if secretEnv is None:
            raise Exception("ERROR_CYBORGAI_SECRET_REQUIRED")

        if strBase64 is None:
            raise Exception("ERROR_strBase64_NONE")
        
        arraySecret=secretEnv.split("~")
        dataKey =  base64.b64decode(arraySecret[0])
        ## dataNonce= base64.b64decode(arraySecret[1])
        dataCompress = base64.b64decode(strBase64)
        dataDecompress = lz4.frame.decompress(dataCompress)
        dataPlain = IuCryptChacha.doDecryptCombined(dataKey, dataDecompress)
        strPlain= dataPlain.decode()
        
        return yaml.safe_load(strPlain)
# ------------------------------------------------------------------------------------------------
    @staticmethod
    def doEncrypt(data:bytes) ->bytes:
        secretEnv =os.environ.get('CYBORGAI_SECRET')
        if secretEnv is None:
            raise Exception("ERROR_CYBORGAI_SECRET_REQUIRED")
        
        arraySecret=secretEnv.split("~")
        dataKey =  base64.b64decode(arraySecret[0])
        dataNonce= base64.b64decode(arraySecret[1])
        dataCrypt=IuCryptChacha.doEncrypt(dataKey, data, dataNonce)
        dataCompress = lz4.frame.compress(dataCrypt)
       
        return dataCompress
    
# ------------------------------------------------------------------------------------------------   
    @staticmethod
    def doDecrypt(data:bytes) -> bytes:
        secretEnv =os.environ.get('CYBORGAI_SECRET')
        if secretEnv is None:
            raise Exception("ERROR_CYBORGAI_SECRET_REQUIRED")
        
        arraySecret=secretEnv.split("~")
        dataKey =  base64.b64decode(arraySecret[0])
        dataCompress = data
        dataDecompress = lz4.frame.decompress(dataCompress)
        dataPlain = IuCryptChacha.doDecryptCombined(dataKey, dataDecompress)
        return dataPlain
# ------------------------------------------------------------------------------------------------