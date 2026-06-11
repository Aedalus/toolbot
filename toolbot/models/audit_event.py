"""Audit event model."""

from datetime import UTC, datetime

from toolbot.extensions import db


class AuditEvent(db.Model):
    """History of meaningful user or admin actions."""

    __tablename__ = "audit_events"

    id = db.Column(db.Integer, primary_key=True)
    actor_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True, index=True)
    action = db.Column(db.String(80), nullable=False, index=True)
    entity_type = db.Column(db.String(80), nullable=False, index=True)
    entity_id = db.Column(db.Integer, nullable=False, index=True)
    event_metadata = db.Column("metadata", db.JSON, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(UTC), index=True)

    actor = db.relationship("User", back_populates="audit_events")

    def __repr__(self):
        return f"<AuditEvent {self.action} {self.entity_type}:{self.entity_id}>"
