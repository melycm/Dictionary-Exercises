phonebook_dict = { 
  'Alice': '703-493-1834', 
  'Bob': '857-384-1234', 
  'Elizabeth': '484-584-2923'
}

#1
values = phonebook_dict['Elizabeth']
print(values)

#2
phonebook_dict["Kareem's"] = "938-489-1234"
print(phonebook_dict)

#3
del phonebook_dict['Alice']
print(phonebook_dict)

#4
phonebook_dict['Bob'] = '968-345-2345'
print(phonebook_dict)

#5
phonebook_dict['Alice'] = '703-493-1834'
print(phonebook_dict)
