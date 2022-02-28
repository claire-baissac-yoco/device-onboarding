from warehouse import Warehouse
from const import status_keys
from sim_card import SimCard

class Device:
    def __init__(self, serial_number: str):
        self._serial_number = serial_number
        self._state = status_keys['serial_number_recorded']

    def set_imei(self, imei: int) -> None:
        self._imei = imei
        self._state = status_keys['imei_recorded']

    def set_box_and_crate(self, box_number: int, crate_number: int) -> None:
        self._box_number = box_number
        self._crate_number = crate_number
        self._state = status_keys['package_info_recorded']

    def get_serial_number(self):
        return self._serial_number

    def get_imei(self):
        return self._imei

    def get_box_number(self):
        return self._box_number

    def get_crate_number(self):
        return self._box_number

    def get_is_damaged(self):
        return self._is_damaged

    def assign_sim_card(self, simcard: SimCard):
        self._sim_card = simcard
        self._state = status_keys['sim_card_assigned']

    def get_sim_card(self):
        return self._sim_card

    def flash(self):
        self._status = status_keys['device_flashed']

    def get_status(self):
        return self._status

    def inject_keys(self, keys: list):
        self._keys = keys
        self._status = status_keys['keys_injected']

    def send_for_repacking(self):
        self._status = status_keys['sent_for_repacking']

    def set_warehouse(self, warehouse: Warehouse):
        self._warehouse = warehouse
        self._status = status_keys['stored_in_warehouse']