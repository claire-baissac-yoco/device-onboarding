from device import Device
from sim_card import SimCard
from flash_device import FlashDevice
from key_injector import KeyInjector
from warehouse import Warehouse

class mockDatabase:
    def __init__(self) -> None:
        self._device_list = []

    def get_number_of_devices(self):
        return len(self._device_list)

    def create_device(self, serial_number, imei):
        self._device_list.append(Device(serial_number, imei))

    def get_device_by_serial_number(self, serial_number) -> Device:
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

    def set_device_package_info(self, serial_number, box_number, crate_number):
        for i in range(len(self._device_list)):
            try:
                if self._device_list[i].get_serial_number() == serial_number:
                    if self._device_list[i].set_package_info(box_number, crate_number):
                        return None
                    else:
                        print("ERROR")
            except Exception as err:
                raise err

        return None

    def set_device_damage_rating(self, serial_number, damage_rating):
        for i in range(len(self._device_list)):
            try:
                if self._device_list[i].get_serial_number() == serial_number:
                    if self._device_list[i].set_is_damaged(damage_rating):
                        return None
                    else:
                        print("ERROR")
            except Exception as err:
                raise err

        return None

    def update_device_sim_card(self, serial_number, snn, imsi):
        for i in range(len(self._device_list)):
            try:
                if self._device_list[i].get_serial_number() == serial_number:
                    if self._device_list[i].assign_sim_card(SimCard(snn, imsi)):
                        return None
                    else:
                        print("ERROR")
            except Exception as err:
                raise err

        return None

    def flash_device(self, serial_number, mode):
        for i in range(len(self._device_list)):
            try:
                if self._device_list[i].get_serial_number() == serial_number:
                    flash_device = FlashDevice(mode)
                    print(flash_device.flash_device())
                    if flash_device.flash_device():
                        self._device_list[i].flash()
                    return None
            except Exception as err:
                raise err

        return None

    def inject_keys(self, serial_number, keys, mode):
        for i in range(len(self._device_list)):
            try:
                if self._device_list[i].get_serial_number() == serial_number:
                    key_injector = KeyInjector(mode)
                    if key_injector.injectKey(keys):
                        self._device_list[i].inject_keys(keys)
                    return None
            except Exception as err:
                raise err

        return None


    def set_device_warehouse(self, serial_number, warehouse_info):
        for i in range(len(self._device_list)):
            try:
                if self._device_list[i].get_serial_number() == serial_number:
                    self._device_list[i].set_warehouse(Warehouse(*warehouse_info))
            except Exception as err:
                raise err

        return None

