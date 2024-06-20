#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation	https://github.com/cyborg-ai-git # 
#========================================================================================================================================

from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_type.entity.EvoMap import EvoMap

from evo_framework.core.evo_core_api.entity.EApiText import EApiText
#========================================================================================================================================
"""EOpenaiOutput

	EOpenaiInput DESCRIPTION
	
"""
class EOpenaiOutput(EObject):

	VERSION:str="8e1e9dfae6bffeda3e0eb68449c116c2329fc75a50358f175047e90707de75ca"

	def __init__(self):
		super().__init__()
		
		self.eAssistantSessionID:str = None
		self.eApiText:EApiText = None
		self.isError:bool = None
		self.error:str = None
  
	def toStream(self, stream):
		super().toStream(stream)
		
		self._doWriteStr(self.eAssistantSessionID, stream)
		self._doWriteEObject(self.eApiText, stream)
		self._doWriteBool(self.isError, stream)
		self._doWriteStr(self.error, stream)
		
	def fromStream(self, stream):
		super().fromStream(stream)
		
		self.eAssistantSessionID = self._doReadStr(stream)
		self.eApiText = self._doReadEObject(EApiText, stream)
		self.isError = self._doReadBool(stream)
		self.error = self._doReadStr(stream)
	
	def __str__(self) -> str:
		strReturn = "\n".join([
				super().__str__(),
							
				f"\teAssistantSessionID:{self.eAssistantSessionID}",
				f"\teApiText:{self.eApiText}",
				f"\tisError:{self.isError}",
				f"\terror:{self.error}",
							]) 
		return strReturn
	