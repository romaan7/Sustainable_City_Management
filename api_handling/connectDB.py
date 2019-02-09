import psycopg2

def postgres_test():
        conn = psycopg2.connect("dbname='RAW_DATA' user='myuser' host='35.166.92.45' password='mypassword' connect_timeout=1 ")
        conn.close()
        return True
print("ROMAN")
print(postgres_test())

