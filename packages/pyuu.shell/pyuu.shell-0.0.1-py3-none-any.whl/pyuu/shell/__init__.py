import subprocess
import os
import tempfile

__all__=[
    
]

def run(cmd:str):
    bufsize=16<<10
    out_pipe=tempfile.SpooledTemporaryFile(mode='w+', max_size=bufsize)
    err_pipe=tempfile.SpooledTemporaryFile(mode='w+', max_size=bufsize)
    try:
        proc = subprocess.Popen(cmd, 
                                stdout=out_pipe, 
                                stderr=err_pipe,
                                shell=True,
                                universal_newlines=True,
                                text=True,
                                )
        proc.wait()
        out_pipe.seek(0)
        err_pipe.seek(0)
        class res:
            out=out_pipe.read()
            err=err_pipe.read()
            returncode=proc.returncode
    finally:
        out_pipe.close()
        err_pipe.close()
    return res

