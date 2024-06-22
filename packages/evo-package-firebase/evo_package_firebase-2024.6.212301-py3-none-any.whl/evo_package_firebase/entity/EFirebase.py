#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git | 
#========================================================================================================================================

from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_type.entity.EvoMap import EvoMap

#========================================================================================================================================
"""EFirebase

    EFirebase DOC
    
"""
class EFirebase(EObject):

    VERSION:str="0941dfad8d89e3a3ffff943e7b3403d44a8bf7f4cf8f17286509806e63e37eee"

    def __init__(self):
        super().__init__()
        
        self.dataCollection:str = None
        self.dataID:str = None
        self.data:bytes = None
  
    def toStream(self, stream):
        super().toStream(stream)
        
        self._doWriteStr(self.dataCollection, stream)
        self._doWriteStr(self.dataID, stream)
        self._doWriteBytes(self.data, stream)
        
    def fromStream(self, stream):
        super().fromStream(stream)
        
        self.dataCollection = self._doReadStr(stream)
        self.dataID = self._doReadStr(stream)
        self.data = self._doReadBytes(stream)
    
    def __str__(self) -> str:
        strReturn = "\n".join([
                super().__str__(),
                            
                f"\tdataCollection:{self.dataCollection}",
                f"\tdataID:{self.dataID}",
                f"\tdata length:{len(self.data) if self.data else 'None'}",
                            ]) 
        return strReturn
    