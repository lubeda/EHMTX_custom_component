"""The notify integration."""
from __future__ import annotations
import logging

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

def setup(hass, config):
    """Set up the EHMTX Notification."""
    _LOGGER.debug("Setting up EHMTX platform")
    return True
