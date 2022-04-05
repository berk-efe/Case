key = int(input("Anahtar(1-255 arası): "))
data = input("Şifrelemek istediğiniz veri: ")

data = bytearray(data, "ascii")
for index, value in enumerate(data):
    data[index] = value ^ key

db = open("database.txt", "w")
db.write(data.decode("utf-8"))
db.close()

