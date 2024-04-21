import mysql.connector
import csv

def create_table():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rey@nsh4"
    )

    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS Assessment")

    cursor.execute("USE Assessment")

    cursor.execute("CREATE TABLE IF NOT EXISTS Users ("
                   "id INT AUTO_INCREMENT PRIMARY KEY,"
                   "Full_Name VARCHAR(255),"
                   "Preferred_Language VARCHAR(50),"
                   "Referral_Code VARCHAR(15),"
                   "Zodiac_Sign VARCHAR(50),"
                   "Nakshatra VARCHAR(50),"
                   "Date_of_Birth DATE,"
                   "Email VARCHAR(255),"
                   "Location VARCHAR(255),"
                   "Gender CHAR(1) CHECK (Gender IN ('M', 'F'))"
                   ")")

    cursor.close()
    connection.close()

def import_data_from_csv(file_path):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rey@nsh4",
        database="Assessment"
    )

    cursor = connection.cursor()

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            dob_parts = row[5].split('-')
            dob = f"{dob_parts[2]}-{dob_parts[1]}-{dob_parts[0]}"

            cursor.execute("INSERT INTO Users (Full_Name, Preferred_Language, Referral_Code, Zodiac_Sign, Nakshatra, Date_of_Birth, Email, Location, Gender) "
                           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (row[0], row[1], row[2], row[3], row[4], dob, row[6], row[7], row[8]))

    connection.commit()

    cursor.close()
    connection.close()

def main():
    create_table()
    import_data_from_csv('users.csv')
    print("Created the Users table successfully...!!")

if __name__ == "__main__":
    main()