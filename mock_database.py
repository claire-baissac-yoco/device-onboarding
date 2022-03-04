from custom_error import NoSuchDeviceException
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

        raise NoSuchDeviceException(f'Device with serial number {serial_number} does not exist')

    def get_device_by_imei(self, imei):
        for device in self._device_list:
            try:
                if device.get_imei() == imei:
                    return device
            except:
                raise ValueError

        raise NoSuchDeviceException(f'Device with IMEI {imei} does not exist')

    def set_device_package_info(self, serial_number, box_number, crate_number):
        try:
            self.get_device_by_serial_number(serial_number).set_package_info(box_number, crate_number)
        except Exception as err:
            raise err

    def set_device_damage_rating(self, serial_number, damage_rating):
        try:
            self.get_device_by_serial_number(serial_number).set_damage_rating(damage_rating)
        except Exception as err:
            raise err

    def update_device_sim_card(self, serial_number, snn, imsi):
        try:
            self.get_device_by_serial_number(serial_number).assign_sim_card(SimCard(snn, imsi))
        except Exception as err:
            raise err

    def flash_device(self, serial_number, mode):
        try:
            flash_device = FlashDevice(mode)
            if flash_device.flash_device():
                self.get_device_by_serial_number(serial_number).flash()
        except Exception as err:
            raise err

    def inject_keys(self, serial_number, keys, mode):
        try:
            key_injector = KeyInjector(mode)
            if key_injector.injectKey(keys):
                self.get_device_by_serial_number(serial_number).inject_keys(keys)
        except Exception as err:
            raise err

    def send_device_for_repacking(self, serial_number):
        try:
            self.get_device_by_serial_number(serial_number).send_for_repacking()
        except Exception as err:
            raise err

    def set_device_warehouse(self, serial_number, warehouse_info):
        try:
            self.get_device_by_serial_number(serial_number).set_warehouse(Warehouse(*warehouse_info))
        except Exception as err:
            raise err

