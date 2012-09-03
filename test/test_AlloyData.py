# test_AlloyData.py
# (C)2012 http://www.ThreeAddOne.com
# Scott Ernst

from alloy.data.AlloyData import AlloyData

print 100*'-' + '\n', 'TEST: AlloyData.getCategories()'
categories = AlloyData.getCategories()
print categories

print 100*'-' + '\n', 'TEST: AlloyData.getCommands()'
commands = AlloyData.getCommands(categories[0])
print commands

print 100*'-' + '\n', 'TEST: AlloyData.createCategory()'
newCategory = AlloyData.createCategory(u'Test Category')
print newCategory

print 100*'-' + '\n', 'TEST: AlloyData.modifyCategory()'
modifiedCategory = AlloyData.modifyCategory(newCategory['id'], label=u'Mod Category')
print modifiedCategory

print 100*'-' + '\n', 'TEST: AlloyData.getCategories()'
print AlloyData.getCategories()

print 100*'-' + '\n', 'TEST: AlloyData.deleteCategory()'
deletedCategory = AlloyData.deleteCategory(modifiedCategory['id'])
print deletedCategory

print 100*'-' + '\n', 'TEST: AlloyData.createCommand()'
newCommand = AlloyData.createCommand(categories[0]['id'], 1)
print newCommand

print 100*'-' + '\n', 'TEST: AlloyData.modifyCommand()'
modifiedCommand = AlloyData.modifyCommand(
    newCommand['id'],
    label=u'Modified Command',
    script=u'test me out\nsome more.',
    language=u'mel'
)
print modifiedCommand

print 100*'-' + '\n', 'TEST: AlloyData.getCommandData()'
commandData = AlloyData.getCommandData(modifiedCommand['id'])
print commandData

print 100*'-' + '\n', 'TEST: AlloyData.getCommands()'
print AlloyData.getCommands(categories[0]['id'])

print 100*'-' + '\n', 'TEST: AlloyData.deleteCommand()'
deletedCommand = AlloyData.deleteCommand(modifiedCommand['id'])
print deletedCommand

print 100*'-' + '\n', 'FINAL STATE TESTS:'
categories = AlloyData.getCategories()
print 'CATEGORIES:', categories

for c in categories:
    print 'COMMANDS(' + c['id'] + '):', AlloyData.getCommands(c['id'])

print 'TESTS COMPLETE!'
