import subprocess
import argparse

parser = argparse.ArgumentParser(description='Run ZMap on a list of hosts.')
parser.add_argument('--hosts', help='the file with the list of hosts', required=True)
parser.add_argument('--output', help='the output file for the scan results', required=True)
args = parser.parse_args()


with open(args.hosts, 'r') as file:
    hosts = [line.strip() for line in file]  # read and strip newline from each line

# Run ZMap for each host and port
for host in hosts:
    for port in range(1, 65536):  # Loop over ports 1-65535
        # Form the zmap command
        command = f"zmap -p {port} -o - -N 10000 {host} | tee -a {args.output}"

        # Execute the command
        process = subprocess.Popen(command, shell=True)
        process.wait()
