from typing import List

from src.base.nlp_module import NLPModule

class EntityExtractor(NLPModule[None, List[str]]):
    """
    Extract entities
    """
    def process(self, input_data: str, params: None) -> List[str]:
        return ['entity1', 'entity2']