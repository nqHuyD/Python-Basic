customer = {
    "name": "Zeki",
    "age": 24,
    "is_handsome": True
}

# print(customer["name"])
# # print(customer["sss"]) Error
# print(customer.get("nameasdas")) # Not Error return None when not avaliable
# print(customer.get("birthdate", "Dec 14 1996"))

# customer["name"] = "Jack"
# print(customer["name"])

numberText = {
    "0": "Yero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}
#
# number = input("Give me a number ")
# output = ""
# for i in number:
#     output += numberText.get(i,"!") + " "
# print(output)