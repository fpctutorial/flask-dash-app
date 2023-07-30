# -*- coding: utf-8 -*-
"""
Created on Mon May 22 19:42:00 2023

@author: User
"""

import sqlite3

# Connect to a database (creates a new database if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

def create_table():
    
# Create a table
    table_query = '''
    CREATE TABLE IF NOT EXISTS speed_db (
    
    id INT PRIMARY KEY NOT NULL,
    latitude varchar(150) NOT NULL,
    longitude varchar(150) NOT NULL,
    service_provider varchar(50) NOT NULL,
    effective_type varchar(10) NOT NULL,
    upload varchar(20) NOT NULL,
    download varchar(20) NOT NULL,
    latency varchar(20) NOT NULL,
    jitter varchar(20) NOT NULL,
    date varchar(15) NOT NULL,
    time varchar(15) NOT NULL
      
    )
    '''

    cursor.execute(table_query)

    # Commit the changes and close the connection
    conn.commit()

def instert_intable():
    

    insert_query = '''
    INSERT INTO 'speed_db' ('id', 'latitude', 'longitude', 'service_provider', 'effective_type', 'upload', 'download', 'latency', 'jitter', 'date', 'time')\
        VALUES (?, ?, ?, ?,? ,?, ?, ?, ? , ?,?)
        '''


    data = [
        (1, '8.9831711', '7.5738469', 'Globacom Limited', '3g', '2.21', '1.96', '336.96', '9.85', 'Nov 19th, 2021', '03:21:56pm'),
        (2, '8.9856184', '7.5790668', 'Globacom Limited', '3g', '1.09', '2.63', '593.27', '650.87', 'Nov 19th, 2021', '03:25:41pm'),
        (3, '8.9856184', '7.5790668', 'Globacom Limited', '4g', '3.14', '4.82', '294.20', '10.38', 'Nov 19th, 2021', '03:26:39pm'),
        (4, '4.876902', '6.9536259', 'MTN NIGERIA Communication limited', '4g', '3.84', '5.11', '334.50', '419.10', 'Nov 19th, 2021', '10:12:07pm'),
        (5, '4.876645', '6.9784646', 'MTN NIGERIA Communication limited', '3g', '1.09', '4.74', '339.60', '37.33', 'Nov 19th, 2021', '10:20:52pm'),
        (6, '4.870907', '6.9727576', 'MTN NIGERIA Communication limited', '3g', '5.09', '2.86', '368.57', '731.33', 'Nov 19th, 2021', '10:22:06pm'),
        (7, '4.876645', '6.9784646', 'MTN NIGERIA Communication limited', '3g', '4.93', '5.83', '321.54', '28.12', 'Nov 19th, 2021', '10:22:48pm'),
        (8, '4.877345', '6.9736533', 'MTN NIGERIA Communication limited', '3g', '1.16', '0.42', '337.30', '32.21', 'Nov 19th, 2021', '10:27:47pm'),
        (9, '4.870907', '6.9727576', 'MTN NIGERIA Communication limited', '4g', '3.72', '14.31', '302.00', '10.49', 'Nov 20th, 2021', '11:56:31am'),
        (10, '4.8725207', '6.9724219', 'MTN NIGERIA Communication limited', '3g', '3.42', '14.23', '313.48', '25.55', 'Nov 20th, 2021', '11:57:56am'),
        (11, '4.876645', '6.9784646', 'MTN NIGERIA Communication limited', '4g', '0.60', '4.18', '344.94', '13.30', 'Nov 20th, 2021', '12:01:22pm'),
        (12, '6.4408087', '3.2877617', 'MTN NIGERIA Communication limited', '4g', '5.53', '10.31', '266.90', '9.55', 'Nov 20th, 2021', '11:16:56pm'),
        (13, '6.4408087', '3.2877617', 'MTN NIGERIA Communication limited', '4g', '4.80', '5.94', '263.70', '5.53', 'Nov 20th, 2021', '11:19:11pm'),
        (14, '6.4406408', '3.2870357', 'MTN NIGERIA Communication limited', '3g', '1.28', '1.89', '298.60', '71.66', 'Nov 20th, 2021', '11:22:08pm'),
        (15, '4.8874361', '6.9890863', 'MTN NIGERIA Communication limited', '3g', '0.24', '0.92', '293.28', '158.69', 'Nov 21st, 2021', '06:47:58pm'),
        (16, '4.8934943', '6.9066592', 'MTN NIGERIA Communication limited', '4g', '4.65', '4.94', '313.50', '14.18', 'Nov 23rd, 2021', '01:15:49pm'),
        (17, '4.8934943', '6.9066592', 'MTN NIGERIA Communication limited', '4g', '4.05', '3.34', '291.70', '34.55', 'Nov 23rd, 2021', '01:18:41pm'),
        (18, '6.4392602', '3.285162', 'MTN NIGERIA Communication limited', '3g', '4.68', '0.23', '260.78', '350.14', 'Dec 8th, 2021', '08:37:41pm'),
        (19, '9.0570752', '7.471104', 'Globacom Limited', '4g', '5.35', '3.32', '266.50', '80.94', 'Dec 10th, 2021', '06:10:33pm'),
        (20, '6.4431936', '3.3053742', 'MTN NIGERIA Communication limited', '4g', '5.29', '6.85', '248.40', '14.65', 'Dec 12th, 2021', '07:41:48pm'),
        (21, '4.8709035', '6.9730933', 'MTN NIGERIA Communication limited', '3g', '0.65', '4.82', '302.42', '13.30', 'Dec 12th, 2021', '07:43:25pm'),
        (22, '9.0570752', '7.471104', 'Globacom Limited', '4g', '1.08', '2.01', '347.54', '15.69', 'Dec 12th, 2021', '08:02:41pm'),
        (23, '4.8708861', '6.9747718', 'MTN NIGERIA Communication limited', '4g', '3.08', '12.94', '287.20', '16.44', 'Dec 12th, 2021', '08:29:29pm'),
        (24, '4.8796064', '6.9724219', 'MTN NIGERIA Communication limited', '4g', '4.42', '1.91', '280.14', '23.63', 'Dec 12th, 2021', '08:31:24pm'),
        (25, '4.8773274', '6.9747718', 'MTN NIGERIA Communication limited', '4g', '3.12', '2.93', '283.10', '25.63', 'Dec 12th, 2021', '08:32:13pm'),
        (26, '4.8773274', '6.9747718', 'MTN NIGERIA Communication limited', '4g', '1.35', '2.26', '281.72', '30.25', 'Dec 12th, 2021', '08:33:13pm'),
        (27, '4.8773274', '6.9747718', 'MTN NIGERIA Communication limited', '4g', '3.71', '2.56', '280.64', '27.04', 'Dec 12th, 2021', '08:34:05pm'),
        (28, '4.8764064', '6.9704078', 'MTN NIGERIA Communication limited', '4g', '5.33', '14.76', '278.83', '8.34', 'Dec 12th, 2021', '09:50:00pm'),
        (29, '4.8789761', '6.9710792', 'MTN NIGERIA Communication limited', '3g', '1.33', '11.57', '288.87', '16.91', 'Dec 12th, 2021', '09:50:44pm'),
        (30, '4.8764064', '6.9704078', 'MTN NIGERIA Communication limited', '3g', '1.43', '13.27', '266.46', '14.14', 'Dec 12th, 2021', '09:51:32pm'),
        (31, '6.1191548', '6.7977593', 'MTN NIGERIA Communication limited', '4g', '5.86', '28.85', '260.43', '7.40', 'Dec 23rd, 2021', '02:11:19pm'),
        (32, '6.1191548', '6.7977593', 'MTN NIGERIA Communication limited', '4g', '5.81', '9.01', '269.91', '12.65', 'Dec 23rd, 2021', '02:13:33pm'),
        (33, '6.1191548', '6.7977593', 'MTN NIGERIA Communication limited', '4g', '5.79', '21.55', '266.60', '3.59', 'Dec 23rd, 2021', '02:14:31pm'),
        (34, '6.1191506', '6.7980941', 'MTN NIGERIA Communication limited', '4g', '6.19', '22.47', '256.90', '7.97', 'Dec 26th, 2021', '02:43:51am'),
        (35, '6.1191506', '6.7980941', 'MTN NIGERIA Communication limited', '4g', '6.23', '34.84', '253.90', '27.60', 'Dec 26th, 2021', '02:44:34am'),
        (36, '6.1181335', '6.8004377', 'MTN NIGERIA Communication limited', '3g', '6.18', '27.62', '262.59', '8.34', 'Dec 26th, 2021', '02:47:32am'),
        (37, '6.1181335', '6.8004377', 'MTN NIGERIA Communication limited', '4g', '4.46', '23.70', '258.21', '2.51', 'Dec 26th, 2021', '02:52:02am'),
        (38, '6.1181335', '6.8004377', 'MTN NIGERIA Communication limited', '4g', '6.16', '24.80', '260.40', '11.54', 'Dec 26th, 2021', '02:52:40am'),
        (39, '7.4508174', '3.9159807', 'MTN NIGERIA Communication limited', '3g', '5.04', '5.07', '297.71', '58.47', 'Jan 9th, 2022', '08:54:35pm'),
        (40, '6.4406511', '3.2871302', 'MTN NIGERIA Communication limited', '4g', '5.08', '24.94', '304.29', '9.55', 'Jan 9th, 2022', '11:44:21pm'),
        (41, '6.1189282', '6.7993045', 'MTN NIGERIA Communication limited', '3g', '2.80', '10.14', '307.32', '23.17', 'Jan 10th, 2022', '02:22:26am'),
        (42, '6.1197962', '6.7990985', 'MTN NIGERIA Communication limited', '3g', '1.86', '5.42', '317.67', '1.23', 'Jan 10th, 2022', '02:24:47am'),
        (43, '7.4525072', '3.9156623', 'MTN NIGERIA Communication limited', '3g', '5.38', '1.54', '261.90', '1532.83', 'Jan 10th, 2022', '11:13:36pm'),
        (44, '7.4525072', '3.9156623', 'MTN NIGERIA Communication limited', '3g', '5.22', '1.05', '265.64', '53.42', 'Jan 10th, 2022', '11:14:51pm'),
        (45, '6.2388202', '6.702336', 'MTN NIGERIA Communication limited', '3g', '0.01', '0.54', '265.00', '19.55', 'Jan 12th, 2022', '12:10:56pm'),
        (46, '6.2388751', '6.7022428', 'MTN NIGERIA Communication limited', '3g', '4.88', '0.89', '1147.83', '2816.73', 'Jan 12th, 2022', '12:16:37pm'),
        (47, '6.225192', '6.671998', 'MTN NIGERIA Communication limited', '3g', '0.30', '1.45', '278.50', '99.05', 'Jan 12th, 2022', '12:48:26pm'),
        (48, '6.2263078', '6.6619744', 'Opera Software AS', '4g', '7.79', '0.07', '1026.50', '6812.85', 'Jan 12th, 2022', '04:29:44pm'),
        (49, '6.2270144', '6.6627523', 'Opera Software AS', '4g', '5.46', '0.23', '1095.76', '944.22', 'Jan 12th, 2022', '04:56:20pm'),
        (50, '6.2265194', '6.6700189', 'Opera Software AS', '4g', '16.09', '0.08', '1039.78', '1513.90', 'Jan 12th, 2022', '05:23:38pm'),
        (51, '4.9588359', '7.0045122', 'MTN NIGERIA Communication limited', '3g', '1.65', '2.61', '309.50', '24.91', 'Jan 12th, 2022', '05:48:34pm'),
        (52, '6.0815838', '6.9566985', 'Opera Software Americas LLC', '4g', '0.48', '0.00', '1265.16', '881.50', 'Jan 13th, 2022', '08:19:49am'),
        (53, '6.4406511', '3.2871302', 'MTN NIGERIA Communication limited', '4g', '3.62', '2.50', '284.70', '138.01', 'Jan 19th, 2022', '10:22:36pm'),
        (54, '4.8941007', '6.9103482', 'MTN NIGERIA Communication limited', '4g', '5.16', '3.87', '301.69', '14.85', 'Jan 20th, 2022', '02:07:46pm'),
        (55, '6.4406409', '3.2868204', 'MTN NIGERIA Communication limited', '4g', '3.53', '4.93', '254.74', '12.14', 'Jan 21st, 2022', '12:35:35am'),
        (56, '4.8884374', '6.9905518', 'MTN NIGERIA Communication limited', '3g', '0.65', '2.21', '311.63', '71.00', 'Jan 28th, 2022', '03:35:33pm'),
        (57, '4.8884374', '6.9905518', 'MTN NIGERIA Communication limited', '3g', '0.72', '2.06', '301.16', '28.29', 'Jan 28th, 2022', '03:36:36pm'),
        (58, '4.7732597', '7.0194355', 'MTN NIGERIA Communication limited', '3g', '1.06', '0.21', '323.38', '49.21', 'Jan 31st, 2022', '01:45:31pm'),
        (59, '4.7732597', '7.0194355', 'MTN NIGERIA Communication limited', '3g', '1.34', '1.49', '332.79', '110.00', 'Jan 31st, 2022', '01:46:36pm'),
        (60, '9.0570752', '7.4481664', 'M247 Ltd', '3g', '1.70', '8.08', '290.90', '48.35', 'Feb 1st, 2022', '02:29:21pm'),
        (61, '6.2059385', '6.7205996', 'MTN NIGERIA Communication limited', '3g', '2.05', '5.49', '274.18', '4.13', 'Feb 1st, 2022', '07:55:18pm'),
        (62, '4.8734973', '6.9714148', 'MTN NIGERIA Communication limited', '4g', '3.19', '8.02', '310.19', '29.85', 'Feb 2nd, 2022', '02:29:52am'),
        (63, '4.8773031', '6.9771218', 'MTN NIGERIA Communication limited', '4g', '1.20', '23.39', '300.81', '29.42', 'Feb 2nd, 2022', '02:30:53am'),
        (64, '4.8773031', '6.9771218', 'MTN NIGERIA Communication limited', '4g', '1.07', '23.61', '292.71', '10.68', 'Feb 2nd, 2022', '02:35:44am'),
        (65, '4.8702455', '6.9744361', 'MTN NIGERIA Communication limited', '4g', '3.15', '9.93', '293.52', '8.66', 'Feb 2nd, 2022', '02:40:31am'),
        (66, '4.8773031', '6.9771218', 'MTN NIGERIA Communication limited', '4g', '2.57', '1.42', '290.26', '2071.88', 'Feb 2nd, 2022', '02:42:15am'),
        (67, '4.8796064', '6.9724219', 'MTN NIGERIA Communication limited', '4g', '5.15', '6.28', '283.50', '26.82', 'Feb 2nd, 2022', '02:42:58am'),
        (68, '6.2059541', '6.7205496', 'Airtel Networks Limited', '4g', '0.80', '0.81', '306.01', '627.93', 'Feb 2nd, 2022', '04:26:00pm'),
        (69, '6.2060554', '6.7201491', 'MTN NIGERIA Communication limited', '3g', '0.00', '1.05', '263.40', '354.11', 'Feb 2nd, 2022', '04:35:44pm'),
        (70, '6.2060554', '6.7201491', 'Airtel Networks Limited', '3g', '0.09', '0.25', '441.60', '16640.39', 'Feb 2nd, 2022', '04:51:36pm'),
        (71, '6.2060554', '6.7201491', 'MTN NIGERIA Communication limited', '3g', '0.26', '0.06', '262.80', '6.31', 'Feb 2nd, 2022', '04:54:14pm'),
        (72, '6.2060554', '6.7201491', 'Airtel Networks Limited', 'slow-2g', '0.08', '0.00', '456.70', '113.53', 'Feb 2nd, 2022', '08:37:31pm'),
        (73, '6.2060554', '6.7201491', 'MTN NIGERIA Communication limited', '3g', '0.07', '0.00', '292.02', '33.54', 'Feb 3rd, 2022', '08:56:14am'),
        (74, '6.2115368', '6.7087645', 'Airtel Networks Limited', 'slow-2g', '0.53', '1.79', '290.64', '22.55', 'Feb 3rd, 2022', '09:10:03am'),
        (75, '4.8931974', '6.9169069', 'MTN NIGERIA Communication limited', '3g', '0.22', '1.46', '302.76', '13.65', 'Feb 3rd, 2022', '01:43:22pm'),
        (76, '6.2115368', '6.7087645', 'Airtel Networks Limited', '2g', '0.05', '0.08', '445.90', '2357.99', 'Feb 4th, 2022', '07:52:51am'),
        (77, '6.2115368', '6.7087645', 'MTN NIGERIA Communication limited', '3g', '0.14', '1.12', '267.00', '17.29', 'Feb 4th, 2022', '07:55:33am'),
        (78, '6.2115368', '6.7087645', 'Airtel Networks Limited', '3g', '0.17', '0.47', '394.69', '11.57', 'Feb 4th, 2022', '07:59:24am'),
        (79, '6.2115368', '6.7087645', 'MTN NIGERIA Communication limited', '2g', '0.06', '2.47', '330.16', '129.89', 'Feb 4th, 2022', '08:02:15am'),
        (80, '6.2115368', '6.7087645', 'Airtel Networks Limited', 'slow-2g', '0.11', '0.01', '319.20', '147.91', 'Feb 4th, 2022', '08:21:46am'),
        (81, '6.2115368', '6.7087645', 'MTN NIGERIA Communication limited', '3g', '0.78', '0.70', '272.10', '27.66', 'Feb 4th, 2022', '08:24:56am'),
        (82, '6.2115368', '6.7087645', 'MTN NIGERIA Communication limited', '3g', '0.04', '1.05', '310.70', '567.02', 'Feb 4th, 2022', '08:36:07am'),
        (83, '6.206582', '6.68336', 'MTN NIGERIA Communication limited', '3g', '5.05', '5.47', '255.40', '12.29', 'Feb 4th, 2022', '10:51:57am'),
        (84, '6.2115368', '6.7087645', 'MTN NIGERIA Communication limited', '2g', '0.54', '3.08', '551.90', '375.07', 'Feb 4th, 2022', '11:14:39am'),
        (85, '6.2069118', '6.68336', 'MTN NIGERIA Communication limited', '3g', '5.51', '6.01', '264.12', '6.89', 'Feb 4th, 2022', '11:19:22am'),
        (86, '6.2069118', '6.68336', 'MTN NIGERIA Communication limited', '3g', '2.59', '1.24', '270.40', '5.61', 'Feb 4th, 2022', '11:26:21am'),
        (87, '6.2115368', '6.7087645', 'MTN NIGERIA Communication limited', '3g', '0.53', '0.46', '515.61', '366.37', 'Feb 4th, 2022', '11:35:42am'),
        (88, '6.2115368', '6.7087645', 'Airtel Networks Limited', '3g', '0.70', '0.21', '429.40', '46.24', 'Feb 4th, 2022', '11:59:03am'),
        (89, '6.2115368', '6.7087645', 'MTN NIGERIA Communication limited', '3g', '0.46', '5.40', '286.18', '631.79', 'Feb 4th, 2022', '12:02:22pm'),
        (90, '6.2060096', '6.7205278', 'MTN NIGERIA Communication limited', '3g', '1.90', '0.63', '273.74', '11.79', 'Feb 4th, 2022', '12:26:02pm'),
        (91, '6.2060096', '6.7205278', 'Airtel Networks Limited', '4g', '1.97', '0.14', '412.20', '14.85', 'Feb 4th, 2022', '12:29:39pm'),
        (92, '6.2060878', '6.7204479', 'Airtel Networks Limited', '3g', '1.80', '0.11', '407.70', '11.98', 'Feb 4th, 2022', '12:38:00pm'),
        (93, '6.2060878', '6.7204479', 'MTN NIGERIA Communication limited', '2g', '0.54', '0.52', '873.47', '530.82', 'Feb 4th, 2022', '12:39:52pm'),
        (94, '6.2060878', '6.7204479', 'Airtel Networks Limited', '4g', '2.46', '2.07', '280.50', '12.66', 'Feb 4th, 2022', '12:42:27pm'),
        (95, '6.2173532', '6.6948433', 'MTN NIGERIA Communication limited', '4g', '5.03', '0.43', '276.76', '34.93', 'Feb 4th, 2022', '02:35:52pm'),
        (96, '6.2060878', '6.7204479', 'Airtel Networks Limited', 'slow-2g', '0.05', '0.18', '434.84', '160.36', 'Feb 4th, 2022', '02:36:23pm'),
        (97, '6.2061134', '6.7204674', 'MTN NIGERIA Communication limited', '2g', '0.05', '1.09', '677.00', '432.18', 'Feb 4th, 2022', '02:54:21pm'),
        (98, '6.2061134', '6.7204674', 'MTN NIGERIA Communication limited', 'slow-2g', '0.06', '0.45', '515.95', '335.17', 'Feb 4th, 2022', '03:24:41pm'),
        (99, '6.2061134', '6.7204674', 'Airtel Networks Limited', '2g', '0.31', '0.78', '407.86', '31.22', 'Feb 4th, 2022', '03:32:54pm'),
        (100, '6.2061134', '6.7204674', 'Airtel Networks Limited', '3g', '0.94', '0.29', '1323.29', '3597.19', 'Feb 4th, 2022', '03:38:53pm'),
        (101, '6.2151049', '6.7029266', 'MTN NIGERIA Communication limited', '4g', '4.07', '0.87', '418.28', '258.01', 'Feb 4th, 2022', '03:39:59pm'),
        (102, '6.2061134', '6.7204674', 'MTN NIGERIA Communication limited', '3g', '0.15', '0.71', '327.00', '166.42', 'Feb 4th, 2022', '03:41:28pm'),
        ]

    cursor.executemany(insert_query, data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def fetch_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Fetch the column names from the database
    cursor.execute("SELECT name FROM pragma_table_info('speed_db')")
    results = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Extract the column names from the fetched results
    column_names = [result[0] for result in results]


    # Specify the desired columns to select
    selected_columns = ['longitude', 'latitude', 'upload', 'download', 'latency', 'jitter', 'service_provider']

    # Filter the column names based on the selected columns
    filtered_columns = [column for column in column_names if column in selected_columns]
    
    print(filtered_columns)
    
fetch_data()

def select_long_lat():
    # Connect to the SQLite database
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

# Execute the SELECT query
    service_provider_value = 'Globacom Limited'
    query = f"SELECT latitude, longitude FROM speed_db WHERE service_provider = ?"
    cursor.execute(query, (service_provider_value,))

# Fetch all the selected rows
    rows = cursor.fetchall()

# Iterate over the rows and print latitude and longitude values
    for row in rows:
        latitude, longitude = row
        print("Latitude:", latitude)
        print("Longitude:", longitude)
        print()

# Close the database connection
    cursor.close()
    conn.close()
    
select_long_lat()