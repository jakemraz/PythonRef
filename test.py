import zipfile

text = 'good\r\nboy'
with open('envar','w') as f:
    f.write(text)

zip = zipfile.ZipFile('Deploy.zip','w')
zip.write('envar')
zip.close()