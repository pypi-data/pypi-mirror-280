#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git # 
#========================================================================================================================================

from evo_framework import *
from evo_package_assistant.entity import *
import importlib.util
from pathlib import Path
# ---------------------------------------------------------------------------------------------------------------------------------------
# UAssistant
# ---------------------------------------------------------------------------------------------------------------------------------------
""" UAssistant
"""
class UAssistant:  
    __instance = None

    def __init__(self):
        if UAssistant.__instance != None:
            raise Exception("ERROR_SINGLETON")
        else:
            UAssistant.__instance = self  
            self.path_assistant:str = "/Users/max/Documents/CYBORGAI_GITHUB/CYBORGAI_GIT/cyborgai_assistant-example/output_assistant-python"  
            self.eAssistantMap:EAssistantMap = None
# -----------------------------------------------------------------------------
    @staticmethod
    def getInstance():
        if UAssistant.__instance == None:
            uObject = UAssistant()
            uObject.doInit()
            
        return UAssistant.__instance
# -----------------------------------------------------------------------------
    def doInit(self):
        try:
            self.eAssistantMap = EAssistantMap()
            self.eAssistantMap.doGenerateID()
            
            self.__doLoadDirEAssistant()
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
        
# -----------------------------------------------------------------------------   
    def doSetEAssistant(self, eAssistant:EAssistant):
        try:
           self.eAssistantMap.mapEAssistant.doSet(eAssistant)
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
        
# -----------------------------------------------------------------------------   
    async def  doGetEAssistantQuery(self, eAssistantQuery:EAssistantQuery) -> EAssistant :
        try:
            if eAssistantQuery is None:
                raise Exception("ERROR_eAssistantQuery_NONE")
            
            if eAssistantQuery.query is None:
                raise Exception("ERROR_eAssistantQuery.query_NONE")
            
            arrayQuery = eAssistantQuery.query.split("=")
            
            if len(arrayQuery) != 2 and arrayQuery[0].lower() != "id":
                raise Exception("ERROR_eAssistantQuery.query_id_NONE")
                
            eAssistantID= arrayQuery[-1]
            
            return await self.doGetEAssistant(eAssistantID)
            
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# -----------------------------------------------------------------------------   
    async def doGetEAssistant(self, id) -> EAssistant:
        try:
            if id in self.eAssistantMap.mapEAssistant.keys():
                return self.eAssistantMap.mapEAssistant.doGet(id)
            
            raise Exception(f"ERROR_NOT_FOUD_ASSISTANT_{id}")
            
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# -----------------------------------------------------------------------------   
    async def doQuery(self, eAssistantQuery:EAssistantQuery) -> EAssistantMap:
        try:
            #TODO:query
            yield self.eAssistantMap
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# -----------------------------------------------------------------------------   
    async def doDelEAssistant(self, id):
        try:
            self.eAssistantMap.mapEAssistant.doDel(id)
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
#-------------------------------------------------------------------------------
    def __doLoadDirEAssistant(self):
        try:
            IuLog.doVerbose(__name__, f"self.path_assistant {self.path_assistant}")
            
            directory = Path(self.path_assistant)
            
            arrayFileAssistant = [str(file) for file in directory.rglob('assistant_*.py')]
            print(arrayFileAssistant)
            
          
            
            for pathAssistant in arrayFileAssistant:
                print(pathAssistant)
      
                # Create a module spec from the file location
                spec = importlib.util.spec_from_file_location("assistant", pathAssistant)

                # Create a new module based on the spec
                external_file = importlib.util.module_from_spec(spec)

                # Execute the module in its own namespace
                spec.loader.exec_module(external_file)
                
                #print(pathAssistant.eAssistant)

                # Now you can use functions and variables from the external file
                #pathAssistant.addAssistant()
                

        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
         