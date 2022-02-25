from device import Device

class mockDatabase:
    def __init__(self) -> None:
        self._device_list = []

    def get_number_of_devices(self):
        return len(self._device_list)

    def create_device(self, serial_number, imei, box_number, crate_number, is_damaged):
        self._device_list.append(Device(serial_number, imei, box_number, crate_number, is_damaged))

    def get_device_by_serial_number(self, serial_number):
        for device in self._device_list:
            try:
                if device.get_serial_number() == serial_number:
                    return device
            except:
                raise ValueError

        return None

    def get_device_by_imei(self, imei):
        for device in self._device_list:
            try:
                if device.get_imei() == imei:
                    return device
            except:
                raise ValueError

        return None