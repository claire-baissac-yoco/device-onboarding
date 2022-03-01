from custom_error import InjectionFailureException

class IKeyInjector:
    def injectKey(self, key: list) -> bool:
        pass

class KeyInjector(IKeyInjector):
    def __init__(self, state: int) -> None:
        self._state = state

    def injectKey(self, key: list) -> bool:
        if self._state:
            return True
        else:
            raise InjectionFailureException