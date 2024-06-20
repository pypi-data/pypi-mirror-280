import subprocess
import os

__all__=[
    
]

def run(cmd:str):
    proc = subprocess.Popen(cmd, 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE,
                            shell=True,
                            universal_newlines=True,
                            text=True
                            )
    proc.wait()
    class res:
        out=proc.stdout.read()
        err=proc.stderr.read()
        returncode=proc.returncode
    return res

