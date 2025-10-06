import datetime

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Video(Base):
    __tablename__ = "videos"
    id = Column(Integer, primary_key=True)
    youtube_video_id = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    video_metadata = Column(JSONB)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    transcripts = relationship("Transcript", back_populates="video")
    analyses = relationship("Analysis", back_populates="video")


class Transcript(Base):
    __tablename__ = "transcripts"
    id = Column(Integer, primary_key=True)
    video_id = Column(Integer, ForeignKey("videos.id"), nullable=False)
    language = Column(String, nullable=False)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    video = relationship("Video", back_populates="transcripts")


class Analysis(Base):
    __tablename__ = "analyses"
    id = Column(Integer, primary_key=True)
    video_id = Column(Integer, ForeignKey("videos.id"), nullable=False)
    prompt_id = Column(Integer, ForeignKey("ai_prompts.id"))
    analysis_result = Column(JSONB)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    video = relationship("Video", back_populates="analyses")
    prompt = relationship("AIPrompt", back_populates="analyses")


class AIPrompt(Base):
    __tablename__ = "ai_prompts"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    prompt_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    analyses = relationship("Analysis", back_populates="prompt")