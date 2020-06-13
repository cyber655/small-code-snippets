#!/usr/bin/python
# -*- coding: utf-8 -*-

from ssh_client import SSHClient


ip_or_url = 'your-ip-or-url-here'
server_ssh_port = 22
username = 'root'
password = 'your-password-here'

client = None


def connect_to_server():
    global client
    client = SSHClient(ip_or_url, server_ssh_port, username, password)
    print('Successfully connected to server.')


# Method is not really needed but sometimes it is maybe a smart check
def is_remote_machine_using_bash():
    output_shell = client.exec_linux_command('echo $0')
    is_remote_machine_using_bash = bool(
        list(filter(lambda line: 'bash' in line, output_shell)).__len__())
    if is_remote_machine_using_bash is False:
        raise Exception(
            'Sorry the remote system is not using bash.')


def run_update_command():
    output_update = client.exec_linux_command('sudo apt-get update')
    print_list_values(output_update)
    output_upgrade = client.exec_linux_command(
        'sudo apt-get upgrade -y')
    print_list_values(output_upgrade)


def print_list_values(stdout_list):
    print(''.join(map(str, stdout_list)))


if __name__ == '__main__':
    try:
        connect_to_server()
        is_remote_machine_using_bash()
        run_update_command()
    except Exception as ex:
        print('Something unexpected happened: {0}'.format(ex))
    finally:
        if client is not None:
            client.close_connection()
