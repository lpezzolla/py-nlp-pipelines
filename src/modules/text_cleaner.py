from src.base.nlp_module import NLPModule

class TextCleaner(NLPModule[None, str]):
    """
    Remove special characters
    """
    def process(self, input_data: str, params: None) -> str:
        return input_data.strip()