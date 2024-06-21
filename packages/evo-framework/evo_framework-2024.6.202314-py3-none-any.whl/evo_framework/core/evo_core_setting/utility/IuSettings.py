#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git |
#========================================================================================================================================
from evo_framework.core.evo_core_crypto.utility.IuCryptHash import IuCryptHash
from evo_framework.core.evo_core_crypto.utility.IuCryptChacha import IuCryptChacha
import lz4.frame
import yaml
import lz4
import base64
class IuSettings:
# ------------------------------------------------------------------------------------------------
    @staticmethod
    def doEncrypt(secret:str, mapSettings:dict) ->str:
        if secret is None:
            raise Exception("ERROR_secret_NONE")
        
        if mapSettings is None:
            raise Exception("ERROR_mapSettings_NONE")
        
        strYaml=yaml.dump(mapSettings)
        dataYaml=strYaml.encode()
        arraySecret=secret.split("~")
        dataKey =  base64.b64decode(arraySecret[0])
        dataNonce= base64.b64decode(arraySecret[1])
        dataCrypt=IuCryptChacha.doEncrypt(dataKey, dataYaml, dataNonce)
        dataCompress = lz4.frame.compress(dataCrypt)
        dataBase64 = base64.b64encode(dataCompress)
        return dataBase64.decode('utf-8')
    
# ------------------------------------------------------------------------------------------------   
    @staticmethod
    def doDecrypt(secret:str, strBase64:str) ->dict:
        if secret is None:
            raise Exception("ERROR_secret_NONE")
        
        if strBase64 is None:
            raise Exception("ERROR_strBase64_NONE")
        
        arraySecret=secret.split("~")
        dataKey =  base64.b64decode(arraySecret[0])
        ## dataNonce= base64.b64decode(arraySecret[1])
        dataCompress = base64.b64decode(strBase64)
        dataDecompress = lz4.frame.decompress(dataCompress)
        dataPlain = IuCryptChacha.doDecryptCombined(dataKey, dataDecompress)
        strPlain= dataPlain.decode()
        print(strPlain)

        return yaml.safe_load(strPlain)
# ------------------------------------------------------------------------------------------------