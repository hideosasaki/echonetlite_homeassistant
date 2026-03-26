from homeassistant.const import CONF_ICON
from pychonet.ElectricVehicleCharger import ElectricVehicleCharger
from ....const import CONF_ICONS, TYPE_SELECT

QUIRKS = {
    0xDA: {
        "EPC_FUNCTION": ElectricVehicleCharger.EPC_FUNCTIONS[0xDA],
        "ENL_OP_CODE": {
            TYPE_SELECT: {
                "Charging": 0x42,
                "Discharging": 0x43,
                "Standby": 0x44,
                "Idle": 0x47,
            },
            CONF_ICON: "mdi:ev-station",
            CONF_ICONS: {
                "Charging": "mdi:battery-charging",
                "Discharging": "mdi:home-lightning-bolt",
                "Standby": "mdi:pause-octagon",
                "Idle": "mdi:power-plug-off",
            },
        },
    },
}

# Fast polling: these EPCs are polled at a shorter interval
FAST_POLL = {
    "interval": 5,  # seconds
    "epcs": [0xD3],  # instantaneous power only (DA comes via push)
}

# When C7 (vehicle connection status) changes via push notification,
# clear optimistic lock on DA (operation mode) and refresh its value.
OPTIMISTIC_TRIGGER = {
    0xC7: [0xDA, 0xE4],  # C7 push → clear DA optimistic, then GET DA + SoC
}

# Composite state sensor: derives user-friendly status from C7 + DA
COMPOSITE_STATE = {
    "name": "Status",
    "connection_epc": 0xC7,
    "mode_epc": 0xDA,
    "connection_ready": [0x41, 0x42, 0x43],
    "connection_connecting": [0x40],
    "connection_disconnected": [0x30],
    "mode_map": {
        0x42: "Charging",
        0x43: "Discharging",
        0x44: "Standby",
    },
    "default_disconnected": "Idle",
    "default_connecting": "Processing",
    "default_unknown": "Unknown",
    "icons": {
        "Idle": "mdi:power-plug-off",
        "Processing": "mdi:progress-clock",
        "Standby": "mdi:pause-octagon",
        "Charging": "mdi:battery-charging",
        "Discharging": "mdi:home-lightning-bolt",
        "Unknown": "mdi:help-circle-outline",
    },
    "default_icon": "mdi:ev-station",
}
