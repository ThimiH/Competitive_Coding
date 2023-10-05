def TowersOfHanoi(Disks, From, To, Using):
    if Disks == 1:
        print("Moving ring 1 from " +From +" to " +To)
    else:
        TowersOfHanoi(Disks-1, From, Using, To)
        print("Moving ring " + str(Disks) + " from " +From +" to " +To)
        TowersOfHanoi(Disks-1, Using, To, From)

