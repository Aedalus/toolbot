"""Slack event handlers."""

import logging

logger = logging.getLogger(__name__)


def register_handlers(bolt_app, app):
    """Register Toolbot Slack event handlers."""

    @bolt_app.event("app_mention")
    def handle_app_mention(event, say):
        text = event.get("text", "").lower()
        logger.warning(
            "Received Slack app_mention event channel=%s user=%s ts=%s",
            event.get("channel"),
            event.get("user"),
            event.get("ts"),
        )

        if "ping" not in text:
            logger.warning("Ignoring Slack app_mention without ping")
            return

        try:
            say(text="pong 🏓", thread_ts=event.get("thread_ts", event.get("ts")))
            logger.warning("Replied pong to Slack app_mention")
        except Exception:
            logger.warning("Failed to reply to Slack app_mention", exc_info=True)
