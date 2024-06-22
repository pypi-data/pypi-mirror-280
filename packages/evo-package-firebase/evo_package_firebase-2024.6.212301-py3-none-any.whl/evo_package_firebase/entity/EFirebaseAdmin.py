#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git | 
#========================================================================================================================================

from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_type.entity.EvoMap import EvoMap

from evo_framework.core.evo_core_api.entity.EApiAdmin import EApiAdmin
from evo_package_firebase.entity.EFirebase import EFirebase
#========================================================================================================================================
"""EFirebaseAdmin

    EFirebaseAdmin DOC
    
"""
class EFirebaseAdmin(EObject):

    VERSION:str="04cb3bf44302935a24c4d02adb6415a00d4d1027f8a30966ad410ed0e6e442af"

    def __init__(self):
        super().__init__()
        
        self.type:str = None
        self.eApiAdmin:EApiAdmin = None
        self.eFirebase:EFirebase = None
  
    def toStream(self, stream):
        super().toStream(stream)
        
        self._doWriteStr(self.type, stream)
        self._doWriteEObject(self.eApiAdmin, stream)
        self._doWriteEObject(self.eFirebase, stream)
        
    def fromStream(self, stream):
        super().fromStream(stream)
        
        self.type = self._doReadStr(stream)
        self.eApiAdmin = self._doReadEObject(EApiAdmin, stream)
        self.eFirebase = self._doReadEObject(EFirebase, stream)
    
    def __str__(self) -> str:
        strReturn = "\n".join([
                super().__str__(),
                            
                f"\ttype:{self.type}",
                f"\teApiAdmin:{self.eApiAdmin}",
                f"\teFirebase:{self.eFirebase}",
                            ]) 
        return strReturn
    