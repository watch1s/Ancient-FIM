import hashlib
import json
import os

def get_file_hash(file_path):
    #calculates hash
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()


def save_hashes_to_json(target_dir, output_file="baseline.json"):
    hashes = {}

    for root, _, files in os.walk(target_dir):
        for file in files:
            full_path = os.path.join(root, file)
            hashes[full_path] = get_file_hash(full_path)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(hashes, f, indent=4)
    print(f"Total {len(hashes)} file's hash saved to '{output_file}'")

while True:
    path = input("please enter the path you want to monitor: ")

    #Checking path of directory
    if not os.path.exists(path):
        print("Please enter correct path!")   
    else:
        print("file path is exists")
        print(f"listing files in: {path}\n" + "|-"*50 + "|")
        
        for root, dirs, files in os.walk(path):
            #Loop for listing all files
            for file in files:
                file_path = os.path.join(root, file)
                
                
                file_hash = get_file_hash(file_path)
                
                #Listing every file's sha256 codes
                #print(f"{file} --> {file_hash}")
        save_hashes_to_json(path)



    

