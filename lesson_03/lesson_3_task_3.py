from address import Address
from mailing import Mailing

to_address = Address(343986, "Владивосток", "Ленина", "145", "4")
from_address = Address(785255, "Москва", "Калинина", "54", "3")
mailing = Mailing(to_address, from_address, "2350", "YG7672899")
print(mailing)
