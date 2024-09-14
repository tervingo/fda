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
            ftp.delete(filename)
        except:
            print(f"Could not delete {filename}")
    
    # Upload files from local directory
    for root, dirs, files in os.walk(local_dir):
        for filename in files:
            local_path = os.path.join(root, filename)
            relative_path = os.path.relpath(local_path, local_dir)
            ftp_path = relative_path.replace(os.path.sep, '/')
            
            # Create directories if they don't exist
            current_dir = ''
            for part in os.path.dirname(ftp_path).split('/'):
                current_dir = f"{current_dir}/{part}"
                try:
                    ftp.mkd(current_dir)
                except:
                    pass  # Directory might already exist
            
            # Upload file
            with open(local_path, 'rb') as file:
                ftp.storbinary(f'STOR {ftp_path}', file)
            print(f"Uploaded {ftp_path}")
    
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