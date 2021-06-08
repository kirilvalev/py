import sqlite3
import random
import statistics

# in-memory db, todo check error
connection = sqlite3.connect(":memory:")

# create table
cursor = connection.cursor()
cursor.execute("CREATE TABLE r_data (id integer PRIMARY KEY, value integer)")

# add some random data
for i in range(100):
    cursor.execute("INSERT INTO r_data VALUES ({}, {})".format(i, random.randrange(10000)))

connection.commit()

cursor.execute("SELECT * FROM r_data")

result = cursor.fetchall()

if(len(result) > 0):
        print(type(result[0]))

values = []

for l in result:
        values.append(l[1])

print(values)

print("mean random data: {}".format(sum(values) / len(values)))

print(statistics.mean(values))
print(statistics.median(values))

connection.close()
