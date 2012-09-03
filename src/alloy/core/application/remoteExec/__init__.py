# __init__.py
#(C)2012 http://www.ThreeAddOne.com
# Scott Ernst

def remoteExec(script):
    try:
        exec script
    except Exception, err:
        return False
    return True