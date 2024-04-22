#!/usr/bin/env python

import os
import base64

filename = input("Provide file name/path: ").strip()  # No need for str() around input
iterations = int(input("Enter number of iterations (times you would like to decode the contents of the file): "))
finished = False

try:
    with open(filename, 'r') as file:
        content = file.read()

    for i in range(iterations):
        content = base64.b64decode(content).decode('utf-8')  # Update content with decoded value

    with open("b64decoded.txt", 'w') as decoded:
        decoded.write(content)
        print("Successfully decoded file content.")

except FileNotFoundError:
    print(f"File: {filename}, does not appear to exist...")
except (PermissionError, IOError) as e:
    print(f"Error accessing file: {e}")

