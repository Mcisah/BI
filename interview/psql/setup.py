import psycopg2
from connection import theConnection


def makeSetup():

    # check if table/relation exists
    def checker(dbcon):
        exists = False
        try:
            cur = dbcon.cursor()
            cur.execute("select exists(SELECT id from BINCOM_TEST)")
            exists = cur.fetchone()[0]
            print exists
            cur.close()
            exists = True
            # print "Table already exists"
        except psycopg2.Error as e:
            print e
            dbcon.rollback()
        return exists

    if checker(theConnection):
        print "Table already exists"
    else:
        cur = theConnection.cursor()
        cur.execute('''CREATE TABLE BINCOM_TEST
        (ID SERIAL PRIMARY KEY,
        COLOUR TEXT,
        FREQ INT);''')

    theConnection.commit()

    print "Table created successfully"

    return theConnection