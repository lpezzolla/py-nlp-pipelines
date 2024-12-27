from src.base.nlp_module import NLPModule

class SentimentAnalyzer(NLPModule[None, float]):
    """
    Analyze sentiment
    """
    def process(self, input_data: str, params: None) -> float:
        return 0.8