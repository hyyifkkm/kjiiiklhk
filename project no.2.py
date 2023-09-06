email = input("enter your email id")  # with gmail.com
j, d, k = 0, 0, 0
if len(email) >= 6:
  if email[0].isalpha():
    if ("@" in email) and (email.count("@") == 1):
      if (email[-4] == ".") ^ (email[-3] == "."):
        for i in email:
          if i.isspace():
            k = 1
          if i.isalpha():
            continue

          elif i.isdigit():
            continue
          elif i == "_" or i == "." or i == "@":
            continue
          else:
            d = 1
        if (k == 1) or (d == 1):
          print("space and any special charecter are not allowed in id")
        else:
          password = input("enter your password")
          ps = "admin123"
          if password == ps:
            print("log in successfully")
    else:
      print("@ must be at least 1 time")

  else:
    print("wrong email 2")

else:
  print("invalid id")
