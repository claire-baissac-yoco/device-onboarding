import click
from click_shell import shell
from mock_database import mockDatabase

database = mockDatabase()

# @click.group(invoke_without_command=True)
@shell(prompt='device-onboarding > ', intro='Starting device onboarding...')
@click.pass_context
def main(ctx):
    pass

@main.command('add')
@click.option('--serial_number', prompt='Enter the serial number of the device')
@click.option('--imei', prompt='Enter the imei number of the device')
def create_device(serial_number, imei):
    try:
        database.create_device(serial_number, imei)
        click.echo('Device successfully registered')
    except Exception as err:
        click.echo(f'ERROR: {err}')

@main.command('record-package')
@click.option('--serial_number', prompt='Enter the serial number of the device')
@click.option('--box_number', prompt='Enter the box number of the device')
@click.option('--crate_number', prompt='Enter the crate number of the device')
def set_device_package_info(serial_number, box_number, crate_number):
    try:
        database.set_device_package_info(serial_number, box_number, crate_number)
    except Exception as err:
        click.echo(f'ERROR: {err}')

@main.command('record-damage')
@click.option('--serial_number', prompt='Enter the serial number of the device')
@click.option('--damage_level', type=click.Choice(['none', 'slight', 'severe']),  prompt='Enter the degree of damage to the device')
def record_damage(serial_number, damage_level):
    try:
        database.set_device_damage_rating(serial_number, damage_level)
    except Exception as err:
        click.echo(f'ERROR: {err}')

@main.command('assign-sim')
@click.option('--snn', prompt='Enter the SNN for the SIM card')
@click.option('--imsi', prompt='Enter the IMSI for the SIM card')
@click.option('--serial_number', prompt='Enter the serial number of the device')
def assign_sim(snn, imsi, serial_number):
    try:
        database.update_device_sim_card(serial_number, snn, imsi)
    except Exception as err:
        click.echo(f'ERROR: {err}')

@main.command('flash')
@click.option('--serial_number', prompt='Enter the serial number of the device')
def flash_device(serial_number):
    print(serial_number)
    try:
        database.flash_device(serial_number, 1)
    except Exception as err:
        click.echo(f'ERROR: {err}')

@main.command('inject-key')
@click.option('--keys', prompt='Enter key to inject into the device')
@click.option('--serial_number', prompt='Enter the serial number of the device')
def inject_key(keys, serial_number):
    try:
        database.inject_keys(serial_number, keys, 1)
    except Exception as err:
        click.echo(f'ERROR: {err}')

@main.command('info')
@click.option('--serial_number', prompt='Enter the serial number of the device')
def get_device_info(serial_number):
    try:
        device = database.get_device_by_serial_number(serial_number)
        click.echo(f'Current state of device: {device.get_state()}')
    except Exception as err:
        click.echo(f'ERROR: {err}')

if __name__ == '__main__':
    main(obj = {})