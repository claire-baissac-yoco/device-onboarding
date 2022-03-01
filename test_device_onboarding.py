import pytest
from device import Device
from mock_database import mockDatabase
from const import DeviceState
from custom_error import FlashFailureException, InjectionFailureException, InvalidOperationException

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
    serial_number, imei = get_dummy_device_info()[0:2]
    device = Device(serial_number, imei)
    return device

def create_database_with_dummy_device() -> mockDatabase:
    serial_number, imei = get_dummy_device_info()[0:2]
    database = mockDatabase()
    database.create_device(serial_number, imei)
    return database

def update_device_to_given_state(database: mockDatabase, serial_number, state) -> mockDatabase:
    func_names = ['', '', '', 'set_device_package_info', 'set_device_damage_rating', 'update_device_sim_card', 'flash_device', 'inject_keys', 'send_device_for_repacking', 'set_device_warehouse']
    box_number, crate_number, is_damaged = get_dummy_device_info()[2:]
    snn, imsi = 1, 2
    mode = 1
    keys = gen_keys()
    func_params = ['', '', '', f'{box_number}, {crate_number}', f'{is_damaged}', f'{snn}, {imsi}', f'{mode}', 'keys, mode', '', '[1, 2, 3, 4, 5, 6]']
    last = False
    for st, name, params in zip(DeviceState, func_names, func_params):
        print(st, name, params)
        if st == state:
            last = True
        if not name == '':
            params = f', {params}' if params else ''
            to_eval = f'database.{name}(serial_number{params})'
            print(to_eval)
            eval(to_eval)

        if last:
            break

    return database

def test_can_create_device():
    serial_number = get_dummy_device_info()[0]
    device = create_dummy_device()
    assert device.get_serial_number() == serial_number

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

def test_can_record_package_info():
    serial_number, _, box_number, crate_number = get_dummy_device_info()[0:4]
    database = create_database_with_dummy_device()
    database.set_device_package_info(serial_number, box_number, crate_number)
    assert database.get_device_by_serial_number(serial_number).get_state() == DeviceState.package_info_recorded

def test_can_update_device_sim_card():
    serial_number  = get_dummy_device_info()[0]
    database = create_database_with_dummy_device()
    database = update_device_to_given_state(database, serial_number, DeviceState.sim_card_assigned)
    database.update_device_sim_card(serial_number, 1, 2)
    sim_card = database.get_device_by_serial_number(serial_number).get_sim_card()
    assert sim_card.get_snn() == 1
    assert sim_card.get_imsi() == 2

def test_update_sim_card_before_record_package_info_throws_exception():
    with pytest.raises(InvalidOperationException):
        serial_number  = get_dummy_device_info()[0]
        database = create_database_with_dummy_device()
        database.update_device_sim_card(serial_number, 1, 2)

def test_can_flash_device():
    serial_number  = get_dummy_device_info()[0]
    database = create_database_with_dummy_device()
    database = update_device_to_given_state(database, serial_number, DeviceState.sim_card_assigned)
    database.flash_device(serial_number, 1)
    assert database.get_device_by_serial_number(serial_number).get_state() == DeviceState.device_flashed

def test_flash_device_raises_exception_with_mode_zero():
    with pytest.raises(FlashFailureException):
        serial_number  = get_dummy_device_info()[0]
        database = create_database_with_dummy_device()
        database = update_device_to_given_state(database, serial_number, DeviceState.device_flashed)
        database.flash_device(serial_number, 0)

def test_can_inject_keys():
    serial_number  = get_dummy_device_info()[0]
    database = create_database_with_dummy_device()
    database = update_device_to_given_state(database, serial_number, DeviceState.device_flashed)
    keys = gen_keys()
    database.inject_keys(serial_number, keys, 1)
    assert database.get_device_by_serial_number(serial_number).get_state() == DeviceState.keys_injected

def test_inject_keys_raises_exception_with_mode_zero():
    with pytest.raises(InjectionFailureException):
        serial_number  = get_dummy_device_info()[0]
        database = create_database_with_dummy_device()
        database = update_device_to_given_state(database, serial_number, DeviceState.device_flashed)
        keys = gen_keys()
        database.inject_keys(serial_number, keys, 0)

def test_can_send_for_repacking():
    serial_number  = get_dummy_device_info()[0]
    database = create_database_with_dummy_device()
    database = update_device_to_given_state(database, serial_number, DeviceState.keys_injected)
    database.send_device_for_repacking(serial_number)
    assert database.get_device_by_serial_number(serial_number).get_state() == DeviceState.sent_for_repacking

def test_can_set_device_warehouse():
    serial_number  = get_dummy_device_info()[0]
    database = create_database_with_dummy_device()
    database = update_device_to_given_state(database, serial_number, DeviceState.sent_for_repacking)
    database.set_device_warehouse(serial_number, [1, 2, 3, 4, 5, 6])
    assert database.get_device_by_serial_number(serial_number).get_state() == DeviceState.stored_in_warehouse

