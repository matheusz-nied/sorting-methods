import util
import sorting


paths = util.list_files()

i = 0
for path in paths:
    print(i, "- " + path)
    i += 1
print("\n")

array = util.open_file(paths[6])
number_line = util.count_array(array)

for line in array:
     print(line)

sorting.InsertionSort(array)
print("\n")
print("\n")

for line in array:
    print(line)