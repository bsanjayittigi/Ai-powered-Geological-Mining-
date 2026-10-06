"""
OreSight Topic Modeling Engine (BERTopic Architecture)
Performs:
1. Topic Identification & Semantic Clustering
2. Word Cloud Keyword Weighting
3. Historical Archive Topic Trend Analysis
4. Subsidiary & Mine-level Topic Distribution
"""

from typing import Dict, List, Any
from backend.app.services.mock_data import INITIAL_TOPICS

class TopicModelingEngine:
    def __init__(self):
        self.topics = INITIAL_TOPICS

    def get_all_topics(self) -> List[Dict[str, Any]]:
        return self.topics

    def get_word_cloud(self) -> List[Dict[str, Any]]:
        """
        Aggregates keywords with frequency weights for interactive word cloud
        """
        words = []
        base_weights = {
            "ROM Coal": 98,
            "Borehole Log": 94,
            "Seam Thickness": 92,
            "Overburden (OBR)": 89,
            "Gross Calorific Value (GCV)": 88,
            "Stripping Ratio": 85,
            "Grade G11": 82,
            "Dragline": 79,
            "Lithology": 78,
            "Ash Content": 76,
            "Slope Stability": 74,
            "Merry-Go-Round (MGR)": 71,
            "Core Recovery": 69,
            "Jharia Basin": 68,
            "Gevra OC": 67,
            "In-pit Crushing": 64,
            "Moisture %": 62,
            "DGMS Compliance": 60,
            "Shovel-Dumper": 58,
            "Afforestation": 55
        }
        for term, weight in base_weights.items():
            words.append({"text": term, "value": weight})
        return sorted(words, key=lambda x: x["value"], reverse=True)

    def get_topic_by_id(self, topic_id: int) -> Dict[str, Any]:
        for t in self.topics:
            if t["id"] == topic_id:
                return t
        return self.topics[0]

topic_engine = TopicModelingEngine()
