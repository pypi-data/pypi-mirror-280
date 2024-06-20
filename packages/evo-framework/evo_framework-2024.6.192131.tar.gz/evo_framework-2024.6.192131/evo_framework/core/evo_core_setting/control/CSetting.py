import base64
import json
import os
import lz4.frame
from evo_framework.core.evo_core_setting.entity.ESetting import ESetting
from evo_framework.core.evo_core_log.utility.IuLog import IuLog
from evo_framework.core.evo_core_system.utility.IuSystem import IuSystem
from evo_framework.core.evo_core_setting.utility.IuSettings import IuSettings
from urllib.parse import unquote
current_path = os.path.dirname(os.path.abspath(__file__))
class CSetting:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if CSetting.__instance == None:
            cObject = CSetting()
            cObject.doInit()
        return CSetting.__instance

    def __init__(self):
        if CSetting.__instance != None:
            raise Exception("ERROR:SINGLETON")
        else:
            CSetting.__instance = self
            self.mapSetting = {}
             
    def doInit(self):
        try:
            self.eSettings = ESetting()
            try:
               self.eSettings.path_output =  IuSystem.do_sanitize_path( f"{current_path}/../../../../assets/")
            except Exception as exception:
                IuLog.doException(__name__,exception)
            
            passwordEnv =os.environ.get('CYBORGAI_PASSWORD')
            if passwordEnv is None:
                raise Exception("ERROR_CYBORGAI_PASSWORD_NONE")
            
            if len(passwordEnv) <16:
                raise Exception(f"ERROR_CYBORGAI_PASSWORD_LENGTH<16")
            
            settingsEnv =os.environ.get('CYBORGAI_SETTINGS')
            
            if(settingsEnv is None or settingsEnv==""):
                IuLog.doError(__name__,"ERROR_CYBORGAI_SETTINGS_environment_EMPTY copy in .env first start")
            else:
                secrectEnv =os.environ.get('CYBORGAI_SECRET')
                
                if secrectEnv is None:
                    raise Exception("ERROR_CYBORGAI_SECRET_NONE")
                
                mapSettingsTmp =  IuSettings.doDecrypt(secrectEnv, settingsEnv)
                
                if mapSettingsTmp is None:
                    raise Exception("ERROR_DECRYPT_CYBORGAI_SETTINGS")
                
                self.mapSetting = mapSettingsTmp
                
        except Exception as exception:
            #IuLog.doError(__name__,f"{exception}")
            IuLog.doException(__name__,exception)
            raise exception
    
    def doGet(self, key:str):
        try:
            return self.mapSetting.get(key)
        except Exception as exception:
            IuLog.doError(__name__,f"{exception}")
            return None
            
            
        
        
