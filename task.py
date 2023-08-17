import phonenumbers

with open("old_numbers.txt", "r") as handler:
    lines = handler.read().split(", ")

new_number = []
for i in lines:
    new_number.append(phonenumbers.format_number(phonenumbers.parse(i, 'US'), phonenumbers.PhoneNumberFormat.NATIONAL))

with open("new_numbers.txt", "w") as handler:
    handler.write(", ".join(new_number))





