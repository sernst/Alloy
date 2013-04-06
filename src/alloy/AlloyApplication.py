# AlloyApplication.py
# (C)2013 http://www.ThreeAddOne.com
# Scott Ernst

from pyglass.app.PyGlassApplication import PyGlassApplication

#___________________________________________________________________________________________________ AlloyApplication
class AlloyApplication(PyGlassApplication):

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: debugRootResourcePath
    @property
    def debugRootResourcePath(self):
        return ['..', 'resources']

#___________________________________________________________________________________________________ GS: splashScreenUrl
    @property
    def splashScreenUrl(self):
        return None

#___________________________________________________________________________________________________ GS: appGroupID
    @property
    def appGroupID(self):
        return 'alloy'

#___________________________________________________________________________________________________ GS: mainWindowClass
    @property
    def mainWindowClass(self):
        from alloy.views.AlloyMainWindow import AlloyMainWindow
        return AlloyMainWindow

####################################################################################################
####################################################################################################

if __name__ == '__main__':
    AlloyApplication().run()

