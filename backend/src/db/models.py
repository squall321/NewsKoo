"""SQLAlchemy models describing the core NewsKoo tables."""
from __future__ import annotations

from datetime import datetime
import enum
from typing import List, Optional

from sqlalchemy import (
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

Base = declarative_base()


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )


class Source(Base, TimestampMixin):
    __tablename__ = "sources"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    base_url: Mapped[str] = mapped_column(String(255), nullable=False)
    rss_url: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    language: Mapped[str] = mapped_column(String(16), default="en", nullable=False)

    articles: Mapped[List["Article"]] = relationship("Article", back_populates="source", cascade="all, delete-orphan")


class ArticleStatus(enum.Enum):
    RAW = "raw"
    CLEANED = "cleaned"
    TRANSLATED = "translated"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class Article(Base, TimestampMixin):
    __tablename__ = "articles"
    __table_args__ = (UniqueConstraint("source_id", "origin_url", name="uq_articles_source_origin"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    source_id: Mapped[int] = mapped_column(ForeignKey("sources.id", ondelete="CASCADE"), nullable=False)
    origin_url: Mapped[str] = mapped_column(String(500), nullable=False)
    origin_title: Mapped[str] = mapped_column(String(500), nullable=False)
    origin_summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    origin_content: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    origin_published_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    status: Mapped[ArticleStatus] = mapped_column(Enum(ArticleStatus), default=ArticleStatus.RAW, nullable=False)
    topic: Mapped[Optional[str]] = mapped_column(String(64))

    source: Mapped[Source] = relationship("Source", back_populates="articles")
    translations: Mapped[List["ArticleTranslation"]] = relationship(
        "ArticleTranslation", back_populates="article", cascade="all, delete-orphan"
    )


class TranslationStatus(enum.Enum):
    PENDING = "pending"
    RUNNING = "running"
    REVIEW = "review"
    APPROVED = "approved"
    REJECTED = "rejected"


class ArticleTranslation(Base, TimestampMixin):
    __tablename__ = "article_translations"
    __table_args__ = (UniqueConstraint("article_id", "target_language", name="uq_translations_article_language"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    article_id: Mapped[int] = mapped_column(ForeignKey("articles.id", ondelete="CASCADE"), nullable=False)
    target_language: Mapped[str] = mapped_column(String(16), default="ko", nullable=False)
    translated_title: Mapped[str] = mapped_column(String(500), nullable=False)
    translated_summary: Mapped[Optional[str]] = mapped_column(Text)
    translated_content: Mapped[Optional[str]] = mapped_column(Text)
    translator_engine: Mapped[str] = mapped_column(String(64), default="open-source")
    reviewer: Mapped[Optional[str]] = mapped_column(String(255))
    status: Mapped[TranslationStatus] = mapped_column(Enum(TranslationStatus), default=TranslationStatus.PENDING, nullable=False)

    article: Mapped[Article] = relationship("Article", back_populates="translations")


class TranslationJob(Base, TimestampMixin):
    __tablename__ = "translation_jobs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    article_id: Mapped[int] = mapped_column(ForeignKey("articles.id", ondelete="CASCADE"), nullable=False)
    provider: Mapped[str] = mapped_column(String(64), nullable=False)
    priority: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    status: Mapped[TranslationStatus] = mapped_column(Enum(TranslationStatus), default=TranslationStatus.PENDING, nullable=False)
    started_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    finished_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    article: Mapped[Article] = relationship("Article")


__all__ = [
    "Base",
    "Source",
    "Article",
    "ArticleTranslation",
    "TranslationJob",
    "ArticleStatus",
    "TranslationStatus",
]
