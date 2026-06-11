"""User model."""

from datetime import UTC, datetime

from toolbot.extensions import db


class User(db.Model):
    """Local user record linked to a Slack identity."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    slack_user_id = db.Column(db.String(80), nullable=False, unique=True, index=True)
    display_name = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="member", index=True)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(UTC))
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )

    reservations = db.relationship("Reservation", foreign_keys="Reservation.user_id", back_populates="user", lazy="dynamic")
    canceled_reservations = db.relationship(
        "Reservation",
        foreign_keys="Reservation.canceled_by_user_id",
        back_populates="canceled_by",
        lazy="dynamic",
    )
    audit_events = db.relationship("AuditEvent", back_populates="actor", lazy="dynamic")

    def __repr__(self):
        return f"<User {self.slack_user_id!r}>"
