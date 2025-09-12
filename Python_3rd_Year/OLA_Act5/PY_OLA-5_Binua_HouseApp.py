print("Binua, Ralph Gabriel B.")
print("3BSIT-5\n")

class House:
    def __init__(self, floorSize, noOfFloors, noOfDoors):
        self.floorSize = floorSize
        self.noOfFloors = noOfFloors
        self.noOfDoors = noOfDoors

    def lightOpen(self):
        print("The lights are now ON.")

    def ovenOpen(self):
        print("The oven is now ON.")

class Townhouse(House):
    def __init__(self, floorSize, noOfFloors, noOfDoors, noOfWindows):
        super().__init__(floorSize, noOfFloors, noOfDoors)
        self.noOfWindows = noOfWindows

    def switchOn(self):
        self.lightOpen()
        self.ovenOpen()
    pass

ralphTownHouse = Townhouse (floorSize=120, noOfFloors=2, noOfDoors=4, noOfWindows=8)

print(f"Floor Size: {ralphTownHouse.floorSize}")
print(f"No. of Floors: {ralphTownHouse.noOfFloors}")
print(f"No. of Doors: {ralphTownHouse.noOfDoors}")
print(f"No. of Windows: {ralphTownHouse.noOfWindows}")

ralphTownHouse.switchOn()