'''
This program is wroted by Taha Alizadeh
It is for end term project for Mr.Najafi in Kharazmi University
ANY COPY AND USING MUST ASK PERMISSION FROM TAHA ALIZADEH

'''
#importing class that we need
from datetime import datetime
import os

#For working in any device
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ACCOUNT_FILE = os.path.join(BASE_DIR, "account.txt")
RESERVATION_FILE = os.path.join(BASE_DIR, "reservations.txt")

#Account class
class Account:
    #Sign up
    def signup(self):
        #Take Username
        while True:
            user = input("Enter your username: ").strip()

            #Dont fill blank
            if user == (""):
                print("Please fill blank")
            else:
                break

        #Take Password
        while True:
            password = input("Enter your password: ").strip()

            #Dont fill blank
            if password == (""):
                print("Please fill blank")
            else:
                break
        
        #define initial credit
        initial_credit = 3.0

        #Save it in file
        x = f"{user}*{password}*{initial_credit}\n"
        with open(ACCOUNT_FILE, "a+") as file:
            file.seek(0)
            
            #check it if they signed in before or not
            lines = file.readlines()
            if x not in lines:
                file.write(x)
            else:
                print("-" * 30)
                print("You signed in Before")
                print("-" * 30)

    #login
    def identify(self):
        #Take username for login
        while True:
            userv = input("Enter Your Username: ").strip()

            #Dont fill blank
            if userv == (""):
                print("Please fill blank")
                continue
            break
        
        #Take password for login
        while True:
            passwordv = input("Enter Your Password: ").strip()

            #Dont fill blank
            if passwordv == (""):
                print("Please fill blank")
                continue

            #checking the user and password is true
            f = userv + "*" + passwordv + "\n"
            with open(ACCOUNT_FILE, "r") as file:
                lines = file.readlines()
                found = False
                for line in lines:
                    parts = line.strip().split("*")
                    if len(parts) >= 2:
                        if parts[0] == userv and parts[1] == passwordv:
                            print("Welcome To Hotel Tehran")
                            return userv

                #error for writing wrong user or password    
                if not found:
                    print("username or password is wrong")
                    return None

    #show credit that you have
    def get_credit(self , username):
        try:
            #reading from file
            with open(ACCOUNT_FILE, "r") as file:
                for line in file:
                    part = line.strip().split("*")
                    if part[0] == username:
                        return float(part[2])
        #if didnt find the user return 0.0
        except FileNotFoundError:
            return 0.0
        return 0.0
    
    #updating credit after add amount or reserve
    def update_credit(self , username , amount):
        update_lines = []
        #find amount in file
        if os.path.exists(ACCOUNT_FILE):
            with open(ACCOUNT_FILE, "r") as f:
                lines = f.readlines()

            #replace new amount
            for line in lines:
                parts = line.strip().split("*")
                if parts[0] == username:
                    new_balance = float(parts[2]) - amount
                    update_lines.append(f"{parts[0]}*{parts[1]}*{new_balance}\n")
                #append if didnt find user
                else:
                    update_lines.append(line)

            with open(ACCOUNT_FILE, "w") as file:
                file.writelines(update_lines)

    #Charge credit of account
    def charge_credit(self, username):
        try:
            #get number of amount from user
            amount = float(input("Enter the amount(milion) that you want to add to your credit: "))
            #check that is positive or not
            if amount <= 0:
                print("Please enter positive amount")
                return
            
            #update and add amount to credit
            self.update_credit(username, -amount)

            print(f"{amount} milion added to your account successfully")
            print(f"your new balance is {self.get_credit(username)} milion")
        except ValueError:
            print("Invalid input , please enter number")

#Hotel class
class Hotel:
    #Room list
    def __init__(self):
        self.Room = {
            "1": {
                "Type": "1 Takhteh",
                "Price": 0.5,
                "Facilities": ["Refrigerator"],
                "Capacity": 1
            },
            "2": {
                "Type": "2 Takhteh",
                "Price": 1.0,
                "Facilities": ["TV", "Refrigerator"],
                "Capacity": 2
            },
            "3": {
                "Type": "Suite",
                "Price": 1.7,
                "Facilities": ["Refrigerator", "TV", "Sofa"],
                "Capacity": 4
            },
            "4": {
                "Type": "Luxury Suite",
                "Price": 2.5,
                "Facilities": ["Refrigerator", "TV", "Sofa", "Jacuzzi"],
                "Capacity": 3
            },
            "5": {
                "Type": "Family Room",
                "Price": 2.0,
                "Facilities": ["Refrigerator", "TV", "Kitchenette"],
                "Capacity": 5
            },
            "6": {
                "Type": "Economy Room",
                "Price": 0.3,
                "Facilities": ["Fan"],
                "Capacity": 1
            },
            "7": {
                "Type": "VIP Suite",
                "Price": 3.5,
                "Facilities": ["Refrigerator", "TV", "Sofa", "Jacuzzi", "Balcony"],
                "Capacity": 4
            },
            "8": {
                "Type": "Conference Room",
                "Price": 5.0,
                "Facilities": ["Projector", "Sound System", "WiFi"],
                "Capacity": 20
            }
        }

    #Showing Room
    def show_room(self, rooms=None):
        if rooms is None:
            rooms = self.Room.items()
        for number, detail in rooms:
            print(f"Room {number}:")
            print(f"  Type       : {detail['Type']}")
            print(f"  Price      : {detail['Price']} million")
            print(f"  Facilities : {', '.join(detail['Facilities'])}")
            print(f"  Capacity   : {detail['Capacity']} person(s)")
            print("-" * 30)

    #Filtring List Of Room
    def filter_rooms(self, room_type=None, min_price=None, max_price=None, facility=None):
        filtered = []
        for number, detail in self.Room.items():
            
            if room_type and detail["Type"] != room_type:
                continue
            
            if min_price and detail["Price"] < min_price:
                continue
            if max_price and detail["Price"] > max_price:
                continue

            if facility and facility not in detail["Facilities"]:
                continue

            filtered.append((number, detail))
        return filtered
    
    #Cheacking Room Availibility
    def check_availability(self, checkin, checkout):
        available_rooms = []
        checkin_date = datetime.strptime(checkin, "%Y-%m-%d")
        checkout_date = datetime.strptime(checkout, "%Y-%m-%d")
        nights = (checkout_date - checkin_date).days
        
        #check reservations from file 
        try:
            with open(RESERVATION_FILE, "r") as file:
                reservations = file.readlines()
        except FileNotFoundError:
            reservations = []

        #listing rooms in that time
        for number, detail in self.Room.items():
            reserved = False
            for res in reservations:
                user, room_no, res_in, res_out, guests, price, status = res.strip().split(" * ")
                if room_no == number:
                    res_in_date = datetime.strptime(res_in, "%Y-%m-%d")
                    res_out_date = datetime.strptime(res_out, "%Y-%m-%d")
                    if not (checkout_date <= res_in_date or checkin_date >= res_out_date):
                        reserved = True
                        break
            if not reserved:
                total_price = detail["Price"] * nights
                available_rooms.append((number, detail, total_price))

        return available_rooms

    #Reserving Room
    def reserve_room(self, username, room_number, checkin, checkout, guests, total_price):
        statue = "active"
        #reserving and saving in file
        reservation_entry = f"{username} * {room_number} * {checkin} * {checkout} * {guests} * {total_price} * {statue}\n"
        with open(RESERVATION_FILE, "a") as file:
            file.write(reservation_entry)
        account.update_credit(username, total_price)

        print(f"Room {room_number} reserved successfully")
        print(f"The total price = {total_price} and your Remaining Credit = {account.get_credit(username)}")

    #showing user reservation
    def show_user_reservation(self, username, only_active=False):
        now = datetime.now()
        #read file to find reserves of user
        if not os.path.exists(RESERVATION_FILE):
            print("no reservation found")
            return

        with open(RESERVATION_FILE, "r") as file:
            lines = file.readlines()

        #show reserves of user
        print(f"\n reservation for {username}")
        for line in lines:
            parts = line.strip().split(" * ")
            res_user, room_no, res_in, res_out, guests, price, status = parts
            
            if res_user == username:
                res_out_date = datetime.strptime(res_out, "%Y-%m-%d")
                if status == "active" and now > res_out_date:
                    status = "completed"

                if only_active and status != "active":
                    continue
                
                print(f"Room : {room_no} , Dates : {res_in} to {res_out} , status : {status} , Paid : {price}")
                found = True

    #Canceling reservation
    def cancel_reservation(self, username):
        update_reservations = []
        refund_amount = 0
        canceled = False
        now = datetime.now()

        #find reserves from file
        try:
            with open(RESERVATION_FILE, "r") as file:
                lines = file.readlines()
            
            #get room number that want to cancel
            room_to_cancel = input("Enter the room number you want to cancel: ")

            #find the room number
            for line in lines :
                parts = line.strip().split(" * ")
                res_user, room_no, res_in, res_out, guests, price, status = parts

                if res_user == username and room_no == room_to_cancel and status == "active":
                    checkin_date = datetime.strptime(res_in, "%Y-%m-%d")
                    total_paid = float(price)

                    hours_diff = (checkin_date - now).total_seconds() / 3600

                    #define that if less than 48h before reserve day refund all
                    if hours_diff > 48:
                        refund_amount = total_paid
                        print("you cancel before 48h of your reserve day and all of your money refund")
                    #define that if less than 48h before reserve day refund 50% of it
                    else:
                        refund_amount = total_paid * 0.5
                        print("you cancel before 48h of your reserve day and %50 of your money refund")

                    #change active to cancel
                    parts[-1] = "canceled"
                    update_reservations.append(" * ".join(parts) + "\n")
                    canceled = True
                else:
                    update_reservations.append(line)

            #add refund amount to account
            if canceled:
                with open(RESERVATION_FILE, "w") as file:
                    file.writelines(update_reservations)
                
                account.update_credit(username, -refund_amount)
                print(f"{refund_amount} milion refund to your account")
            #if write wrong number of active reserve
            else:
                print("active reservation not found or room number is wrong")
        
        except FileNotFoundError:
            print("no reservation found")

#Defining Room Avaibility
def checking():
    while True:
        checkin = input("Enter check-in date (YYYY-MM-DD): ")
        checkout = input("Enter check-out date (YYYY-MM-DD): ")
        if checkin == "" or checkout == "":
            print("Please fill in the blanks")
            continue
        try:
            datetime.strptime(checkin, "%Y-%m-%d")
            datetime.strptime(checkout, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter dates in YYYY-MM-DD format")

    #Checking Room Availblity
    available = hotel.check_availability(checkin, checkout)
    if not available:
        print("No rooms available in this period.")
        return
    else:
        for number, detail, total_price in available:
            print(f"Room {number} ({detail['Type']}) is available.")
            print(f"Facilities: {', '.join(detail['Facilities'])}")
            print(f"Capacity: {detail['Capacity']} person(s)")
            print(f"Total price for stay: {total_price} million")
            print("-" * 30)

    #Reservation Entry And Credit
    while True:
        choice = input("Enter room number to reserve:(if you want cancel proccess just write 'c') ")
        username = current_user
        if choice.lower() == "c":
            break
        elif choice == ("") or username == (""):
            print("please fill the blank")

        #reserve room for user
        selected_room = None
        for room in available:
            if room[0] == choice:
                selected_room = room
                break
        
        if selected_room:
            room_no , detail , total_price = selected_room

            #check credit that is enough or not
            user_credit = account.get_credit(username)
            if user_credit < total_price :
                print("You dont have enough credit")
            else:
                guests = input(f"Enter number of guests (maximum = {detail['Capacity']}): ")
                if guests.isdigit() and int(guests) <= detail['Capacity']:
                    #save reserve room in file
                    hotel.reserve_room(username, choice, checkin, checkout, guests, total_price)
                else:
                    print("Invalid number or guest number is more than maximum")
        else:
            print("The room is not avaiable or the entry is wrong")

#Defining Filtering Room list Input
def FILTER():
    #Asking for what kind of sort they want
    print("you can sort the list by the thing that you want")
    print("Type: 1 Takhteh , 2 Takhteh , Suite")
    print("Price : From 0.5 to 5.0")
    print("Facilities : Refrigerator , TV , Sofa , Jacuzzi , Balcony , Wifi , Sound System , Projector , Fan , Kitchenette")
    Type = input("what type room?(you can dont fill it) ")
    min = input("what min price?(you can dont fill it) ")
    if min == '':
        min = None
    else:
        min = float(min)
    max = input("what max price?(you can dont fill it) ")
    if max == '':
        max = None
    else:
        max = float(max)
    facilitie = input("what facilities do you want?(you can dont fill it) ")
    room = hotel.filter_rooms(room_type = Type , min_price = min , max_price = max , facility = facilitie)
    if not room:
        print("No rooms found with given filters.")
    else:
        hotel.show_room(room)


#Using Class
account = Account()
hotel = Hotel()

#Run Sign in class
print("-" * 30)
print("Please Sign in first to continue")
print("-" * 30)
account.signup()

#Run login class
print("-" * 30)
print("login your account please to countinue")
print("-" * 30)
current_user = account.identify()
#Show list of Hotel Room
hotel.show_room()

#What Do They Want To Do
while True:
    Input = input("What Do You Want To Do?(1-Filtring room , 2-Checking room , 3-My reservation , 4-Canceling reservation , 5-Charge credit , 6-Exit) ")
    if Input == "1" :
        FILTER()
    elif Input == "2" :
        checking()
    elif Input == "3" :
        hotel.show_user_reservation(current_user)
    elif Input == "4" :
        hotel.cancel_reservation(current_user)
    elif Input == "5" :
        account.charge_credit(current_user)
    elif Input == "6" :
        break
    else:
        print("Please Write the true command \n")