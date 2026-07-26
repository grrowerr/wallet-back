from typing import Optional

from flask_sqlalchemy import SQLAlchemy

from app.extensions import db


class BaseCRUD:
    def __init__(self,database: SQLAlchemy, model: db.Model):
        self.db = database
        self.model = model

    def get_list(
            self,
            limit: Optional[int] = None,
            offset: Optional[int] = None,
            **filters
    ):
        query = self.db.session.query(self.model)

        if filters:
            query = query.filter_by(**filters)
        if limit and isinstance(limit, int):
            query = query.limit(limit)
        if offset and isinstance(offset, int):
            query = query.offset(offset)

        instances = query.all()

        return instances

    def get_by_ref(self, ref):
        return self.db.session.query(self.model).get(ref)

    def get_filtered(self, **filters):
        return (
            self.db
            .session
            .query(self.model)
            .filter_by(**filters)
            .first()
        )
