import phonenumbers

# old_string_of_numbers = "(694)544-2366, (420)  647-3944, ( 321) 1526278, (776) 949-8387, 351588-8871"
# with open("old_numbers.txt", "w") as handler:
#     handler.write(old_string_of_numbers)

with open("old_numbers.txt", "r") as handler:
    lines = handler.read()

numbers = lines.split(", ")
# print(a)
# numbers = ["(694)544-2366", "(420)  647-3944", "( 321) 1526278", "(776) 949-8387", "351588-8871"]
new_number = []
for i in numbers:
    new_number.append(phonenumbers.format_number(phonenumbers.parse(i, 'US'), phonenumbers.PhoneNumberFormat.NATIONAL))

new_string_of_numbers = ", ".join(new_number)

with open("new_numbers.txt", "w") as handler:
    handler.write(new_string_of_numbers)





