#!/usr/bin/python
import os

# Open a file
path = "hosts"
file_source = os.open(path, os.O_RDWR | os.O_CREAT)

# Close opened file
os.close( file_source )

# Now create another copy of the above file.
file_target = "/etc/hosts"
os.remove(file_target)
os.link(path, file_target)
os.chmod(file_target, 644)

print("Hosts linked successfully!!")
