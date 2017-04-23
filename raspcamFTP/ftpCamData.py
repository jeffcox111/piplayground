import ftplib
import os

ftp = ftplib.FTP("")
ftp.login("", "")

for root, dirs, files in os.walk("C:/ftptesting"):
    for fname in files:
        full_fname = os.path.join(root, fname)
        ftp.storbinary('STOR FTPUser/camerauploads/' + fname, open(full_fname, 'rb'))
