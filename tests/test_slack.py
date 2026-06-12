"""Tests for Toolbot Slack handlers."""

import signal
from unittest.mock import MagicMock

import pytest


def _register_and_capture(app):
    """Register handlers on a mock Bolt app and capture the handler functions."""
    from toolbot.slack.handlers import register_handlers

    handlers = {}

    def capture_event(event_type):
        def decorator(fn):
            handlers[f"event:{event_type}"] = fn
            return fn

        return decorator

    bolt_app = MagicMock()
    bolt_app.event = capture_event
    register_handlers(bolt_app, app)
    return handlers


def test_app_mention_ping_replies_pong(app):
    handlers = _register_and_capture(app)
    say = MagicMock()

    handlers["event:app_mention"](
        event={
            "type": "app_mention",
            "text": "<@UTOOLBOT> ping",
            "ts": "1710000000.000100",
        },
        say=say,
    )

    say.assert_called_once_with(text="pong 🏓", thread_ts="1710000000.000100")


def test_app_mention_ignores_non_ping(app):
    handlers = _register_and_capture(app)
    say = MagicMock()

    handlers["event:app_mention"](
        event={
            "type": "app_mention",
            "text": "<@UTOOLBOT> help",
            "ts": "1710000000.000100",
        },
        say=say,
    )

    say.assert_not_called()


def test_sigterm_handler_closes_socket_and_exits_for_default_handler():
    import toolbot.slack as slack_mod

    socket_handler = MagicMock()
    slack_mod._socket_handler = socket_handler
    handler = slack_mod._build_sigterm_handler(signal.SIG_DFL)

    with pytest.raises(SystemExit) as exc:
        handler(signal.SIGTERM, None)

    socket_handler.close.assert_called_once_with()
    assert slack_mod._socket_handler is None
    assert exc.value.code == 128 + signal.SIGTERM


def test_sigterm_handler_closes_socket_and_delegates_custom_handler():
    import toolbot.slack as slack_mod

    previous_handler = MagicMock()
    socket_handler = MagicMock()
    slack_mod._socket_handler = socket_handler
    handler = slack_mod._build_sigterm_handler(previous_handler)

    handler(signal.SIGTERM, None)

    socket_handler.close.assert_called_once_with()
    previous_handler.assert_called_once_with(signal.SIGTERM, None)
    assert slack_mod._socket_handler is None


def test_sigterm_handler_closes_socket_and_preserves_ignored_signal():
    import toolbot.slack as slack_mod

    socket_handler = MagicMock()
    slack_mod._socket_handler = socket_handler
    handler = slack_mod._build_sigterm_handler(signal.SIG_IGN)

    handler(signal.SIGTERM, None)

    socket_handler.close.assert_called_once_with()
    assert slack_mod._socket_handler is None
