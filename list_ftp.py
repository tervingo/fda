import os
from ftplib import FTP

def sync_ftp_directory(ftp_host, ftp_user, ftp_pass, ftp_dir, local_dir):
    # Connect to FTP server
    ftp = FTP(ftp_host)
    ftp.login(user=ftp_user, passwd=ftp_pass)
    
    # Change to the specified FTP directory
    ftp.cwd(ftp_dir)
    
    # Delete existing files in FTP directory
    for filename in ftp.nlst():
        try:
            print(f"File: {filename}")
        except:
            print(f"Could not find {filename}")
    
    # Close FTP connection
    ftp.quit()

# Usage example
if __name__ == "__main__":
    ftp_host = "ftp.onstatic-es.setupdns.net"
    ftp_user = "tervingo"
    ftp_pass = "sami.edaso"
    ftp_dir = "/public"
    local_dir = "C:\\Users\\j4alo\\Dropbox\\Eltomalturta\\flor\\public\\"
    
    sync_ftp_directory(ftp_host, ftp_user, ftp_pass, ftp_dir, local_dir)