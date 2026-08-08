def check_login(username, password):
    if username == "" or password == "":
        return "test failed: username or password is empty"
    else:
        return "test passed: login successful"

result1 = check_login("test", "1234")
result2 = check_login("", "1234")

print(result1)
print(result2)