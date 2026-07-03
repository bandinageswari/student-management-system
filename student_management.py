import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",  # Change if different
        database="college"
    )

    cursor = conn.cursor()

    while True:
        print("\n" + "=" * 40)
        print("     STUDENT MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                sid = int(input("Enter ID: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))

                cursor.execute(
                    "INSERT INTO student(id,name,age) VALUES(%s,%s,%s)",
                    (sid, name, age)
                )

                conn.commit()
                print("✅ Student Added Successfully!")

            elif choice == 2:
                cursor.execute("SELECT * FROM student")
                students = cursor.fetchall()

                print("\nID\tName\t\tAge")
                print("-" * 30)

                for s in students:
                    print(f"{s[0]}\t{s[1]}\t\t{s[2]}")

            elif choice == 3:
                sid = int(input("Enter Student ID: "))

                cursor.execute(
                    "SELECT * FROM student WHERE id=%s",
                    (sid,)
                )

                student = cursor.fetchone()

                if student:
                    print("\nStudent Found")
                    print(f"ID   : {student[0]}")
                    print(f"Name : {student[1]}")
                    print(f"Age  : {student[2]}")
                else:
                    print("❌ Student Not Found")

            elif choice == 4:
                sid = int(input("Enter Student ID: "))
                new_age = int(input("Enter New Age: "))

                cursor.execute(
                    "UPDATE student SET age=%s WHERE id=%s",
                    (new_age, sid)
                )

                conn.commit()

                if cursor.rowcount > 0:
                    print("✅ Student Updated!")
                else:
                    print("❌ Student ID Not Found")

            elif choice == 5:
                sid = int(input("Enter Student ID: "))

                cursor.execute(
                    "DELETE FROM student WHERE id=%s",
                    (sid,)
                )

                conn.commit()

                if cursor.rowcount > 0:
                    print("✅ Student Deleted!")
                else:
                    print("❌ Student ID Not Found")

            elif choice == 6:
                print("🙏 Thank You!")
                break

            else:
                print("❌ Invalid Choice")

        except ValueError:
            print("❌ Please enter numbers only!")

except mysql.connector.Error as e:
    print("Database Error:", e)

finally:
    try:
        conn.close()
    except:
        pass