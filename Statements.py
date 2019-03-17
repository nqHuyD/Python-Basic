# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It is a Hot Day baby")
#     print("Drink plenty of water")
# elif is_cold:
#     print("Stay at home and sleep")
# else:
#     print("It's a lovely Day")
#
# print("Enjoy your weekend Baby")
#
# price = 1000000
# has_good_credit = True
#
# if has_good_credit:
#     downpayment = price * 0.1
# else:
#     downpayment = price * 0.2
# print(f"Your payment ${downpayment}")
#
# has_high_income = True
# has_good_credit = False
#
# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# elif has_high_income or has_good_credit:
#     print("May be we can loan")
# else:
#     print("Can't not loan")

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")