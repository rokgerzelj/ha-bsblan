HVAC_MODES = [
    HVAC_MODE_HEAT, # Automatic / Comfort / Reduced, further specified by preset.
    HVAC_MODE_OFF # Schutzbetrieb
]

# import from core/homeassistant/components/climate/const.py 

PRESET_MODES = [
    PRESET_NONE, # Automatic, follows built in schedule in BSB controller.
    PRESET_COMFORT, # Comfort, manual Comfort mode setting.
    PRESET_AWAY # Reduced, manual Reduced mode setting.
]

class BSBLanClimate(ClimateEntity):
    def __init__(self, entry_id: str, bsblan: BSBLan):
        self.bsblan = bsblan

    async def async_update(self):
        # params to query: for HC1:
        # 700 - operating mode: Schutzbetrieb / Automatik / Reduziert / Komfort
        # 710 - Comfort setpoint
        # 711 - Comfort setpoint max / Reduced setpoint max
        # 712 - Reduced setpoint / Comfort setpoint min
        # 714 - Frost protect setpoint / Reduced setpoint min
        # 8000 - HC1 status
        # 8740 - HC1 actual room temp
        # 8749 - HC1 thermostat request for heat YES / NO
