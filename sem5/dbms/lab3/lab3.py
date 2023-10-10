import mysql.connector as mycon

# Establish database connection
db = mycon.connect(
    host="localhost",
    user="root",
    password="Vijisrini$@1"
)
cursor = db.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS blood_bank")
cursor.execute("USE blood_bank")

# Create the blood_donor table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS blood_donor (
        Donor_id INT AUTO_INCREMENT PRIMARY KEY,
        Aadhaar_Number VARCHAR(12) UNIQUE,
        Name VARCHAR(100),
        Blood_group VARCHAR(7),
        Region VARCHAR(50),
        Phone_number VARCHAR(15)
    )
""")

def insert_donor(details):
    sql = "INSERT INTO blood_donor (Aadhaar_Number, Name, Blood_group, Region, Phone_number) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, details)
    db.commit()
    print("Donor information inserted successfully!")

def display_donor(region, blood_group):
    sql = "SELECT * FROM blood_donor WHERE Region = %s AND Blood_group = %s"
    cursor.execute(sql, (region, blood_group))
    results = cursor.fetchall()
    for row in results:
        print(row)

def update_donor_details(donor_id, new_phone_number, new_region):
    sql = "UPDATE blood_donor SET Phone_number = %s, Region = %s WHERE Donor_id = %s"
    cursor.execute(sql, (new_phone_number, new_region, donor_id))
    db.commit()
    print("Donor details updated successfully!")

def deregister_donor(donor_id):
    sql = "DELETE FROM blood_donor WHERE Donor_id = %s"
    cursor.execute(sql, (donor_id,))
    db.commit()
    print("Donor information removed successfully!")

def main_menu():
    print("Blood Bank Information System")
    print("1. Insert Donor Information")
    print("2. Display Donors by Region and Blood Group")
    print("3. Update Donor Details")
    print("4. Deregister Donor")
    print("5. Exit")

while True:
    main_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        aadhaar = input("Enter Aadhaar Number: ")
        name = input("Enter Name: ")
        blood_group = input("Enter Blood Group: ")
        region = input("Enter Region: ")
        phone_number = input("Enter Phone Number: ")
        insert_donor((aadhaar, name, blood_group, region, phone_number))

    elif choice == "2":
        region = input("Enter Region: ")
        blood_group = input("Enter Blood Group: ")
        display_donor(region, blood_group)

    elif choice == "3":
        donor_id = input("Enter Donor ID: ")
        new_phone_number = input("Enter New Phone Number: ")
        new_region = input("Enter New Region: ")
        update_donor_details(donor_id, new_phone_number, new_region)

    elif choice == "4":
        donor_id = input("Enter Donor ID: ")
        deregister_donor(donor_id)

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please select again.")

cursor.close()
db.close()
