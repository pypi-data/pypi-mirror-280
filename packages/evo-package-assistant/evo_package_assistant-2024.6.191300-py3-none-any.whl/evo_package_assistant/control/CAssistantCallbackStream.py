from evo_framework import *
import re
class CAssistantCallbackStream:
    def __init__(self):
        self.isParseHeader:bool = True
        self.header:str = None
        self.prefixID:str = ""
        self.messageFull:str = ""
        self.count:int = 0
        self.messageHeader:str = None
        self.headerPattern = r'\[.*?\]'
        self.isRemoveHeader:bool = True
        self.chunkHeader:int = -1
        self.totenTot:int=0
   
    @abstractmethod
    def onParser(self, message:str) -> EApiText: 
        eApiText= self.doParser(message)
        return eApiText
    
    def isHeaderComplete(self, message) ->bool:
        if not self.isParseHeader:
                self.header="no"
                return True

        if self.header is None:
            self.messageFull = "".join([self.messageFull, message])
            match = re.search(self.headerPattern, self.messageFull)
            
            if match:
                self.header=match.group().replace("[","").replace("]", "")
                self.chunkHeader = self.count
                return True
            else:
                return False
        
        return True
    
    def doParser(self, message:str) -> EApiText: 
        eApiText = EApiText()
        eApiText.id = f"{self.prefixID}{self.count}"  
        messageChunk=message
        self.totenTot +=1
        eApiText.tokenTot = self.totenTot

        if message is None:
            eApiText.isComplete = True      
        else:
            if self.isHeaderComplete(message):
                eApiText.header = self.header
                if self.isRemoveHeader:
                    if self.count == self.chunkHeader:
                        messageChunk = message.replace(self.header, "")
                              
        eApiText.text = messageChunk
        self.count +=1
        return eApiText
    