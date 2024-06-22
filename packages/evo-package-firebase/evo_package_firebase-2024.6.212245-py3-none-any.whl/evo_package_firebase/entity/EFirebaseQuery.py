#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git | 
#========================================================================================================================================

from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_type.entity.EvoMap import EvoMap

#========================================================================================================================================
"""EFirebaseQuery

    EFirebaseQuery DOC
    
"""
class EFirebaseQuery(EObject):

    VERSION:str="b10c32985a14c338c86f116961e512c4dd0be41fbfa74c4037f01399f26e064a"

    def __init__(self):
        super().__init__()
        
        self.dataCollection:str = None
        self.dataID:str = None
        self.query:str = None
  
    def toStream(self, stream):
        super().toStream(stream)
        
        self._doWriteStr(self.dataCollection, stream)
        self._doWriteStr(self.dataID, stream)
        self._doWriteStr(self.query, stream)
        
    def fromStream(self, stream):
        super().fromStream(stream)
        
        self.dataCollection = self._doReadStr(stream)
        self.dataID = self._doReadStr(stream)
        self.query = self._doReadStr(stream)
    
    def __str__(self) -> str:
        strReturn = "\n".join([
                super().__str__(),
                            
                f"\tdataCollection:{self.dataCollection}",
                f"\tdataID:{self.dataID}",
                f"\tquery:{self.query}",
                            ]) 
        return strReturn
    