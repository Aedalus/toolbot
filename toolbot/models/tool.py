"""Tool model."""

from datetime import UTC, datetime

from toolbot.extensions import db


class Tool(db.Model):
    """Reservable makerspace equipment."""

    __tablename__ = "tools"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, index=True)
    slug = db.Column(db.String(120), nullable=False, unique=True, index=True)
    description = db.Column(db.Text, nullable=True)
    enabled = db.Column(db.Boolean, nullable=False, default=True, index=True)
    advance_booking_window_minutes = db.Column(db.Integer, nullable=False, default=120)
    min_duration_minutes = db.Column(db.Integer, nullable=False, default=15)
    max_duration_minutes = db.Column(db.Integer, nullable=False, default=120)
    slot_granularity_minutes = db.Column(db.Integer, nullable=False, default=15)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(UTC))
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )

    reservations = db.relationship("Reservation", back_populates="tool", lazy="dynamic")

    def __repr__(self):
        return f"<Tool {self.slug!r}>"
