from audioop import reverse


firstname = "john"
lastname = "smith"
tele = "00468123456789"

#1
print(f'{firstname}, {lastname}, {tele}')

fullname = firstname + " " + lastname
print(fullname)

print(f' {len(fullname)} {len(firstname)} {len(lastname)}')

print(f"{fullname}\n{tele}")

print(fullname + " " + tele)
print(f'{fullname} {tele}')
print('{} {}'.format(fullname,  tele))
#print(f'Ditt namn är {} och ditt nummer är {}, fullname, tele')

#2
print(fullname[:5])
print(fullname[1:-1])
print(fullname.upper()[0:-1:2])
print(fullname[::-1])
print(fullname[5:5])
