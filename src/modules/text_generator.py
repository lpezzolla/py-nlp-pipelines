from pydantic import BaseModel

from src.base.nlp_module import NLPModule

class TextGeneratorParams(BaseModel):
    max_length: int

class TextGenerator(NLPModule[TextGeneratorParams, str]):
    """
    Generate text
    """
    def process(self, input_data: str, params: TextGeneratorParams) -> str:
        return f"Generated text based on: {input_data}"