"""Support for file notification."""
from __future__ import annotations

import voluptuous as vol
import logging

import homeassistant.helpers.config_validation as cv

from .const import ATTR_ICON,ATTR_DEVICE,ATTR_DATA

from homeassistant.components.notify import (
    PLATFORM_SCHEMA,
    BaseNotificationService,
)

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(ATTR_ICON, default="error"): cv.string,
        vol.Required(ATTR_DEVICE): cv.string,
    }
)

def get_service(
    hass: HomeAssistant, config: ConfigType, discovery_info=None
) -> EhmtxNotificationService:
    """Get the file notification service."""
    data = {
        ATTR_DEVICE: config[ATTR_DEVICE],
        ATTR_ICON: config[ATTR_ICON],
    }
    return EhmtxNotificationService(hass,data)


class EhmtxNotificationService(BaseNotificationService):
    """Implement the notification service for the File service."""
    hass: HomeAssistant

    def __init__(self,hass,data) -> None:
        """Initialize the service."""
        self.hass = hass
        self.data = data

    def send_message(self, message="", **kwargs) -> None:
        """Send a message to a matrix."""

        data = kwargs.get(ATTR_DATA)
        _LOGGER.debug("Data: %s", data)
        icon = self.data[ATTR_ICON]

        if data is not None:
            if ATTR_ICON in data:
                icon = data[ATTR_ICON]

        _LOGGER.info("Sending device/icon/text: %s/%s/%s", self.data[ATTR_DEVICE],icon, message)

        try:
            self.hass.services.call("esphome",self.data[ATTR_DEVICE]+"_screen",dict(icon_name=icon,text=message))
        except TimeoutError:
            _LOGGER.error("Target failed: %s", self.data[ATTR_DEVICE])
