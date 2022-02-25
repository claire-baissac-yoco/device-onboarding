class Device:
    def __init__(self, serial_number, imei, box_number, crate_number, is_damaged):
        self._serial_number = serial_number
        self._imei = imei
        self._box_number = box_number
        self._crate_number = crate_number
        self._is_damaged = is_damaged

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

    def assign_sim_card(self, snn, imsi):
        self._snn = snn
        self._imsi = imsi