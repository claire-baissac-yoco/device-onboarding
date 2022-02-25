import click
from mock_database import mockDatabase

database = mockDatabase()

@click.group(invoke_without_command=True)
def main():
    print("WELCOME")

@main.command('add')
@click.option('--serial_number', prompt='Enter the serial number of the device')
@click.option('--imei', prompt='Enter the imei number of the device')
@click.option('--box_number', prompt='Enter the box number of the device')
@click.option('--crate_number', prompt='Enter the crate number of the device')
def create_device(serial_number, imei, box_number, crate_number):
    database.create_device(serial_number, imei, box_number, crate_number, False)
    print(database.get_number_of_devices())

@main.command('record-damage')
@click.option('--damage_level', type=click.Choice(['none', 'slight', 'severe']),  prompt='Enter the degree of damage to the device')
def record_damage(damage_level):
    print(damage_level)

@main.command('assign-sim')
@click.option('--snn', prompt='Enter the SNN for the SIM card')
@click.option('--imsi', prompt='Enter the IMSI for the SIM card')
@click.option('--serial_number', prompt='Enter the serial number of the device')
def assign_sim(snn, imsi, serial_number):
    print(snn, imsi, serial_number)

@main.command('flash')
@click.option('--serial_number', prompt='Enter the serial number of the device')
def flash_device(serial_number):
    print(serial_number)

@main.command('inject-key')
@click.option('--key', prompt='Enter key to inject into the device')
@click.option('--serial_number', prompt='Enter the serial number of the device')
def inject_key(key, serial_number):
    print(key, serial_number)

if __name__ == '__main__':
    main()