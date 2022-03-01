from enum import Enum

class DeviceState(Enum):
    device_received = 1
    serial_number_recorded = 2
    imei_recorded = 3
    package_info_recorded = 4
    damage_recorded = 5
    sim_card_assigned = 6
    # snn_recorded = 7
    # imsi_recorded = 8
    device_flashed = 7
    keys_injected = 8
    sent_for_repacking = 9
    stored_in_warehouse = 10

# status_keys = {
#     'device_received': 1,
#     'serial_number_recorded': 2,
#     'imei_recorded': 3,
#     # 'box_number_recorded': 3,
#     'package_info_recorded': 4,
#     'damage_recorded': 5,
#     'sim_card_assigned': 5,
#     'snn_recorded': 7,
#     'imsi_recorded': 8,
#     'device_flashed': 9,
#     'keys_injected': 10,
#     'sent_for_repacking': 11,
#     'stored_in_warehouse': 12
# }