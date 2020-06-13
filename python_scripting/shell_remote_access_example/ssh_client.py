#!/usr/bin/python
# -*- coding: utf-8 -*-

import paramiko


class SSHClient:

    def __init__(self, host_name, port, username, password):
        print('Connecting to server via ssh...')
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host_name, port, username=username, password=password)
        self.client = client
        print('Successfully connected!')

    def exec_linux_command(self, command):
        print('Execute command: {0}'.format(command))
        stdin, stdout, stderr = self.client.exec_command(command)
        error_message = stderr.read().decode('utf-8')
        if error_message:
            print('Error: {0}'.format(error_message))
        lines = stdout.readlines()
        #lines = [linebreak.replace('\n', '') for linebreak in lines]
        #lines = [linebreak.replace('\r', '') for linebreak in lines]
        print('Command successfully executed')
        return lines

    def close_connection(self):
        self.client.close()
        print('Connection successfully closed.')
