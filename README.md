Hotel Project KHU

A hotel reservation system written in Python – the final project for Kharazmi University (KHU).

## 📖 About the Project

This project is a hotel reservation system implemented entirely as a Command-Line Interface (CLI).
Users can register, log in, view and filter different rooms, make reservations, and cancel them.
All user information, account balances, and reservation data are stored in plain text files.

## ✨ Features

- **User Registration & Login** – Each user registers with a username and password and receives an initial balance of **3,000,000 IRR**.
- **Authentication** – Login validates usernames and passwords against the `account.txt` file.
- **Account Balance Management** – View balance, recharge the account, and automatically deduct the room price upon successful booking.
- **8 Deafault Room Types** with varying amenities, capacities, and prices:

| Room No. | Room Type        | Price (Million IRR) | Capacity | Amenities                                  |
|----------|------------------|---------------------|----------|--------------------------------------------|
| 1        | 1-Bed            | 0.5                 | 1        | Refrigerator                               |
| 2        | 2-Bed            | 1.0                 | 2        | TV, Refrigerator                           |
| 3        | Suite            | 1.7                 | 4        | Refrigerator, TV, Sofa                     |
| 4        | Luxury Suite     | 2.5                 | 3        | Refrigerator, TV, Sofa, Jacuzzi            |
| 5        | Family Room      | 2.0                 | 5        | Refrigerator, TV, Kitchenette              |
| 6        | Economy Room     | 0.3                 | 1        | Fan                                        |
| 7        | VIP Suite        | 3.5                 | 4        | Refrigerator, TV, Sofa, Jacuzzi, Balcony   |
| 8        | Conference Room  | 5.0                 | 20       | Projector, Sound System, WiFi              |

- **Display and Filter Rooms** – Filter by type, price range, and specific amenities.
- **Room Availability Check** – Enter check-in and check-out dates to see which rooms are available during that period.
- **Room Reservation** – Confirm room availability and sufficient account balance before booking.
- **View User Reservations** – Display both active and past reservations for the logged-in user.
- **Cancel Reservations** – If canceled **more than 48 hours** before check-in, **100%** of the amount is refunded; otherwise, **50%** is refunded.
- **Recharge Account** – Users can top up their balance at any time.

## 🚀 How to Run

### Prerequisites
- Python 3.6 or higher

### Steps
```bash
# Clone the repository
git clone https://github.com/Mrtaha20066/Hotel-Project-KHU.git
cd Hotel-Project-KHU

# Run the application
python hotel.py
```

## 📂 File Structure

```
Hotel-Project-KHU/
├── hotel.py           # Main application file
├── account.txt        # User account data (auto-generated)
└── reservations.txt   # Reservation records (auto-generated)
```

## 🎮 User Guide

Once you run the program, follow these steps:

1. **Register** – Enter a new username and password.
2. **Login** – Use your registered username and password to access the system.
3. **View Room List** – All available rooms with their details will be displayed.
4. **Choose an action** from the main menu:

| Option | Action                    |
|--------|---------------------------|
| 1      | Filter rooms              |
| 2      | Check availability & book |
| 3      | View my reservations      |
| 4      | Cancel a reservation      |
| 5      | Recharge account          |
| 6      | Exit                      |

### How to Filter Rooms
- **By Type**: e.g., `1 Takhteh`, `2 Takhteh`, `Suite`, etc.
- **By Price**: Enter a range (e.g., from 0.5 to 2.0).
- **By Amenities**: e.g., `TV`, `Refrigerator`, `WiFi`, etc.

### How to Make a Reservation
- Enter the **check-in** and **check-out** dates in `YYYY-MM-DD` format.
- Select the room number from the list of available rooms.
- Enter the number of guests (must not exceed the room's capacity).

## 👨‍💻 Author

**Taha Alizadeh** – Final project for the Advanced Programming course at Kharazmi University (KHU) – under the supervision of DR.Najafi.

> **Note:** Any copying or unauthorized use of this code requires explicit permission from the author.

---

## 🔧 Suggestions for Future Development

This Code is wroted simply and it can be better if you want it for you hotel tell me from tahaalizadeh69@gmail.com so make it personal for you.
like:

Replace text files with a proper database (e.g., SQLite).

Add a Graphical User Interface (GUI) using Tkinter or PyQt.

Implement an admin panel to manage rooms (add/remove/modify).

Store a transaction history for each user.

Introduce different user roles (Admin, Regular User, Manager).

THANK YOU FOR YOUR ATTENTION.
