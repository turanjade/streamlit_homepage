import pandas as pd
import mysql.connector
from mysql.connector import Error
import openai


# Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '21101314',
    'database': 'Ran_Publication'
}


csv_file_path = '/Users/ran/weiyun_sycn/5_Github/learngit/personal_info_database_SQL/citations_20240908.csv'
try:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    #df = df.fillna('')  # Replace NaN with empty string or any other default value
    #print(df.columns)

    ##avoid "" in convert
    def remove_decimal(x):
        if x == '':
            return None  # or a default value, e.g., 0.0
        try:
            # Remove commas if present
            x = str(x).replace(',', '')
            return string(int(float(x)))
        except ValueError:
            return None  # or a default value, e.g., 0.0

    #df['Volume'] = remove_decimal(df['Volume'])
    #df['Number'] = remove_decimal(df['Number'])
    #df['Year'] = remove_decimal(df['Year'])
    # Process DataFrame: Convert numeric columns to VARCHAR and remove decimal points
    df['Volume'] = df['Volume'].apply(lambda x: str(int(float(x))) if pd.notnull(x) else '0')
    df['Number'] = df['Number'].apply(lambda x: str(int(float(x))) if pd.notnull(x) else '0')
    df['Year'] = df['Year'].apply(lambda x: str(int(float(x))) if pd.notnull(x) else '0')
    df['Pages'] = df['Pages'].apply(lambda x: str(x) if pd.notnull(x) else '0')
    print(df[0:5])
    df = df.fillna('')
    print(df['Pages'][0:5])

    # Connect to the MySQL database
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print("Connected to MySQL database")

        # Create a cursor object
        cursor = connection.cursor()

        # Create a table if it doesn't exist
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS PUBLICATION_LIST (
            Authors VARCHAR(255),
            Title VARCHAR(225) PRIMARY KEY,
            Publication TEXT NULL,
            Volume TEXT NULL,
            Number TEXT NULL,
            Pages VARCHAR(225) NULL,
            Year TEXT NULL,
            Publisher TEXT NULL
        );
        '''
        cursor.execute(create_table_query)

        # Insert data from DataFrame into MySQL table
        for index, row in df.iterrows():
            insert_query = '''
            INSERT IGNORE INTO PUBLICATION_LIST (Authors, Title, Publication, Volume, Number, Pages, Year, Publisher)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            '''
            ###ignore existing data with the same primary key

            cursor.execute(insert_query, tuple(row))

        # Commit the changes
        connection.commit()
        print("Data inserted successfully")


    def fetch_data_from_db(query):
        try:
            # Fetch the result
            result = cursor.fetchall()

            # Return the result
            return result if result else None

        except mysql.connector.Error as err:
            return f"Error: {err}"

    ###validate the fetch by priting the result
    def print_in_custom_format(data):
        if data:
            # Example format: Print data in uppercase
            print(f"Retrieved Value: {data[1]}")
            # You can customize this format as needed
        else:
            print("No data found or error retrieving data.")

    #convert each row of records to a string, and return a category
    def format_to_string(row):
        if row:
            #iterate the whole row, and combine all the elements to a full string:
            values = str('--')
            for elements in row:
                values = str(values + '. ' + str(elements))
        else:
            print("No data found or error retrieving data.")
        return(values)
        ####expected to return category of this paper from ChatGPT
    query = "SELECT * FROM PUBLICATION_LIST;"
    data = fetch_data_from_db(query)
    #print_in_custom_format(data)
    #print(format_to_string(data[1]))



except Error as e:
    print(f"Error: {e}")

#finally:
#    # Close the cursor and the connection
#    if connection.is_connected():
#        cursor.close()
#        connection.close()
#        print("MySQL connection closed")


#finally:
    # Close the cursor and the connection
#    if connection.is_connected():
#        cursor.close()
#        connection.close()
#        print("MySQL connection closed")
