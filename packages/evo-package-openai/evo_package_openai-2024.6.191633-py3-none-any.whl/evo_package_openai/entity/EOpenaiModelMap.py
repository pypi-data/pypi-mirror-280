#========================================================================================================================================
# CyborgAI CC BY-NC-ND 4.0 Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Internation	https://github.com/cyborg-ai-git # 
#========================================================================================================================================

from evo_framework.entity.EObject import EObject
from evo_framework.core.evo_core_type.entity.EvoMap import EvoMap

from evo_package_openai.entity.EOpenaiModel import EOpenaiModel
#========================================================================================================================================
"""EOpenaiModelMap

	EOpenaiModel DESCRIPTION
	
"""
class EOpenaiModelMap(EObject):

	VERSION:str="3e3e2f198010dd5ce9594d54a9edc9efb27c801d7baabd39dac2a6306884259d"

	def __init__(self):
		super().__init__()
		
		self.mapEModel:EvoMap = EvoMap()
  
	def toStream(self, stream):
		super().toStream(stream)
		
		self._doWriteMap(self.mapEModel, stream)
		
	def fromStream(self, stream):
		super().fromStream(stream)
		
		self.mapEModel = self._doReadMap(EOpenaiModel, stream)
	
	def __str__(self) -> str:
		strReturn = "\n".join([
				super().__str__(),
							
				f"\tmapEModel:{self.mapEModel}",
							]) 
		return strReturn
	