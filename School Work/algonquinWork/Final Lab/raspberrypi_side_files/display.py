#!/usr/bin/python3
import cgi, sqlite3, sys

print("Content-type:text/html\r\n\r\n")
indexfile = open("display.html", "r")
htmlDoc = indexfile.read()
print (htmlDoc)

def Main():
    try:
        # Open database connection
        con = sqlite3.connect("studentGrades.db")

        # Prepare a cursor to execute queries
        cur = con.cursor()

        # Executing commands and queries
        cur.execute('SELECT * FROM Students')
        data = cur.fetchall()
        for row in data:
            print ("<tr>")
            print ("<td>" + row[0] + "</td>")
            print ("<td>" + row[1] + "</td>")
            print ("<td>" + row[2] + "</td>")
            print ("<td>" + row[3] + "</td>")
            print ("<td>" + row[4] + "</td>")
            print ("</tr>")
        print("</table>")
        print("<br>")
        print("<a href='index.html'>Add Another Student</a>")
        print("</body>")
        print("</html>")
        indexfile.close()

    except sqlite3.Error as er:
        if con:
            print("Error! Rolling back!")
            print(er)
            con.rollback()
    finally:
        if con:
            con.close()

            

if __name__ == '__main__':
    Main()
