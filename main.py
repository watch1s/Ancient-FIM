import hashlib
import os

print("please enter the path you want to monitor ")

path = input("")

#Checking path of directory
if not os.path.exists(path):
    print("Please enter correct path")   
else:
    print("file path is exists")
    print(f"listing files in: {path}\n" + "|-"*50 + "|")
    
    for root, dirs, files in os.walk(path):
        #Loop for listing all files
        for file in files:
            file_path = os.path.join(root, file)
            
            with open(file_path, "rb") as f:
                content = f.read()
            # File Hash
            file_hash = hashlib.sha256(content).hexdigest()
            
            #Listing every file's sha256 codes
            print(f"{file} -> {file_hash}")




    

