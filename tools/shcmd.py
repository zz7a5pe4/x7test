#!/usr/bin/python

import shlex, subprocess
import pexpect

#bash treat return value 0 as success
class ShellResult:
    output = ""
    error = ""
    def __init__(self,v):
        self.ret = v

    def __str__(self):
        if self.ret == 0:
            return "Success"
        else:
            return "Fail: {0}".format(self.ret)

    def __nonzero__(self):
        if self.ret == 0:
            return True
        else:
            return False


def syncexec(shellcmds):
    if not shellcmds:
        return None
    args = shlex.split(shellcmds)
    ret = ShellResult(0)
    p = subprocess.Popen(args,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ret.output,ret.error = p.communicate()
    ret.ret = p.returncode
    return ret

def syncexec_timeout(shellcmds, t=600):
    if not shellcmds:
        return None
    ret = ShellResult(-1)
    child = None
    try:
        child = pexpect.spawn(shellcmds, timeout=t)
        ret.output=""
        #index = p.expect ([pexpect.EOF, pexpect.TIMEOUT])
        while(1):
            i = child.readline()
            ret.output += i
            if not i:
                break
            ret.error = ret.output
    except pexpect.TIMEOUT as e:
        ret.error = "Timeout while running: {0}".format(shellcmds)
    except pexpect.ExceptionPexpect as e:
        ret.error = str(e)
    finally:
        if child:
            child.close()
            ret.ret = child.exitstatus
    
    return ret
    

def main():
    if len(sys.argv) < 2:
        cmd = r"ls -al ."
    else:
        cmd = sys.argv[1]

    r = syncexec_timeout(cmd,10)
    #print r
    if r:
        # success
        print r.output.rstrip()
    else:
        # error occur
        print r.error.rstrip()
        exit()

if __name__ == '__main__':
    import sys
    main()
