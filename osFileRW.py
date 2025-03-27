import os


file = os.open("helloworld.txt", os.O_RDWR | os.O_CREAT | os.O_APPEND)
i = 0
while i < 10:

    os.write(file, b"THIS IS A TEST WRITE!\n")
    i = i + 1

os.lseek(file, 0, os.SEEK_SET)

data = os.read(file, 200)

print(f"Read from file: {data.decode()}")

os.close(file)