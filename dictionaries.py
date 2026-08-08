user = {
    "username": "idan",
    "email": "idan@example.com",
    "is_admin": False
}

print("שם משתמש:", user["username"])
print("אימייל:", user["email"])

if user["is_admin"] == False:
    print("המשתמש אינו מנהל - גישה מוגבלת")
else:
    print("המשתמש הוא מנהל - גישה מלאה")