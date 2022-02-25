from device import Device
from custom_error import FlashFailureException

class IFlashDevice:
    def flash_device(self) -> bool:
        pass

class FlashDevice(IFlashDevice):
    def __init__(self, device: Device) -> None:
        self._device = device

    def flash_device(self) -> bool:
        try:
            self._device.flash()
        except:
            raise FlashFailureException
