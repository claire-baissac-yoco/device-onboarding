from device import Device
from mock_database import mockDatabase

def get_dummy_device_info():
    serial_number = 1
    imei = 1
    box_number = 1
    crate_number = 1
    is_damaged = False
    return serial_number, imei, box_number, crate_number, is_damaged

def test_can_create_device():
    serial_number, imei, box_number, crate_number, is_damaged = get_dummy_device_info()
    device = Device(serial_number, imei, box_number, crate_number, is_damaged)
    assert device.get_serial_number() == serial_number
    assert device.get_imei() == imei
    assert device.get_box_number() == box_number
    assert device.get_crate_number() == crate_number
    assert device.get_is_damaged() == is_damaged

def test_can_add_device_to_device_list():
    serial_number, imei, box_number, crate_number, is_damaged = get_dummy_device_info()
    database = mockDatabase()
    database.create_device(serial_number, imei, box_number, crate_number, is_damaged)
    assert database.get_number_of_devices() == 1

def test_can_get_device_from_device_list_by_serial_number():
    serial_number, imei, box_number, crate_number, is_damaged = get_dummy_device_info()
    database = mockDatabase()
    database.create_device(serial_number, imei, box_number, crate_number, is_damaged)
    assert database.get_device_by_serial_number(serial_number).get_serial_number() == serial_number

def test_can_get_device_from_device_list_by_imei():
    serial_number, imei, box_number, crate_number, is_damaged = get_dummy_device_info()
    database = mockDatabase()
    database.create_device(serial_number, imei, box_number, crate_number, is_damaged)
    assert database.get_device_by_imei(imei).get_imei() == imei