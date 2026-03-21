from homeassistant.const import CONF_ICON
from pychonet.ElectricVehicleCharger import ElectricVehicleCharger
from ....const import CONF_ICONS

QUIRKS = {
    0xDA: {
        "EPC_FUNCTION": ElectricVehicleCharger.EPC_FUNCTIONS[0xDA],
        "ENL_OP_CODE": {
            CONF_ICON: "mdi:ev-station",
            CONF_ICONS: {
                "Charging": "mdi:battery-charging",
                "Discharging": "mdi:battery-arrow-down",
                "Standby": "mdi:battery-clock",
                "Idle": "mdi:power-plug-off",
                "Other": "mdi:help-circle-outline",
            },
        },
    },
}

# Fast polling: these EPCs are polled at a shorter interval
# and excluded from the normal polling cycle.
FAST_POLL = {
    "interval": 5,  # seconds
    "epcs": [0xD3, 0xDA],  # instantaneous power, operation mode
}
