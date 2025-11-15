"""Repository layer for CRUD operations on Article entities."""
from __future__ import annotations

from typing import Iterable, List, Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.src.db import models


class ArticleRepository:
    """High level data access helper focused on article workflows."""

    def __init__(self, session: Session):
        self.session = session

    def create_article(
        self,
        *,
        source_id: int,
        origin_url: str,
        origin_title: str,
        origin_summary: Optional[str] = None,
        origin_content: Optional[str] = None,
        origin_published_at=None,
        topic: Optional[str] = None,
    ) -> models.Article:
        article = models.Article(
            source_id=source_id,
            origin_url=origin_url,
            origin_title=origin_title,
            origin_summary=origin_summary,
            origin_content=origin_content,
            origin_published_at=origin_published_at,
            topic=topic,
        )
        self.session.add(article)
        self.session.flush()
        return article

    def get_by_id(self, article_id: int) -> Optional[models.Article]:
        return self.session.get(models.Article, article_id)

    def get_by_source_and_url(self, source_id: int, origin_url: str) -> Optional[models.Article]:
        stmt = select(models.Article).where(
            models.Article.source_id == source_id, models.Article.origin_url == origin_url
        )
        return self.session.execute(stmt).scalar_one_or_none()

    def list_recent(self, limit: int = 20) -> List[models.Article]:
        stmt = select(models.Article).order_by(models.Article.created_at.desc()).limit(limit)
        return list(self.session.execute(stmt).scalars())

    def list_by_status(self, status: models.ArticleStatus, limit: int = 50) -> List[models.Article]:
        stmt = (
            select(models.Article)
            .where(models.Article.status == status)
            .order_by(models.Article.updated_at.desc())
            .limit(limit)
        )
        return list(self.session.execute(stmt).scalars())

    def update_status(self, article: models.Article, status: models.ArticleStatus) -> models.Article:
        article.status = status
        self.session.add(article)
        self.session.flush()
        return article

    def attach_translations(
        self,
        article: models.Article,
        translations: Iterable[dict],
        *,
        target_language: str = "ko",
    ) -> List[models.ArticleTranslation]:
        created: List[models.ArticleTranslation] = []
        for payload in translations:
            translation = models.ArticleTranslation(
                article=article,
                target_language=payload.get("target_language", target_language),
                translated_title=payload["translated_title"],
                translated_summary=payload.get("translated_summary"),
                translated_content=payload.get("translated_content"),
                translator_engine=payload.get("translator_engine", "open-source"),
                reviewer=payload.get("reviewer"),
                status=payload.get("status", models.TranslationStatus.REVIEW),
            )
            self.session.add(translation)
            created.append(translation)
        self.session.flush()
        return created


__all__ = ["ArticleRepository"]
