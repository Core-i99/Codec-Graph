from pathlib import Path




inputcodec = input("drag & drop codec dump:")
print (inputcodec)

inputcodec.remove(f'')
my_file = Path(inputcodec)
if my_file.is_file():
    print("found")
else:
    print("not found")
