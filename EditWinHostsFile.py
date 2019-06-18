"""
Work with windows etc\hosts file (%WINDIR%\\system32\\drivers\\etc\\hosts)
Get hostname and IP address as input.
If line for hostname exists - update it, if not add a new one
"""

import os

ETC_HOSTS_FILE = os.path.join(os.environ['WINDIR'], 'system32\drivers\etc\hosts')

def upsert(hostname, ip_addr, is_print_new_file):
    """
    remove existing hostname (if exists), insert the new value
    """
    with open(ETC_HOSTS_FILE, 'r') as hosts_file:
        hosts_file_data = hosts_file.readlines()

    #Read from the file
    for idx, line in enumerate(hosts_file_data):
        #print(f'line: {line}')
        if hostname in line:
            print(hosts_file_data)
            hosts_file_data.remove(line)
            hosts_file_data.insert(idx, f' {ip_addr} {hostname}\n')
            #print(f'removed line: {line}')

    #write back to the file
    with open(ETC_HOSTS_FILE, 'w') as target_hosts_file:
        target_hosts_file.writelines(hosts_file_data)

    if is_print_new_file:
        with open(ETC_HOSTS_FILE, 'r') as new_hosts_file:
            print(new_hosts_file.read())

if __name__ == "__main__":
    #testing
    print(f'ETC_HOSTS_FILE: {ETC_HOSTS_FILE}')
    upsert('instance-1.us-central1-c.c.naya-de.internal', '1.1.1.1', True)
