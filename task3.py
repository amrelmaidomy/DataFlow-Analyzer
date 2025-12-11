email = "Amit_ml@gmail.edu"

# Validation
if email.count("@") != 1 or "." not in email.split("@")[1]:
    print("Invalid email")
else:
    username = email.split("@")[0]
    domain_full = email.split("@")[1]
    domain = domain_full.split(".")[0]

    print("Username:", username)
    print("Domain:", domain)

    if domain_full.endswith(".com"):
        print("Commercial Domain")
    elif domain_full.endswith(".edu"):
        print("Educational Domain")
    else:
        print("Other Domain")
print(50 * "-")
msg = "###!!@mocleW EPGTQ!!!6789"

core = "".join([c for c in msg if c.isalpha() or c == " "])
first, second = core.split()

decoded = first[::-1] + " " + second
print(decoded)
print(50 * "-")
msg = "&&&**$gnirtS PLIO!!@1234"

core = "".join([c for c in msg if c.isalpha() or c == " "])
first, second = core.split()

second = second.replace("I", "E").replace("O", "U")

decoded = first[::-1] + " " + second
print(decoded)
print(50 * "-")
msg = "##$$$@!yalpstcejorp EPUVT****9887"

core = "".join([c for c in msg if c.isalpha() or c == " "])
first, second = core.split()


second = second.replace("E", "A").replace("U", "O")

decoded = first[::-1] + " " + second
print(decoded)
print(50 * "-")
