import subprocess
import os

# commands = ["dmesg", "ifconfig"]
commands = ["/root/test1.sh", "ifconfig"]

def dump_logs(job):
    # change dir to log dir for this command
    for command in commands:
        # Write to log files and store in results
        output = subprocess.check_output(command)

        f = open("%s"%(command))
        f.write(output.decode("utf-8"))
        f.close()
