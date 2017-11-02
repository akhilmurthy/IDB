import os

paths = (os.path.join(root, filename)
        for root, _, filenames in os.walk('../../media/skins')
        for filename in filenames)

'''
#phase 1 remove hero name
for path in paths:
    print(path)
    splitpath = path.split("/")
    print(splitpath)
    oldfilename = splitpath[len(splitpath)-1]
    print(oldfilename)
    #time to seperate hero name
    oldfilenamesplit = oldfilename.split(" ", 1)
    print(oldfilenamesplit)
    oldfilenamesplit[0] = ""
    newfilename = "".join(oldfilenamesplit)
    print(newfilename)

    newpath = path.replace(oldfilename, newfilename)
    print(newpath)
    os.rename(path, newpath)
'''

'''
#phase 2 event name
events = ["summergames", "winterwonderland", "uprising", "anniversary"]
for path in paths:
    print(path)
    splitpath = path.split("/")
    print(splitpath)
    oldfilename = splitpath[len(splitpath)-1]
    print(oldfilename)
    #time to seperate event name
    stripeventname = 0
    for event in events:
        if event in oldfilename:
            stripeventname = 1
    if stripeventname == 1:
        oldfilenamesplit = oldfilename.split(" ", 1)
        print(oldfilenamesplit)
        oldfilenamesplit[0] = ""
        newfilename = "".join(oldfilenamesplit)
        print(newfilename)

        newpath = path.replace(oldfilename, newfilename)
        print(newpath)
        os.rename(path, newpath)
'''
'''
#phase 3 remove "rarity skin" and hyphens
for path in paths:
    print(path)
    splitpath = path.split("/")
    print(splitpath)
    oldfilename = splitpath[len(splitpath)-1]
    print(oldfilename)
    #time to seperate rarity
    if "skin" in oldfilename:
        oldfilenamesplit = oldfilename.split("-")
        print(oldfilenamesplit)
        newfilename = oldfilenamesplit[1] + ".jpg"
        print(newfilename)
        #remove leading and ending spaces
        newfilename = newfilename.replace(" ", "")
        print(newfilename)
        newpath = path.replace(oldfilename, newfilename)
        print(newpath)
        print("---")
        os.rename(path, newpath)
'''
'''
#phase 4 make all lowercase
for path in paths:
    print(path)
    splitpath = path.split("/")
    print(splitpath)
    oldfilename = splitpath[len(splitpath)-1]
    print(oldfilename)
    newfilename = oldfilename.lower()
    print(newfilename)
    if (newfilename != oldfilename):
        print("-----------------------")
        newpath = path.replace(oldfilename, newfilename)
        os.rename(path, newpath)
'''