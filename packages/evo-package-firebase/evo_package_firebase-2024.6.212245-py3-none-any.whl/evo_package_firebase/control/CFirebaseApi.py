#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation	https://github.com/cyborg-ai-git | 
#========================================================================================================================================

from evo_framework import *
from evo_package_firebase.entity import *
from evo_package_firebase.utility import *
# ---------------------------------------------------------------------------------------------------------------------------------------
# CFirebaseApi
# ---------------------------------------------------------------------------------------------------------------------------------------
"""CFirebaseApi
"""
class CFirebaseApi(CApi):
	__instance = None
# ---------------------------------------------------------------------------------------------------------------------------------------
	def __init__(self):   
		if CFirebaseApi.__instance != None:
			raise Exception("ERROR:SINGLETON")
		else:
			super().__init__()
			CFirebaseApi.__instance = self
			self.currentPath = os.path.dirname(os.path.abspath(__file__))
			
# ---------------------------------------------------------------------------------------------------------------------------------------
	"""getInstance Singleton

	Raises:
		Exception:  api exception

	Returns:
		_type_: CFirebaseApi instance
	"""
	@staticmethod
	def getInstance():
		if CFirebaseApi.__instance is None:
			cObject = CFirebaseApi()  
			cObject.doInit()  
		return CFirebaseApi.__instance
# ---------------------------------------------------------------------------------------------------------------------------------------
	"""doInit

	Raises:
		Exception: api exception

	Returns:

	"""   
	def doInit(self):   
		pass	  
# ---------------------------------------------------------------------------------------------------------------------------------------
	"""doAddApi

	Raises:
		Exception: api exception

	Returns:

	"""
	@override   
	def doAddApi(self):
		try:			
			
			api0 = self.newApi("firebase-set", callback=self.onSet, input=EFirebaseAdmin, output=EFirebase, isEnabled=True )
			api0.description="firebase-set description"

			api1 = self.newApi("firebase-get", callback=self.onGet, input=EFirebaseQuery, output=EFirebase, isEnabled=True )
			api1.description="firebase-get description"

			api2 = self.newApi("firebase-del", callback=self.onDel, input=EFirebaseAdmin, output=EFirebase, isEnabled=True )
			api2.description="firebase-del description"

			api3 = self.newApi("firebase-del_all", callback=self.onDelAll, input=EFirebaseAdmin, output=EFirebase, isEnabled=True )
			api3.description="firebase-del_all description"

			api4 = self.newApi("firebase-query", callback=self.onQuery, input=EFirebaseQuery, output=EFirebaseMap, isEnabled=True )
			api4.description="firebase-query description"
  
		except Exception as exception:
			IuLog.doException(__name__, exception)
			raise
# ---------------------------------------------------------------------------------------------------------------------------------------

	"""onSet api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onSet(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onSet: {eAction} ")
				
			eFirebaseAdminIn:EFirebaseAdmin = eAction.doGetInput(EFirebaseAdmin)
			
			#Remove eAction input for free memory
			eAction.input = None
#<
					 
			eFirebaseOut = await UFirebaseApi.getInstance().doOnSet(eFirebaseAdminIn)
			eAction.doSetOutput(eFirebaseOut)
			yield eAction
			
			'''
			#IF NEED STREAM 
			async for eFirebase in UFirebaseApi.getInstance().doOnSet(eFirebaseAdmin):
				eAction.doSetOutput(eFirebase)
				yield eAction	
			'''	
#>

		except Exception as exception:
			IuLog.doException(__name__, exception)
			eAction.doSetError(f"{exception}")
			yield eAction
# ---------------------------------------------------------------------------------------------------------------------------------------

	"""onGet api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onGet(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onGet: {eAction} ")
				
			eFirebaseQuery:EFirebaseQuery = eAction.doGetInput(EFirebaseQuery)
			
			#Remove eAction input for free memory
			eAction.input = None
#<
					 
			eFirebase = await UFirebaseApi.getInstance().doOnGet(eFirebaseQuery)
			eAction.doSetOutput(eFirebase)
			yield eAction
			
			'''
			#IF NEED STREAM 
			async for eFirebase in UFirebaseApi.getInstance().doOnGet(eFirebaseQuery):
				eAction.doSetOutput(eFirebase)
				yield eAction	
			'''	
#>

		except Exception as exception:
			IuLog.doException(__name__, exception)
			eAction.doSetError(f"{exception}")
			yield eAction
# ---------------------------------------------------------------------------------------------------------------------------------------

	"""onDel api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onDel(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onDel: {eAction} ")
				
			eFirebaseAdmin:EFirebaseAdmin = eAction.doGetInput(EFirebaseAdmin)
			
			#Remove eAction input for free memory
			eAction.input = None
#<
					 
			eFirebase = await UFirebaseApi.getInstance().doOnDel(eFirebaseAdmin)
			eAction.doSetOutput(eFirebase)
			yield eAction
			
			'''
			#IF NEED STREAM 
			async for eFirebase in UFirebaseApi.getInstance().doOnDel(eFirebaseAdmin):
				eAction.doSetOutput(eFirebase)
				yield eAction	
			'''	
#>

		except Exception as exception:
			IuLog.doException(__name__, exception)
			eAction.doSetError(f"{exception}")
			yield eAction
# ---------------------------------------------------------------------------------------------------------------------------------------

	"""onDelAll api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onDelAll(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onDelAll: {eAction} ")
				
			eFirebaseAdmin:EFirebaseAdmin = eAction.doGetInput(EFirebaseAdmin)
			
			#Remove eAction input for free memory
			eAction.input = None
#<
					 
			eFirebase = await UFirebaseApi.getInstance().doOnDelAll(eFirebaseAdmin)
			eAction.doSetOutput(eFirebase)
			yield eAction
			
			'''
			#IF NEED STREAM 
			async for eFirebase in UFirebaseApi.getInstance().doOnDelAll(eFirebaseAdmin):
				eAction.doSetOutput(eFirebase)
				yield eAction	
			'''	
#>

		except Exception as exception:
			IuLog.doException(__name__, exception)
			eAction.doSetError(f"{exception}")
			yield eAction
# ---------------------------------------------------------------------------------------------------------------------------------------

	"""onQuery api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onQuery(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onQuery: {eAction} ")
				
			eFirebaseQuery:EFirebaseQuery = eAction.doGetInput(EFirebaseQuery)
			
			#Remove eAction input for free memory
			eAction.input = None
#<
					 
			eFirebaseMap = await UFirebaseApi.getInstance().doOnQuery(eFirebaseQuery)
			eAction.doSetOutput(eFirebaseMap)
			yield eAction
			
			'''
			#IF NEED STREAM 
			async for eFirebaseMap in UFirebaseApi.getInstance().doOnQuery(eFirebaseQuery):
				eAction.doSetOutput(eFirebaseMap)
				yield eAction	
			'''	
#>

		except Exception as exception:
			IuLog.doException(__name__, exception)
			eAction.doSetError(f"{exception}")
			yield eAction
# ---------------------------------------------------------------------------------------------------------------------------------------
