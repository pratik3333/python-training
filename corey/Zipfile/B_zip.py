import zipfile

with zipfile.ZipFile('files.zip','w') as my_zip:
    my_zip.write('black_panther.txt')
    my_zip.write('panther.png')

