'''
This snippet just executes any linux command 
with python version >= 3.5 
and returns stdout and stderr output
'''

import subprocess


def run_linux_command(command):
    result = subprocess.run([command], capture_output=True, shell=True)
    stdout = result.stdout.decode("utf-8")
    stderr = result.stderr.decode("utf-8")
    print(stdout)
    print(stderr)
    return stdout, stderr


if __name__ == "__main__":
    # Example command: Listing filenames without permissions
    stdout, stderr = run_linux_command('ls -p | grep -v /')
    print(stdout)
    print(stderr)
