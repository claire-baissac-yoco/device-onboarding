class InjectionFailureException(Exception):
    def __init__(self, msg='Failed to key inject device', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

class FlashFailureException(Exception):
    def __init__(self, msg='Failed to flash device', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

class InvalidOperationException(Exception):
    def __init__(self, msg='This operation is prohibited for the given device', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)

class NoSuchDeviceException(Exception):
    def __init__(self, msg='No such device exists', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)