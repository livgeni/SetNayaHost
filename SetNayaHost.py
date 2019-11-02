"""
Update the naya (CDP) host IP address
"""

from EditWinHostsFile import upsert

default_hostname = 'naya-cnt7-cdh6-v2.us-central1-a.c.naya-de.internal'

hostname = input(f'Naya server full name (default:{default_hostname}):')
if len(hostname) < 1:
	hostname = 'naya-cnt7-cdh6-v2.us-central1-a.c.naya-de.internal'
ip_addr = input(f'Ip Address for {hostname}: ')

try:
    upsert(hostname, ip_addr, is_print_new_file=True)
except Exception as ex:
    print(f'Exception occured: {ex}')
    print(r'Try runnig as administrator')
else:
    print(f'Successfully updated the file')
finally:
    input('Press Enter to continue...')
