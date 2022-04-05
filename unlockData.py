import os

key = int(input("Anahtar(1-255 arası): "))
db = open("database.txt", "r")
data = db.read()
db.close()

data = bytearray(data, "ascii")
for index, value in enumerate(data):
    data[index] = value ^ key

os.remove("database.txt")

db = open("database.txt", "w")
print(data.decode("utf-8"))
db.write(data.decode("utf-8"))