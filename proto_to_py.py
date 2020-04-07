import os
import sys
directory = 'object_detection/protos'
protoc_path = './protoc'
for file in os.listdir(directory):
    if file.endswith(".proto"):
        os.system(protoc_path+" "+directory+"/"+file+" --python_out=.")
