from warehouse import Warehouse
from const import DeviceState
from sim_card import SimCard
from custom_error import InvalidOperationException

class Device:
    def __init__(self, serial_number: str, imei: str):
        self._serial_number = serial_number
        self._imei = imei
        self._state = DeviceState.imei_recorded
        self._damage_rating = 0

    def set_imei(self, imei: int) -> None:
        self._imei = imei
        self._state = DeviceState.imei_recorded

    def set_package_info(self, box_number: int, crate_number: int) -> bool:
        self._box_number = box_number
        self._crate_number = crate_number
        self._state = DeviceState.package_info_recorded
        return True

    def get_serial_number(self):
        return self._serial_number

    def get_imei(self):
        return self._imei

    def get_box_number(self):
        return self._box_number

    def get_crate_number(self):
        return self._box_number

    def set_damage_rating(self, damage_rating) -> bool:
        if self.process_is_allowed(DeviceState.damage_recorded):
            self._damage_rating = damage_rating
            self._state = DeviceState.damage_recorded
            return True
        else:
            raise InvalidOperationException

    def get_damage_rating(self):
        return self._damage_rating

    def assign_sim_card(self, simcard: SimCard) -> bool:
        if self.process_is_allowed(DeviceState.sim_card_assigned):
            self._sim_card = simcard
            self._state = DeviceState.sim_card_assigned
            return True
        else:
            raise InvalidOperationException

    def get_sim_card(self):
        return self._sim_card

    def flash(self):
        if self.process_is_allowed(DeviceState.device_flashed):
            self._state = DeviceState.device_flashed
        else:
            raise InvalidOperationException('INVALID')

    def get_state(self):
        return self._state

    def inject_keys(self, keys: list):
        if self.process_is_allowed(DeviceState.keys_injected):
            self._keys = keys
            self._state = DeviceState.keys_injected
        else:
            raise InvalidOperationException

    def send_for_repacking(self):
        if self.process_is_allowed(DeviceState.sent_for_repacking):
            self._state = DeviceState.sent_for_repacking
            return True
        else:
            raise InvalidOperationException('INVALID')

    def set_warehouse(self, warehouse: Warehouse):
        print("here")
        if self.process_is_allowed(DeviceState.stored_in_warehouse):
            self._warehouse = warehouse
            self._state = DeviceState.stored_in_warehouse
            return True
        else:
            raise InvalidOperationException

    def process_is_allowed(self, desired_state):
        print(desired_state.value, self._state.value)
        if not desired_state.value - self._state.value <= 1:
            return False
        elif self._damage_rating > 0:
            return False
        return True