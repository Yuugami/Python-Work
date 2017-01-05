#!/usr/bin/python3
import cgi, cgitb, sqlite3, sys
cgitb.enable(format="text")
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
firstName = form.getvalue("fName")
lastName = form.getvalue("lName")
course = form.getvalue("courses")
workType = form.getvalue("workType")
grade = form.getvalue("grade")

print("Content-type:text/html\r\n\r\n")
##print ("<html>")
##print ("<head>")
##print ("<title>Hello - Second CGI Program</title>")
##print ("</head>")
##print ("<body>")
##print ("<h2>Name: " + firstName + " " + lastName + "</h2>")
##print ("<h2>Course: " + course + "</h2>")
##print ("<h2>Work Type: " + workType + "</h2>")
##print ("<h2>Grade: " + grade + "</h2>")
##print ("</body>")
##print ("</html>")
indexfile = open("index.html", "r")
htmlDoc = indexfile.read()
print (htmlDoc)
indexfile.close()

def Main():
    try:
        # Open database connection
        con = sqlite3.connect("studentGrades.db")

        # Prepare a cursor to execute queries
        cur = con.cursor()

        # Executing commands and queries
        cur.executescript("""
                    CREATE TABLE IF NOT EXISTS Students (FirstName TEXT, LastName TEXT, Course TEXT, WorkType TEXT, Grade TEXT); """)

        student = (firstName, lastName, course, workType, grade)

        cur.execute("INSERT INTO Students VALUES(?, ?, ?, ?, ?)", student)
        
        con.commit()

        cur.execute('SELECT * FROM Students')

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
