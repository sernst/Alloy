# alloyApplication.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

import os
import sys
import getopt


#___________________________________________________________________________________________________ alloyApplication
def alloyApplication():
    """A script for..."""

    try:
        import alloy
    except Exception, err:
        sys.path.append(os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..', 'src'
        ))

    try:
        import alloy
    except Exception, err:
        print 'LOAD FAILURE: Unable to locate the Alloy source directories.'
        return

    alloy.run(sys.argv)

#___________________________________________________________________________________________________ usage
def usage():
    print """Runs the Alloy application."""

#___________________________________________________________________________________________________ main
def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], 'h', ['help'])
    except getopt.GetoptError, err:
        print str(err) + "\n"
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            sys.exit(0)
        else:
            print '\nUnknown argument: " + o + ". Unable to continue.\n\n'
            usage()
            sys.exit(2)

    alloyApplication()

####################################################################################################
####################################################################################################

if __name__ == '__main__':
    main()
