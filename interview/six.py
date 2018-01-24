# Question 6

"""
    Save the colours and their frequencies in postgresql database.
"""

import psycopg2
from psql.setup import makeSetup
from custom import sortMethod, sortMethod2
from data import dataset


def main():
    pass
    # carryout setup
    conn = makeSetup()
    # get dataSet and set to right format
    data = sortMethod2(sortMethod(dataset()))

    def inserter(dataSet, conn):
        cur = conn.cursor()
        sql = """INSERT INTO bincom_test(colour, freq)
                     VALUES(%s, %s);"""
        for colour in dataSet:
            cur.execute(sql, (colour, str(dataSet[colour])))

        conn.commit()  # commit

        print "Records Created."

        conn.close()  # close connection

    inserter(data, conn)

if __name__ == "__main__":
    main()
