
class NameTooShortError(Exception):
    pass
class MustContainAtSymbolError(Exception):
    pass
class InvalidDomainError(Exception):
    pass

import re
patern=r"(?P<domain>(\.[a-z]+))" # using regex to find the domain in the email

valid_domains=[".com", ".bg", '.org', ".net"]

valid=True
actual_domain=''

while True:
    is_there_at_symbol = False
    name=""
    # read the email:
    email=input()
    if email == "END":
        break
    # check for domain in the mail
    current_domain=re.finditer(patern,email)
    for domain in current_domain:
        actual_domain=domain.group('domain')
    # check if name in a email is enought long:
    for char in email:
        if char =="@" or char ==".": # if meet @ stop store the name
            break
        name+=char

    if email.count("@") <2: #  if in email is @ make notice that
        is_there_at_symbol=True



    if len(name)<4:
        raise NameTooShortError("Name must be more than 4 characters")
    # check if in email is @:
    if not is_there_at_symbol:
        raise MustContainAtSymbolError("Email must contain one @")
    # check if is valid domain
    if actual_domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")



    # if everithing is fine print
    if valid:
        print("Email is valid")

# what are you doing in this case  => deni.@.bg?

