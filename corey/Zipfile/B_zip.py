import zipfile

my_zip=zipfile.ZipFile('files.zip','w')

my_zip.write('black_panther.txt')
my_zip.write('panther.png')

my_zip.close()