class house:

    total_house = 0

    def __init__(self,floors,doors,windows,color="white",has_garage=False,address=""):
        self.floors = floors
        self.doors = doors
        self.windows = windows
        self.color = color
        self.has_garage = has_garage
        self.address = address

        #increment house
        house.total_house += 1

    def displayinfo(self):
        print("house information: ")
        print(f"there is {self.floors} floors")
        print(f"there is {'garage is available' if self.has_garage else 'garage is not avail'}")
        print(f"the color is {self.color}")
        print(f"the address is {self.address}")

    @classmethod
    def display_total_house(cls):
        print(f'there is {cls.total_house} house')


    @staticmethod
    def validate_house(self):
        changecolor = input("Enter 'y' if you want to change the color of the house 'n' if no ")
        if changecolor == 'y':
            validatecolor = input("enter the color ")
            self.color = validatecolor
            return self.color
        else:
            print("ok")
        addgarage = input("Enter 'y' if you want to add a garage 'n' if no ")
        if addgarage == 'y' and not self.has_garage:
            self.has_garage = True
            return self.has_garage
        else:
            print("ok")
        changeaddress = input("Enter 'y' if you want to change the address of the house 'n' if no ")
        if changeaddress == 'y':
            validateaddress = input("enter the address ")
            self.address = validateaddress
            return self.address
        else:
            print("ok")



house1 = house(floors=2,doors=4,windows=6,color="pink",has_garage=False,address="123 main")



house1.display_total_house()

house1.displayinfo()
house1.validate_house(house1)
house1.displayinfo()

