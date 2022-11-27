#packing and unpacking
tuple1 = (1,2,3) #packing
(one, two, three) = tuple1 #unpacking
print(one)
print(two)
print(three)

tuple2 = ("car", "bike", "boat", "cycle")
(item1, *item2, item3) = tuple2
print(item1)
print(item2)
print(item3)