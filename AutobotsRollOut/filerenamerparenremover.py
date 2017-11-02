import os

paths = (os.path.join(root, filename)
        for root, _, filenames in os.walk('../../media/items')
        for filename in filenames)

for path in paths:
    print(path)
    splitpath = path.split("/")
    print(splitpath)
    oldfilename = splitpath[len(splitpath)-1]
    print(oldfilename)
    #time to remove paren number paren
    oldfilenamesplit = oldfilename.split(" ")
    print(oldfilenamesplit)
    #check if need correction
    if ")" in oldfilenamesplit[len(oldfilenamesplit)-1]:
        oldfilenamesplit[len(oldfilenamesplit)-1] = ".png"
        newfilename = " ".join(oldfilenamesplit)
        print(newfilename)
        #remove 1 extra space from end of filename
        newfilename = newfilename.rsplit(" ", 1)
        newfilename = "".join(newfilename)
        print(newfilename)
        newpath = path.replace(oldfilename, newfilename)
        print(newpath)
        os.rename(path, newpath)
