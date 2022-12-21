# Compare Firebase with Cloudinary's photos and return the photos that are missing from Firebase
def DictListUpdate( lis1, lis2):
    lis3 = []
    for aLis1 in lis1:
        if aLis1 not in lis2:
            lis3.append(aLis1)
    return lis3


