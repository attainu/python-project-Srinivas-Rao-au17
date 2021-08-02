from random import randint
 
 
class swiggy():

    def __init__(self):   # created some clss 
        self.cart = {}
        self.curRes = ""
        self.history = {}
        self.totalItems = 0
        self.NameOfRestaurant = {'Naruto Hotel': {"Fish": 125, # made dic of resname and items with thr pricesfor simple cal and and easly acss.
                                               "Noodles": 130,
                                               "Rice": 150},

                                'DBZ Hotel':    {"Soup": 135,
                                                "Rice": 155,
                                                "Roti Sabji": 160},

                                'One Piece InterNation Resort':{"Sushi": 170,
                                                                "Roti": 180,
                                                                "Scamosa": 190}}
        print()
        print("%"*45, "HELLOO WELCOME TO SWIGGY", "%"*45)
        print()
        print("It would be great to know your name ")
        name = input()
        print("Hey", name , "You do looK hungry Let's Get you something to eat ASAP")
        self.mainMenu()

    def mainMenu(self):
        print("")   
        print("!"*35 , "MAIN  MENU", "!"*35)
        print()
        print("SELECT ANY ONE OF THESE AVAILABLE OPTIONS :-")
        print()
        print("(1) ORDER FOOD \n"
              "(2) EXIT \n"
              "(3) ORDER HISTORY \n"
              "(4) RESTAURANT OWNER'S ")
                                             
        while True:
            print()
            NumberForMainManu = int(input("Enter You selection :"))  
            if NumberForMainManu == 1:
                self.renderHotelMenu(NumberForMainManu)
            elif NumberForMainManu == 2:
                print("Thank For using our services, Hope to see you again")
                exit()
            elif NumberForMainManu == 3:
                self.History()
            elif NumberForMainManu == 4:
                self.restaurantside()
            else: 
                print("Invalid input try again")

    def restaurantside (self):
        Enter_pin = input("Enter the pin = ")
        if Enter_pin == "srinivas":              # extra feature added key to acs change the name and all
            for key, value in enumerate(self.NameOfRestaurant):  # here i am taking hotel names
                    print(key+1, ")",     value)
            editRes=int(input("Enter which restaurant you want to edit :"))
            r = 0
            for key, value in self.NameOfRestaurant.items():
                r += 1
                if editRes == r:
                        itemMap = {}
                        cur = 1
                        for key1, value1 in value.items():
                            itemMap[str(cur)] = key1
                            print(cur, ")", key1.ljust(30), value1, "/-")
                            cur += 1  
            
            EditThePrice = int(input("which hotel price you want to change :"))
            r = 0
            for key, value in self.NameOfRestaurant.items():
                r += 1
                if r == editRes:
                    a = 0
                    for key1, value1 in value.items():
                        a += 1
                        if a == EditThePrice:
                            enter_price = int(input("Enter the price you wanna change to = "))
                            self.NameOfRestaurant[key][key1] = enter_price
                            print(self.NameOfRestaurant)
                            self.mainMenu()
        else:
            print("Incorrect Pin")
            self.mainMenu()
 
    def payment(self, amount):
        print()
        print("$"*15, "WELCOME TO THE PAYMENT GATEWAY", "$"*15)
        print()
        print("*"*50)
        print("AMOUNT TO BE PAID FOR YOUR SWIGGY ORDER RS", amount, "/-")
        print("*"*50)
        print("AVAILABLE PAYMENT OPTIONS :-")
        print()
        print(
        "(D) DEBIT CARD / CREDIT CARD \n"
        "(N) NET BANKING \n"
        "(U) UPI \n"
        "(W) WALLETS \n"
        "(A) CASH ON DELIVERY")

        print("="*50)          
        while True: 
            inp = input("Enter your selection: ").upper()
            if inp == "C" or inp == "D" or inp == "N" or inp == "U" or inp == "W":
                print()
                print("PAYMENT SUCCESSFULL")
                print("HURRAY, YOUR ORDER CONFIRMED")
                print()
                print("It'll Take us 30 minutes MaX to deliver")
                print()
                print("(H) ORDER HISTORY (M) MAIN MENU (E) EXIT".ljust(0.2))
                print("="*52)
                self.clearCart()
                while True:
                    inp1 = input("SELECT YOUR OPERATION: ").upper()
                    if inp1 == "M":
                        self.mainMenu()
                        break
                    elif inp1 == 'E':
                        exit()
                    elif inp1 == 'H':
                        self.History()
                        break
                    else:
                        print("INVALID INPUT PLEASE TRY AGAIN")
                print("="*86)
                self.main_menu()
            elif inp == 'A':
                if amount > 499:
                    print("CASH ON DELIVERY IS NOT AVAILABLE FOR ORDERS ABOVE 499")
                    print("TRY AGAIN WITH DIFFERENT OPTIONS")
                else:
                    print()
                    print("PLEASE PAY THE AMOUNT TO THE DELIVERY PARTNER")
                    print("HURRAY, ORDER CONFIRMED")
                    print("It'll Take us 30 minutes MaX to deliver")
                    print("\n (H) ORDER HISTORY    (M) MAIN MENU    (E) EXIT")
                    print("="*55)
                    self.clearCart()
                    while True:
                        inp1 = input("SELECT YOUR OPERATION: ").upper()
                        if inp1 == "M":
                            self.mainMenu()
                            break
                        elif inp1 == 'E':
                            exit()
                        elif inp1 == 'H':
                            self.History()
                        else:
                            print("INVALID INPUT PLEASE TRY AGAIN")
            else:
                print("INVALID INPUT PLEASE TRY AGAIN")

    def showCart(self):
        print()
        print(">"*22, "CART", "<"*22)
        print()
        print("Resturant Selected", ":".ljust(13),self.curRes)
        print()
        total = 0
        print("Items:".ljust(32), "Calculation".ljust(14))
        print()
        print("-"*50)
        print()
        for i in self.cart:
            curtotal = self.cart[i]["Quantity"] * self.cart[i]["Price"]
            total += curtotal
            print(i.ljust(32), self.cart[i]["Quantity"],
                "*", self.cart[i]["Price"], "=", curtotal)
        print()
        print('Total   ---->>>>>>', total, "/-")
        print("="*18, "Main-M", "Pay-P", "="*18)
        while True:
            userInp = input("Enter Your Choice: ")
            userInp = userInp.lower()
            if userInp == "m":
                self.mainMenu()
            if userInp == "p":
                order_no = randint(0,10000)
                self.history[order_no] = [self.curRes, total]
                self.payment(total)

    def clearCart(self):
        self.cart = {}
        self.curRes = ""
        self.totalItems = 0

    def renderHotelMenu(self, NumberForMainManu):
            print("*"*50)
            if NumberForMainManu == 1:
                print("Some Of the best Available Restaurant are :-")
                print()
                for key, value in enumerate(self.NameOfRestaurant):
                    print(key+1, ")",     value) 
                    print()
                print("="*17, "Main-M Cart-C", "="*18)      

            while True:
                hotelMenu = input("Enter your Choice :")
                if(hotelMenu.isnumeric()): 
                    r = 0
                    for key, value in self.NameOfRestaurant.items():
                        r += 1
                        if int(hotelMenu) == r:
                            itemMap = {}
                            cur = 1
                            for key1, value1 in value.items():
                                itemMap[str(cur)] = key1
                                print(cur, ")", key1.ljust(30), value1, "/-")
                                cur += 1
                            print("="*16, "Main-M Cart-C", "="*19)   
                            while True:    
                                selection = input("Enter Your Order :")
                                if(selection.isnumeric()):
                                    if self.curRes == "":
                                        self.curRes = key
                                    else:
                                        if self.curRes != key:
                                            print("Your cart is cleared as you seleceted item from diffrent restaurant")
                                            self.clearCart()
                                    quantity = int(input("How many do you want :"))
                                    if(self.totalItems + quantity > 3):
                                        print("Restaurant cannot process more than 3 Items ") 
                                    else:
                                        if itemMap[selection] in self.cart:
                                            self.cart[itemMap[selection]]["Quantity"] += quantity
                                        else:
                                            self.cart[itemMap[selection]] = {
                                                "Price": self.NameOfRestaurant[key][itemMap[selection]], "Quantity": quantity}
                                        self.totalItems += quantity
                                else:
                                    try:
                                        selection = selection.lower()
                                        if(selection == "c"):
                                            self.showCart()
                                            break
                                        elif(selection == "m"):
                                            self.mainMenu()
                                            break
                                        else:
                                            raise Exception("error")
                                    except:
                                        print("Invalid Input Try Again")   
                else:
                    try:
                        hotelMenu = hotelMenu.lower()
                        if(hotelMenu == "c"):
                            self.showCart()
                            break
                        elif(hotelMenu == "m"):
                            self.mainMenu()
                            break
                        else:
                            raise Exception("error")
                    except:
                        print("Invalid Input Try Again2")  
                             
    def History(self):
            print()
            print(">"*23, "ORDER HISTORY", "<"*23)
            if len(self.history) == 0:
                print("NO ORDERS YET")
                print()
                print("(M) MAIN MENU \n"
                      "(E) EXIT")
                print("="*50)
            else:
                for i in self.history:
                    print("ORDER NUMBER  =", i)
                    print("RESTURANT     =", self.history[i][0]) #name of restaurant 
                    print("ORDER TOTAL   =", self.history[i][1], "/-") # price
                    print("-"*50)
                    print("(M) MAIN MENU \n"
                    "(E) EXIT")
                    print("="*50)
            while True:
                r = input("SELECT A OPERATION: ").upper()
                if r == 'M':
                    self.mainMenu()
                    break
                elif r == 'E':
                    exit()
                else:
                    print("INVALID INPUT TRY AGAIN3")


if __name__ == "__main__":
    swiggy()
