import mysql.connector
import csv

def create_database_and_table():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rey@nsh4"
    )

    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS Assessment")

    cursor.execute("USE Assessment")

    cursor.execute("CREATE TABLE IF NOT EXISTS Astrologers ("
                   "id INT AUTO_INCREMENT PRIMARY KEY,"
                   "Name VARCHAR(255),"
                   "Expertise_1 VARCHAR(255),"
                   "Expertise_2 VARCHAR(255),"
                   "Expertise_3 VARCHAR(255),"
                   "Language VARCHAR(255),"
                   "Experience INT NOT NULL,"
                   "Calls INT NOT NULL,"
                   "Ratings INT CHECK (Ratings BETWEEN 1 AND 5),"
                   "PricePerMinute INT NOT NULL,"
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
            cursor.execute("INSERT INTO Astrologers (Name, Expertise_1, Expertise_2, Expertise_3, Language, Experience, Calls, Ratings, PricePerMinute, Gender) "
                           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (row[0], row[1], row[2], row[3], row[4], int(row[5]), int(row[6]), int(row[7]), int(row[8]), row[9]))

    connection.commit()

    cursor.close()
    connection.close()

def main():
    create_database_and_table()
    import_data_from_csv('astrologers.csv')
    print("Database, table, and data imported successfully.")

if __name__ == "__main__":
    main()