class SimCard:
    def __init__(self, snn, imsi):
        self._snn = snn
        self._imsi = imsi

    def get_snn(self):
        return self._snn

    def get_imsi(self):
        return self._imsi