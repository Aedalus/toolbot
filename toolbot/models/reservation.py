"""Reservation model."""

from datetime import UTC, datetime

from toolbot.extensions import db


class Reservation(db.Model):
    """Time-bounded booking for one user and one tool."""

    __tablename__ = "reservations"

    id = db.Column(db.Integer, primary_key=True)
    tool_id = db.Column(db.Integer, db.ForeignKey("tools.id"), nullable=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    starts_at = db.Column(db.DateTime, nullable=False, index=True)
    ends_at = db.Column(db.DateTime, nullable=False, index=True)
    status = db.Column(db.String(20), nullable=False, default="active", index=True)
    notes = db.Column(db.Text, nullable=True)
    created_via = db.Column(db.String(20), nullable=False)
    canceled_at = db.Column(db.DateTime, nullable=True)
    canceled_by_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(UTC), index=True)
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )

    tool = db.relationship("Tool", back_populates="reservations")
    user = db.relationship("User", foreign_keys=[user_id], back_populates="reservations")
    canceled_by = db.relationship("User", foreign_keys=[canceled_by_user_id], back_populates="canceled_reservations")

    def __repr__(self):
        return f"<Reservation tool={self.tool_id} user={self.user_id} {self.starts_at}-{self.ends_at}>"
