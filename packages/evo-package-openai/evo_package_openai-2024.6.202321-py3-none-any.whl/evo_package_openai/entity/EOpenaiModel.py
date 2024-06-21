#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation	https://github.com/cyborg-ai-git # 
#========================================================================================================================================

from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_type.entity.EvoMap import EvoMap

#========================================================================================================================================
"""EOpenaiModel

	EOpenaiModel DESCRIPTION
	
"""
class EOpenaiModel(EObject):

	VERSION:str="8e2c14b57f175e0dcc75eb32e7a8df0544f2cbaf90594ecb774f02622a27de8d"

	def __init__(self):
		super().__init__()
		
		self.name:str = None
		self.created:int = None
  
	def toStream(self, stream):
		super().toStream(stream)
		
		self._doWriteStr(self.name, stream)
		self._doWriteInt(self.created, stream)
		
	def fromStream(self, stream):
		super().fromStream(stream)
		
		self.name = self._doReadStr(stream)
		self.created = self._doReadInt(stream)
	
	def __str__(self) -> str:
		strReturn = "\n".join([
				super().__str__(),
							
				f"\tname:{self.name}",
				f"\tcreated:{self.created}",
							]) 
		return strReturn
	