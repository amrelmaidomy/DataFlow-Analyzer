# TASK 1
email = "Amit_ml@gmail.edu"

# Validation (اختياري لو عايز)
if email.count("@") != 1 or "." not in email.split("@")[1]:
    print("Invalid email")
else:
    username = email.split("@")[0]
    after_at = email.split("@")[1]
    domain = after_at.split(".")[0]

    if email.endswith(".com"):
        domain_type = "Commercial Domain"
    elif email.endswith(".edu"):
        domain_type = "Educational Domain"
    else:
        domain_type = "Other Domain"

    print(username)
    print(domain)
    print(domain_type)

print(50*"-")


# TASK 2
encoded = "###!!@mocleW EPGTQ!!!6789"

core = encoded[6:18]   # شغّالة
words = core.split()
decoded_first = words[0][::-1]
decoded_second = words[1]
print(decoded_first, decoded_second)

numbers = encoded[-4:][::-1]
print(numbers)
print(50*"-")


# TASK 3
encoded = "&&&$gnirtS PLIO!!@1234"

core = encoded[4:16]  # ← هنا كان الخطأ، لازم تبدأ من index 4 مش 6
words = core.split()
first = words[0][::-1]
second = words[1].replace("I", "E").replace("O", "U")
print(first, second)

numbers = encoded[-4:][::-1]
print(numbers)
print(50*"-")


# TASK 4
encoded = "##$$$@!yalpstcejorp EPUVT**9887"

core = encoded[7:25]  # شغّالة
words = core.split()
first = words[0][::-1]
second = words[1].replace("E", "A").replace("U", "O")
print(first, second)

numbers = encoded[-4:][::-1]
print(numbers)
print(50*"-")
