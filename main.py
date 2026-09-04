from datetime import datetime
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


def check_for_changes(target_dir, baseline_file = "baseline.json"):
    with open(baseline_file, "r", encoding="utf-8") as f:
        old_hashes = json.load(f)

    current_hashes = {}
    for root, _, files in os.walk(target_dir):
        for file in files:
            full_path = os.path.join(root, file)
            if full_path == os.path.abspath(baseline_file):
                continue
            h = get_file_hash(full_path)
            #checks the variable is not blank.
            if h:
                current_hashes[full_path] = h
            else:
                print(f"unidentified file: {full_path}")

    old_paths = set(old_hashes.keys())
    current_paths = set(current_hashes.keys())

    changes_detected = False
    now = datetime.now().strftime("%H:%M:%S")

    for path in current_paths - old_paths:
        print(f"[{now}] [New File] --> {path}")
        changes_detected = True

    for path in old_paths - current_paths:
        print(f"[{now}] [Removed File] --> {path}")
        changes_detected = True

    for path in old_paths & current_paths:
     if old_hashes[path] != current_hashes[path]:
       print(f"[{now}] [Changed File]    -> {path}")
       changes_detected = True

    if changes_detected:
      with open(baseline_file, "w", encoding="utf-8") as f:
          json.dump(current_hashes, f, indent=4)


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
        #save_hashes_to_json(path)
        check_for_changes(path)



    

