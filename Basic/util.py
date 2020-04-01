

# compress
import zipfile

# file write io
text = 'good\r\nboy'
with open('envar','w') as f:
    f.write(text)
    text = f.readline()

zip = zipfile.ZipFile('Deploy.zip','w')
zip.write('envar',compress_type=zipfile.ZIP_DEFLATED)
zip.close()