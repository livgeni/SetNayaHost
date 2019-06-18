"""
Update the naya (CDP) host IP address
"""

from EditWinHostsFile import upsert

IP_ADDR = input('Ip Address for instance-1.us-central1-c.c.naya-de.internal: ')

try:
    upsert('instance-1.us-central1-c.c.naya-de.internal', IP_ADDR, is_print_new_file=True)
except Exception as ex:
    print(f'Exception occured: {ex}')
    print(r'Try runnig as administrator')
else:
    print(f'Successfully updated the file')
finally:
    input('Press Enter to continue...')
