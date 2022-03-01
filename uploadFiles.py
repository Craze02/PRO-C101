import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_files(self, file_from, file_to):
        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode= WriteMode('overwrite'))

                

def main():
    access_token = "sl.BADSCesjV-8XB2zAhnDryQy-WDf3tuDAxQsGXskGfYEQ9uaDnXuhJRRnbIhuVAQ1JfX0gc0bn2w_qM3T3iZ-jjgQFFIfmFXFX-IW4HuK21ZVnZ6AwgUfjBwA9vpnZYKUuSPE6JU"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer:- ")
    file_to = input("Enter the path to upload to dropbox:- ")
    transferData.upload_files(file_from, file_to)
    print("File has been uploaded.")



if __name__ == '__main__':
    main()