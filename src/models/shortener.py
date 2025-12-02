from extensions.db import db

class Shortnener(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    code = db.Column(db.String(5), unique=True, nullable=False)
    amount_clicked = db.Column(db.Integer, server_default="0", nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "code": self.code,
            "url": self.url,
            "amount_clicked": self.amount_clicked,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }