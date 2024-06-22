#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation    https://github.com/cyborg-ai-git | 
#========================================================================================================================================

from evo_framework import *
from evo_package_firebase.entity import *
#<
import firebase_admin
from firebase_admin import credentials, firestore, storage
from typing import List
import lz4

#>
# ---------------------------------------------------------------------------------------------------------------------------------------
# UFirebaseApi
# ---------------------------------------------------------------------------------------------------------------------------------------
"""UFirebaseApi
"""
class UFirebaseApi():
    __instance = None
# ---------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):   
        if UFirebaseApi.__instance != None:
            raise Exception("ERROR:SINGLETON")
        else:
            super().__init__()
            UFirebaseApi.__instance = self
            self.currentPath = os.path.dirname(os.path.abspath(__file__))
            self.database = None
            self.storage = None
            
# ---------------------------------------------------------------------------------------------------------------------------------------
    """getInstance Singleton

    Raises:
        Exception:  api exception

    Returns:
        _type_: UFirebaseApi instance
    """
    @staticmethod
    def getInstance():
        if UFirebaseApi.__instance is None:
            uObject = UFirebaseApi()  
            uObject.doInit()  
        return UFirebaseApi.__instance
# ---------------------------------------------------------------------------------------------------------------------------------------
    """doInit

    Raises:
        Exception: api exception

    Returns:

    """   
    def doInit(self):  
        try:
#<
            ACCESS_TOKEN_FIREBASE=CSetting.getInstance().doGet("ACCESS_TOKEN_FIREBASE")
            #print("\n\n",ACCESS_TOKEN_FIREBASE)
            mapFirebase=json.loads(ACCESS_TOKEN_FIREBASE)
            #print("\n\nmapFirebase\n",mapFirebase)
            cred = credentials.Certificate(mapFirebase)
            
            projectID = mapFirebase["project_id"]
            firebase_admin.initialize_app(cred, {
                'storageBucket': f'{projectID}.appspot.com'
            })
            self.database = firestore.client()
            self.storage = storage.bucket()
#>   
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnSet(self, eFirebaseAdminIn:EFirebaseAdmin) -> EFirebase :
        try:
            if eFirebaseAdminIn is None:
                raise Exception("ERROR_eFirebaseAdmin_REQUIRED")
 #<           
 
            #TODO:check eApiAdmin
            #IuApi.doCheckEApiAdmin(eFirebaseAdminIn.eApiAdmin)
 
            if eFirebaseAdminIn.eFirebase is None:
                raise Exception("ERROR_eFirebaseAdmin.eFirebase_REQUIRED")
            
            if eFirebaseAdminIn.eFirebase.dataCollection is None:
                raise Exception("ERROR_eFirebaseAdmin.eFirebase.dataCollection_REQUIRED")
            
            if eFirebaseAdminIn.eFirebase.dataID is None:
                raise Exception("ERROR_eFirebaseAdmin.eFirebase.dataID_REQUIRED")
            
            if eFirebaseAdminIn.eFirebase.data is None:
                raise Exception("ERROR_eFirebaseAdmin.eFirebase.data_REQUIRED")
            
            await self.doSet(eFirebaseAdminIn.eFirebase.dataCollection, eFirebaseAdminIn.eFirebase.dataID, eFirebaseAdminIn.eFirebase.data)
            
            eFirebaseOutput = EFirebase()
            eFirebaseOutput.doGenerateID()
            
            return eFirebaseOutput
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnGet(self, eFirebaseQueryIn:EFirebaseQuery) -> EFirebase :
        try:
            if eFirebaseQueryIn is None:
                raise Exception("ERROR_eFirebaseQuery_REQUIRED")
            
#<     
            if eFirebaseQueryIn.dataCollection is None:
                raise Exception("ERROR_eFirebase.dataCollection_REQUIRED")
            
            if eFirebaseQueryIn.dataID is None:
                raise Exception("ERROR_eFirebase.dataID_REQUIRED")           
#>
            data = await self.doGet(eFirebaseQueryIn.dataCollection, eFirebaseQueryIn.dataID)
            
            if data is None:
                raise Exception(f"ERROR_GET_{eFirebaseQueryIn.dataCollection}_{eFirebaseQueryIn.dataID}")
            
            eFirebaseOut = EFirebase()
            eFirebaseOut.id = eFirebaseQueryIn.id
            eFirebaseOut.dataCollection = eFirebaseQueryIn.dataCollection
            eFirebaseOut.dataID = eFirebaseQueryIn.dataID
            eFirebaseOut.data = data
            
            return eFirebaseOut
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnDel(self, eFirebaseAdminIn:EFirebaseAdmin) -> EFirebase :
        try:
            if eFirebaseAdminIn is None:
                raise Exception("ERROR_eFirebaseAdmin_REQUIRED")
#<             
            
            #TODO:check eApiAdmin
            #IuApi.doCheckEApiAdmin(eFirebaseAdminIn.eApiAdmin)
 
            if eFirebaseAdminIn.eFirebase is None:
                raise Exception("ERROR_eFirebaseAdmin.eFirebase_REQUIRED")
            
            if eFirebaseAdminIn.eFirebase.dataCollection is None:
                raise Exception("ERROR_eFirebaseAdmin.eFirebase.dataCollection_REQUIRED")
            
            if eFirebaseAdminIn.eFirebase.dataID is None:
                raise Exception("ERROR_eFirebaseAdmin.eFirebase.dataID_REQUIRED")   
    
            await self.doDel(eFirebaseAdminIn.eFirebase.dataCollection, eFirebaseAdminIn.eFirebase.dataID)
            
            eFirebaseOutput = EFirebase()
            eFirebaseOutput.doGenerateID()
            return eFirebaseOutput
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnDelAll(self, eFirebaseAdminIn:EFirebaseAdmin) -> EFirebase :
        try:
            if eFirebaseAdminIn is None:
                raise Exception("ERROR_eFirebaseAdmin_REQUIRED")
#<             
            
            #TODO:check eApiAdmin
            #IuApi.doCheckEApiAdmin(eFirebaseAdminIn.eApiAdmin)
 
            if eFirebaseAdminIn.eFirebase is None:
                raise Exception("ERROR_eFirebaseAdmin.eFirebase_REQUIRED")
            
            if eFirebaseAdminIn.eFirebase.dataCollection is None:
                raise Exception("ERROR_eFirebaseAdmin.eFirebase.dataCollection_REQUIRED")
            
            
            await self.doDelAll(eFirebaseAdminIn.eFirebase.dataCollection)
            
            eFirebaseOutput = EFirebase()
            eFirebaseOutput.doGenerateID()
            return eFirebaseOutput
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doOnQuery(self, eFirebaseQuery:EFirebaseQuery) -> EFirebaseMap :
        try:
            if eFirebaseQuery is None:
                raise Exception("ERROR_eFirebaseQuery_REQUIRED")
            
            #Add other check
            '''
            if eFirebaseQuery. is None:
                raise Exception("ERROR_eFirebaseQuery._REQUIRED")
            '''
#<     
            eFirebaseMap = EFirebaseMap()
            eFirebaseMap.doGenerateID()
            
            
            return eFirebaseMap
#>
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise

#<
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doSet(self, collection:str, iD: str, data:bytes):
        try:
            timeCurrent = IuKey.generateTime()
            hashData= IuCryptHash.toSha256(data)
            
            dataCrypt = IuSettings.doEncrypt(data)
            blob = self.storage.blob(iD)
            
            if await asyncio.to_thread(blob.exists):
                IuLog.doWarning(__name__,f"WARNING_update_{collection}_{iD}_doDel")
                #raise Exception(f"ERROR_{collection}_{iD}_doDel")
                await self.doDel(collection, iD)

            await asyncio.to_thread(blob.upload_from_string, dataCrypt)

           # await asyncio.to_thread(blob.make_public)
            
            cyborgaiID = CSetting.getInstance().doGet("CYBORGAI_ID")

            url=blob.public_url
            
            if url is None:
                 raise Exception(f"ERROR_GET_{collection}_{iD}")
        
            mapInfo = {
                'id':iD,
                'time':timeCurrent,
                'hash':hashData,
               # 'url':url,
                'cyborgaiID':cyborgaiID
            }
            
            doc_ref = self.database.collection(collection).document(iD)
            doc_ref.set(mapInfo)
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise

# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doGet(self, collection:str, id: str ) -> bytes:
        try:
            doc_ref = self.database.collection(collection).document(id)
            doc = doc_ref.get()
            if not doc.exists:
                raise Exception(f"ERROR_GET_{collection}_{id}")
            
            mapInfo = doc.to_dict()
            
            IuLog.doWarning(__name__, f"mapInfo:\n{mapInfo}")
            
            if mapInfo is None:
                raise Exception(f"ERROR_GET_MAPINFO_{collection}_{id}")
                   
            blob = self.storage.blob(mapInfo["id"])
            
            dataEncrypt = await asyncio.to_thread(blob.download_as_bytes)
            
            if dataEncrypt is None:
                raise Exception(f"ERROR_dataEncrypt_{collection}_{id}")
            
            data = IuSettings.doDecrypt(dataEncrypt)
            
            if data is None:
                raise Exception(f"ERROR_data_{collection}_{id}")
            
            return data
    
            '''
            async with aiofiles.open(download_path, 'wb') as f:
                await asyncio.to_thread(blob.download_to_file, f)
            '''
            
            
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
        

# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doDel(self, collection:str, id: str ):
        try:
            doc_ref = self.database.collection(collection).document(id)
            await asyncio.to_thread(doc_ref.delete)
            blob = self.storage.blob(id)
            await asyncio.to_thread(blob.delete)
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
        
# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doDelAll(self, collection:str):
        try:
            
            docs_ref = self.database.collection(collection)
            arrayDoc = await asyncio.to_thread(docs_ref.stream)
            
            arrayMapInfo = []
            for doc in arrayDoc:
                arrayMapInfo.append(doc.to_dict())
     
            for mapInfo in arrayMapInfo:
                print(mapInfo)
                await self.doDel(collection, mapInfo["id"] )
    
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
       

# ---------------------------------------------------------------------------------------------------------------------------------------
    async def doQuery(self, query: List, collection:str) -> List[dict]:
        try:
            result = []
            for q in query:
                docs = self.database.collection(collection).where(*q).get()
                for doc in docs:
                    result.append(doc.to_dict())
            return result
        except Exception as exception:
            IuLog.doException(__name__,exception)
            raise
# ---------------------------------------------------------------------------------------------------------------------------------------

    '''
    def doCreateDynamicLink():
        {
        "longDynamicLink": "https://example.page.link/?link=https://www.example.com/&apn=com.example.android&ibi=com.example.ios"
        }
        api_key = 'your_api_key'
        domain = 'example.page.link'
        timeout = 10
        dl = DynamicLinks(api_key, domain, timeout) # or DynamicLinks(api_key, domain)
        params = {
            "androidInfo": {
                "androidPackageName": 'packagename',
                "androidFallbackLink": 'fallbacklink',
                "androidMinPackageVersionCode": '1'
            },
        }
        # dl.generate_dynamic_link(url_to_redirect, create_short_url, params) or
        # dl.generate_dynamic_link(url_to_redirect)
        short_link = dl.generate_dynamic_link('http://google.es', True, params)
        return short_link
    '''
#>
# ---------------------------------------------------------------------------------------------------------------------------------------
