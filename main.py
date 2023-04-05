import hashlib
import os

def compute_top_hash(file_list):
    """
    Computes the top-level hash of a list of files using the SHA-1 hash function.

    Parameters:
    file_list (list): A list of filenames (including path) to compute the hash over.

    Returns:
    str: The hexadecimal representation of the computed hash value.

    """
    original_top_hash = hashlib.sha1() # this Use  hash function
    for file_name in file_list:
        if os.path.isfile(file_name):  
            with open(file_name, "rb") as file:
                while True:
                    chunk = file.read(4096) 
                    if not chunk:
                        break
                    original_top_hash.update(chunk) # add the file content to the hash value
    return original_top_hash.hexdigest()

#  using this above function
file_list = os.listdir(".") # list all files in the current directory.this program can handle multiple files.
original_top_hash = compute_top_hash(file_list)
print("The original Top Hash is:", original_top_hash)

#  modifing  files the hash value will change.
with open("L1.txt", "a") as file:
    file.write("inputing data  into L1.txt file")

modified_top_hash = compute_top_hash(file_list)
print("Modified Top Hash:", modified_top_hash)

if original_top_hash != modified_top_hash:
    print("Top Hash does not match when one or more files are modified")
else:
    print("Top Hash matches when files are not modified")
