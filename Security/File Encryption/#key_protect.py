import pyminizip

level=4 #level of compression
password = input("Assign Password: ")
pyminizip.compress("key.key",None,"key.key.zip",password ,level)
