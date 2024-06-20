#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation	https://github.com/cyborg-ai-git # 
#========================================================================================================================================

from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_type.entity.EvoMap import EvoMap

from evo_framework.core.evo_core_api.entity.EApiFile import EApiFile
#========================================================================================================================================
"""EOpenaiInput

	EOpenaiInput DESCRIPTION
	
"""
class EOpenaiInput(EObject):

	VERSION:str="81cec441d52e46ab42249a9924f821590307210ec5f21c8129fe5fd5bd07fff2"

	def __init__(self):
		super().__init__()
		
		self.openaiToken:str = None
		self.model:str = None
		self.eAssistantID:str = None
		self.eAssistantSessionID:str = None
		self.eAssistantRagID:str = None
		self.language:str = None
		self.text:str = None
		self.mapEApiFile:EvoMap = EvoMap()
  
	def toStream(self, stream):
		super().toStream(stream)
		
		self._doWriteStr(self.openaiToken, stream)
		self._doWriteStr(self.model, stream)
		self._doWriteStr(self.eAssistantID, stream)
		self._doWriteStr(self.eAssistantSessionID, stream)
		self._doWriteStr(self.eAssistantRagID, stream)
		self._doWriteStr(self.language, stream)
		self._doWriteStr(self.text, stream)
		self._doWriteMap(self.mapEApiFile, stream)
		
	def fromStream(self, stream):
		super().fromStream(stream)
		
		self.openaiToken = self._doReadStr(stream)
		self.model = self._doReadStr(stream)
		self.eAssistantID = self._doReadStr(stream)
		self.eAssistantSessionID = self._doReadStr(stream)
		self.eAssistantRagID = self._doReadStr(stream)
		self.language = self._doReadStr(stream)
		self.text = self._doReadStr(stream)
		self.mapEApiFile = self._doReadMap(EApiFile, stream)
	
	def __str__(self) -> str:
		strReturn = "\n".join([
				super().__str__(),
							
				f"\topenaiToken:{self.openaiToken}",
				f"\tmodel:{self.model}",
				f"\teAssistantID:{self.eAssistantID}",
				f"\teAssistantSessionID:{self.eAssistantSessionID}",
				f"\teAssistantRagID:{self.eAssistantRagID}",
				f"\tlanguage:{self.language}",
				f"\ttext:{self.text}",
				f"\tmapEApiFile:{self.mapEApiFile}",
							]) 
		return strReturn
	