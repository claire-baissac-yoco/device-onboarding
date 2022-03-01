from device import Device
from custom_error import FlashFailureException

class IFlashDevice:
    def flash_device(self) -> bool:
        pass

class FlashDevice(IFlashDevice):
    def __init__(self, state: int) -> None:
        self._state = state

    def flash_device(self) -> bool:
        if self._state == 1:
            return True
        else:
            raise FlashFailureException
