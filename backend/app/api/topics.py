"""
OreSight Topic Explorer & Word Cloud APIs (BERTopic)
"""

from fastapi import APIRouter
from backend.app.ai.topic_model import topic_engine

router = APIRouter(prefix="/topics", tags=["Topics & Word Cloud"])

@router.get("")
def get_topics():
    return topic_engine.get_all_topics()

@router.get("/wordcloud")
def get_wordcloud():
    return topic_engine.get_word_cloud()

@router.get("/{topic_id}")
def get_topic_detail(topic_id: int):
    return topic_engine.get_topic_by_id(topic_id)
