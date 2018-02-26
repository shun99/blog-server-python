from app import db
import datetime


class BaseModel(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow,
                           onupdate=datetime.datetime.utcnow, index=True)

    def __repr__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.id)

    def update(self, **kwargs):
        try:
            for k, v in kwargs.items():
                setattr(self, k, v)
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)
            raise e
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def check_unique(cls, **kwargs):
        if cls.query.filter_by(**kwargs).first():
            return False
        return True
