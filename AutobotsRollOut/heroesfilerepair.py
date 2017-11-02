import os

paths = (os.path.join(root, filename)
        for root, _, filenames in os.walk('../../media/heroes')
        for filename in filenames)


for path in paths:
    print(path)
    splitpath = path.split("/")
    print(splitpath)
    oldfilename = splitpath[len(splitpath)-1]
    print(oldfilename)
    newfilename = oldfilename.replace("1", "")
    print(newfilename)
    newpath = path.replace(oldfilename, newfilename)
    print(newpath)
    os.rename(path, newpath)
