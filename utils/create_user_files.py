"""
Modul, ktory sluzi na vyrobenie user_settings.txt suboru 
z user_settings.txt.template.
"""

import os

if not os.path.isfile("./user_settings.txt"):
    import shutil
    source_file= r'./user_settings.txt.template'
    destination_file = r'./user_settings.txt'
    
    shutil.copyfile(source_file, destination_file)

if not os.path.isfile("./cases/inventory.txt"):
    open('./cases/inventory.txt', 'a').close()
