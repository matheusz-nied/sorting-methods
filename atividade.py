import util


paths = util.list_files()
i = 0
for path in paths:
    i += 1
    print(i + " " + path)
