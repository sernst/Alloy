# __init__.py
#(C)2012 http://www.ThreeAddOne.com
# Scott Ernst

import nimble
import imp

#___________________________________________________________________________________________________ remoteExec
def remoteExec(script):
    """ Executes a remote python script as specified by the argument.

        @@@param script:string
            The python script to execute

        @@@return:boolean
            True if the script executed without throwing an error, otherwise False.
    """

    try:
        nimble.cmds.undoInfo(openChunk=True)
    except Exception, err:
        print err
        return False

    success = True
    try:
        module = imp.new_module('runExecTempModule')
        exec script in module.__dict__
    except Exception, err:
        print err
        success = False

    try:
        nimble.cmds.undoInfo(closeChunk=True)
    except Exception, err:
        print err
        return False

    return success
