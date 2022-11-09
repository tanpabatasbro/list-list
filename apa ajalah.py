data = ["kaco","bro","opung"]
print(data)
print(20*"=")
data_2 = ["becce","sis","jess"]
print(data_2)
print(20*"+")

#menambahkan list dengan list
data.extend(data_2)
print(f"data gabungan = {data}")
print(20*"*")

#merubah data  list
data[2] = "yasop"
print(f"data setelah di rubah = {data}")
print(20*"$")

#meremove data terakhir
data_akhir  = data.pop()
print(f"data setelah di remove = {data}")

