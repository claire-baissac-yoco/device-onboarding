import pytest
from device import Device
from mock_database import mockDatabase
from const import status_keys
from custom_error import FlashFailureException, InjectionFailureException

def gen_keys():
    return [0], [0], [0]

def get_dummy_device_info():
    serial_number = 1
    imei = 1
    box_number = 1
    crate_number = 1
    is_damaged = False
    return serial_number, imei, box_number, crate_number, is_damaged

def create_dummy_device() -> Device:
    serial_number, imei, box_number, crate_number, is_damaged = get_dummy_device_info()
    device = Device(serial_number, imei, box_number, crate_number, is_damaged)
    return device

def create_database_with_dummy_device() -> mockDatabase:
    serial_number, imei, box_number, crate_number, is_damaged = get_dummy_device_info()
    database = mockDatabase()
    database.create_device(serial_number, imei, box_number, crate_number, is_damaged)
    return database

def test_can_create_device():
    serial_number, imei, box_number, crate_number, is_damaged = get_dummy_device_info()
    device = create_dummy_device()
    assert device.get_serial_number() == serial_number
    assert device.get_imei() == imei
    assert device.get_box_number() == box_number
    assert device.get_crate_number() == crate_number
    assert device.get_is_damaged() == is_damaged

def test_can_add_device_to_device_list():
    database = create_database_with_dummy_device()
    assert database.get_number_of_devices() == 1

def test_can_get_device_from_device_list_by_serial_number():
    serial_number  = get_dummy_device_info()[0]
    database = create_database_with_dummy_device()
    assert database.get_device_by_serial_number(serial_number).get_serial_number() == serial_number

def test_can_get_device_from_device_list_by_imei():
    imei = get_dummy_device_info()[1]
    database = create_database_with_dummy_device()
    assert database.get_device_by_imei(imei).get_imei() == imei

def test_return_none_when_get_device_not_exist():
    database = create_database_with_dummy_device()
    assert database.get_device_by_imei(0) == None

def test_can_update_device_sim_card():
    serial_number  = get_dummy_device_info()[0]
    database = create_database_with_dummy_device()
    database.update_device_sim_card(serial_number, 1, 2)
    sim_card = database.get_device_by_serial_number(serial_number).get_sim_card()
    assert sim_card.get_snn() == 1
    assert sim_card.get_imsi() == 2

def test_can_flash_device():
    serial_number  = get_dummy_device_info()[0]
    database = create_database_with_dummy_device()
    database.flash_device(serial_number, 1)
    assert database.get_device_by_serial_number(serial_number).get_status() == status_keys['device_flashed']

def test_flash_device_raises_exception():
    with pytest.raises(FlashFailureException):
        serial_number  = get_dummy_device_info()[0]
        database = create_database_with_dummy_device()
        database.flash_device(serial_number, 0)

def test_can_inject_keys():
    serial_number  = get_dummy_device_info()[0]
    database = create_database_with_dummy_device()
    keys = gen_keys()
    database.inject_keys(serial_number, keys, 1)
    assert database.get_device_by_serial_number(serial_number).get_status() == status_keys['keys_injected']

def test_inject_keys_raises_exception():
    with pytest.raises(InjectionFailureException):
        serial_number  = get_dummy_device_info()[0]
        database = create_database_with_dummy_device()
        keys = gen_keys()
        database.inject_keys(serial_number, keys, 0)