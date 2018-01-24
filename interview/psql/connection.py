import psycopg2

theConnection = psycopg2.connect(database="postgres", user="postgres")

print "Connection successful"
