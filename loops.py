usernames = ["idan", "dana", "", "michal"]

for username in usernames:
    if username == "":
        print("שגיאה: שם משתמש ריק - הבדיקה נכשלת!")
    else:
        print("בודק התחברות עבור:", username)