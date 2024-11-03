Jumlah = 0
string = ""
for i in range(1, 20, 2):
  Jumlah += i
  string += f"{i}"
  if i == 19 :
   string += " = "
else :
  string += " + "
print(f"{string} {Jumlah}")