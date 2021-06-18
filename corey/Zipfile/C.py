import zipfile

with zipfile.ZipFile('files.zip','r') as my_zip:
    my_zip.extractall('files')