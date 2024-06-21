
#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation	https://github.com/cyborg-ai-git # 
#========================================================================================================================================

from evo_framework import *
from evo_package_openai.entity import *
from evo_package_openai.utility import *
# ---------------------------------------------------------------------------------------------------------------------------------------
# COpenaiApi
# ---------------------------------------------------------------------------------------------------------------------------------------
"""COpenaiApi
"""
class COpenaiApi(CApi):
	__instance = None
# ---------------------------------------------------------------------------------------------------------------------------------------
	def __init__(self):   
		if COpenaiApi.__instance != None:
			raise Exception("ERROR:SINGLETON")
		else:
			super().__init__()
			COpenaiApi.__instance = self
			self.current_path = os.path.dirname(os.path.abspath(__file__))
			self.path_assets:str = f"{self.current_path}/../../../../assets"		
#<
			self.callbackParser = None
			self.callback = None
			self.arrayMessage:[] = None
			self.arrayTools:[] = None
			self.arrayToolsChoice:[] = None
#>
# ---------------------------------------------------------------------------------------------------------------------------------------
	"""getInstance Singleton

	Raises:
		Exception:  api exception

	Returns:
		_type_: COpenaiApi instance
	"""
	@staticmethod
	def getInstance():
		if COpenaiApi.__instance is None:
			cObject = COpenaiApi()  
			cObject.doInit()  
		return COpenaiApi.__instance
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
			
			api0 = self.newApi("openai-chatstream", callback=self.onChatStream, input=EOpenaiInput, output=EOpenaiOutput, isEnabled=True )
			api0.isStream=True 
			api0.description="openai-chatsream DESCRIPTION"

			api1 = self.newApi("openai-chat", callback=self.onChat, input=EOpenaiInput, output=EOpenaiOutput, isEnabled=True )
			api1.isStream=False 
			api1.description="openai-chat DESCRIPTION"

			api2 = self.newApi("openai-get_model", callback=self.onGetModel, input=EOpenaiInput, output=EOpenaiModelMap, isEnabled=True )
			api2.isStream=False 
			api2.description="openai-get_model DESCRIPTION"

			api3 = self.newApi("openai-get_session", callback=self.onGetSession, input=EOpenaiInput, output=EOpenaiModelMap, isEnabled=True )
			api3.isStream=False 
			api3.description="openai-get_session DESCRIPTION"

			api4 = self.newApi("openai-get_assistant", callback=self.onGetSession, input=EOpenaiInput, output=EOpenaiModelMap, isEnabled=True )
			api4.isStream=False 
			api4.description="openai-get_assistant DESCRIPTION"

			api5 = self.newApi("openai-finetune", callback=self.onGetSession, input=EOpenaiInput, output=EOpenaiModelMap, isEnabled=True )
			api5.isStream=False 
			api5.description="openai-finetune DESCRIPTION"

			api6 = self.newApi("openai-rag", callback=self.onGetSession, input=EOpenaiInput, output=EOpenaiModelMap, isEnabled=True )
			api6.isStream=False 
			api6.description="openai-rag DESCRIPTION"
  
		except Exception as exception:
			IuLog.doException(__name__, exception)
			raise
# ---------------------------------------------------------------------------------------------------------------------------------------

	"""onChatStream api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onChatStream(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onChatStream: {eAction} ")
				
			eOpenaiInput:EOpenaiInput = eAction.doGetInput(EOpenaiInput)
			
			#Remove eAction input for free memory
			eAction.input = None
#<
			async for eOpenaiOutput in UOpenai.getInstance().doChatStream(eOpenaiInput):
				if eOpenaiOutput.eApiText.isComplete:
					eAction.enumApiAction = EnumApiAction.COMPLETE
				eAction.doSetOutput(eOpenaiOutput)
				yield eAction
#>
		except Exception as exception:
			IuLog.doException(__name__, exception)
			eAction.doSetError(f"{exception}")
			yield eAction
# ---------------------------------------------------------------------------------------------------------------------------------------
	"""onChat api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onChat(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onChat: {eAction} ")
				
			eOpenaiInput:EOpenaiInput = eAction.doGetInput(EOpenaiInput)
			
			#Remove eAction input for free memory
			eAction.input = None
			#<
			
			#await UOpenai.getInstance().doOpenai()
			eOpenaiModelMap = await UOpenai.getInstance().doGetModel()

			eAction.doSetOutput(eOpenaiModelMap)
   
			return eAction
		
			#>

		except Exception as exception:
			IuLog.doException(__name__, exception)
			raise
# ---------------------------------------------------------------------------------------------------------------------------------------

	"""onGetModel api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onGetModel(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onGetModel: {eAction} ")
				
			eOpenaiInput:EOpenaiInput = eAction.doGetInput(EOpenaiInput)
			
			#Remove eAction input for free memory
			eAction.input = None
#<   
			eOpenaiModelMap = await UOpenai.getInstance().doGetModel()
			eAction.doSetOutput(eOpenaiModelMap)
			return eAction
#>

		except Exception as exception:
			IuLog.doException(__name__, exception)
			raise
# ---------------------------------------------------------------------------------------------------------------------------------------
	"""onGetSession api callback

	Raises:
		Exception: api exception

	Returns:
		EAction:  EObject 
	"""   
	async def onGetSession(self,  eAction: EAction) -> EAction:
		try:
			IuLog.doDebug(__name__,f"onGetSession: {eAction} ")
				
			eOpenaiInput:EOpenaiInput = eAction.doGetInput(EOpenaiInput)
			
			#Remove eAction input for free memory
			eAction.input = None
#<
			#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			#@TODO: INSERT YOUR CODE 

			eOpenaiModelMap = EOpenaiModelMap()
			eOpenaiModelMap.doGenerateID()
			eOpenaiModelMap.doGenerateTime()

			eAction.doSetOutput(eOpenaiModelMap)
			return eAction
			#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#>

		except Exception as exception:
			IuLog.doException(__name__, exception)
			raise
# ---------------------------------------------------------------------------------------------------------------------------------------