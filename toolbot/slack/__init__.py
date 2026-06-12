"""Slack integration initialization."""

import atexit
import logging
import signal

logger = logging.getLogger(__name__)

_bolt_app = None
_socket_handler = None
_socket_mode_intended = False


def init_slack(app):
    """Initialize Slack Bolt in Socket Mode when Slack tokens are configured."""
    global _bolt_app, _socket_handler, _socket_mode_intended

    _shutdown_socket()
    _bolt_app = None
    _socket_mode_intended = False

    token = app.config.get("SLACK_BOT_TOKEN", "")
    app_token = app.config.get("SLACK_APP_TOKEN", "")

    if not token:
        logger.info("SLACK_BOT_TOKEN not configured, Slack module disabled")
        return

    if not app_token:
        logger.warning("SLACK_APP_TOKEN not configured, Slack module disabled")
        return

    if not token.startswith("xoxb-"):
        logger.warning("SLACK_BOT_TOKEN must be a Bot User OAuth Token starting with xoxb-, Slack module disabled")
        return

    if not app_token.startswith("xapp-"):
        logger.warning("SLACK_APP_TOKEN must be an app-level token starting with xapp-, Slack module disabled")
        return

    from slack_bolt import App
    from slack_sdk import WebClient

    try:
        _bolt_app = App(token=token, client=WebClient(token=token, timeout=15))
    except Exception:
        logger.warning("Failed to initialize Slack Bolt app, Slack module disabled", exc_info=True)
        _bolt_app = None
        return

    from toolbot.slack.handlers import register_handlers

    register_handlers(_bolt_app, app)
    logger.warning("Slack Bolt app initialized successfully")

    if app.config.get("TESTING"):
        logger.info("Testing mode, skipping Socket Mode connection")
        return

    if app.config["SLACK_SOCKET_MODE_CONNECT"].lower() != "true":
        logger.info("SLACK_SOCKET_MODE_CONNECT is not true, skipping Socket Mode connection")
        return

    try:
        _socket_mode_intended = True
        from slack_bolt.adapter.socket_mode import SocketModeHandler

        _socket_handler = SocketModeHandler(app=_bolt_app, app_token=app_token)
        _socket_handler.connect()
        logger.warning("Slack Socket Mode connected")
    except Exception:
        logger.warning("Failed to set up Slack Socket Mode; app will run without Slack", exc_info=True)
        _socket_handler = None
        return

    atexit.register(_shutdown_socket)

    import threading

    if threading.current_thread() is threading.main_thread():
        previous_handler = signal.getsignal(signal.SIGTERM)
        signal.signal(signal.SIGTERM, _build_sigterm_handler(previous_handler))


def _shutdown_socket():
    """Close the Socket Mode connection if one is active."""
    global _socket_handler

    if _socket_handler is not None:
        try:
            _socket_handler.close()
            logger.info("Slack Socket Mode disconnected")
        except Exception:
            logger.warning("Error closing Socket Mode connection", exc_info=True)
        _socket_handler = None


def _build_sigterm_handler(previous_handler):
    """Build a SIGTERM handler that closes Slack before preserving prior behavior."""

    def _sigterm_handler(signum, frame):
        _shutdown_socket()
        if previous_handler == signal.SIG_DFL:
            raise SystemExit(128 + signum)
        if callable(previous_handler) and previous_handler != signal.SIG_IGN:
            previous_handler(signum, frame)

    return _sigterm_handler


def is_socket_mode_enabled() -> bool:
    """Return whether the most recent init attempted Socket Mode setup."""
    return _socket_mode_intended


def is_socket_mode_connected() -> bool:
    """Return whether a Socket Mode handler is currently bound."""
    return _socket_handler is not None
