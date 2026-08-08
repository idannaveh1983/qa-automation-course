test_results = [
    "בדיקת התחברות: עבר",
    "בדיקת חיפוש: נכשל",
    "בדיקת תשלום: עבר",
    "בדיקת עדכון פרופיל: עבר"
]

with open("results.txt", "w", encoding="utf-8") as report:
    for result in test_results:
        report.write(result + "\n")

print("הדוח נשמר בהצלחה!")