from device import Device

def test_can_create_device():
    serial_number = 1
    imei = 1
    box_number = 1
    crate_number = 1
    is_damaged = False

    device = Device(serial_number, imei, box_number, crate_number, is_damaged)
    assert device.get_serial_number() == serial_number
    assert device.get_imei() == imei
    assert device.get_box_number() == box_number
    assert device.get_crate_number() == crate_number
    assert device.get_is_damaged() == is_damaged