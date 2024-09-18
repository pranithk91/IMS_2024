import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="193.203.184.152",
        port='3306',
        user="u885517842_AdminUser",
        password="MdP@ssword!!1",
        database="u885517842_MedicalStore"
    )

    query2 = 'Drop table MedicineList;'
    query3 = """CREATE TABLE MedicineList (
  MId varchar(255) DEFAULT NULL,
  MName varchar(255) DEFAULT NULL,
  MCompany varchar(255) DEFAULT NULL,
  CurrentStock int(11) DEFAULT NULL,
  MType varchar(255) DEFAULT NULL,
  MRP decimal(10,0) DEFAULT NULL,
  PTR decimal(10,0) DEFAULT NULL,
  GST int(11) DEFAULT NULL,
  HSN varchar(255) DEFAULT NULL,
  Offer1 int(11) DEFAULT NULL,
  Offer2 int(11) DEFAULT NULL,
  Weight varchar(255) DEFAULT NULL,
  Composition varchar(255) DEFAULT NULL,
  Alternative varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;"""    
    record = ('RLG11999','2024-06-27','Sri Jaya Krishna Medical Agencies',5426,'1',5,'1','','','NULL','','')                                      
    if conn.is_connected():
        print("Connected to MySQL database")
        cursor = conn.cursor()
        cursor.execute(query2, multi= True)

        #print(f"Line {line_number}: {word_count} words")
        
        # You can do more processing here
        # For example, print lines with more than 10 words

        
        
        #results = cursor.fetchall()
        
        #for row in results:
            #print(row)

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")