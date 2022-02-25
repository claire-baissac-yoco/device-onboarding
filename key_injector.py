from device import Device
from custom_error import InjectionFailureException

class IKeyInjector:
    def injectKey(self, key: list) -> bool:
        pass

class KeyInjector(IKeyInjector):
    def __init__(self, device: Device) -> None:
        self._device = device

    def injectKey(self, key: list) -> bool:
        try:
            self._device.inject_key(key)
            return True
        except:
            raise InjectionFailureException