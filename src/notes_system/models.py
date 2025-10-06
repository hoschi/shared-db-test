import datetime

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    Table,
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

note_tags = Table(
    "note_tags",
    Base.metadata,
    Column("note_id", Integer, ForeignKey("notes.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content_markdown = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    tags = relationship("Tag", secondary=note_tags, back_populates="notes")
    attachments = relationship("Attachment", back_populates="note")
    versions = relationship("NoteVersion", back_populates="note")


class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    color = Column(String)

    notes = relationship("Note", secondary=note_tags, back_populates="tags")


class Attachment(Base):
    __tablename__ = "attachments"
    id = Column(Integer, primary_key=True)
    note_id = Column(Integer, ForeignKey("notes.id"), nullable=False)
    filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    mime_type = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    note = relationship("Note", back_populates="attachments")


class NoteVersion(Base):
    __tablename__ = "note_versions"
    id = Column(Integer, primary_key=True)
    note_id = Column(Integer, ForeignKey("notes.id"), nullable=False)
    version_number = Column(Integer, nullable=False)
    content_markdown = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    note = relationship("Note", back_populates="versions")