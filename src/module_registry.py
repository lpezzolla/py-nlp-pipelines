from src.modules.entity_extractor import EntityExtractor
from src.modules.sentiment_analyzer import SentimentAnalyzer
from src.modules.text_cleaner import TextCleaner
from src.modules.text_generator import TextGenerator

# All modules that should be available for pipeline inclusion must be registered here
# Alternatively - it would be possible to dynamically discover them
MODULE_REGISTRY = {
    "EntityExtractor": EntityExtractor,
    "SentimentAnalyzer": SentimentAnalyzer,
    "TextCleaner": TextCleaner,
    "TextGenerator": TextGenerator,
}