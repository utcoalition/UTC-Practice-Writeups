import re

given ="Ohis is the flag: L2IPMntzNP3wOYIfTlP5S42xeYIkSzQ3LnH5aSM3QYZwbl1YHSWoH3E1 Eust decode it :K"
known = 'T'
broken = 'O'
void= ord(known)-ord(broken)
assert chr(ord(broken)+void)==known

fixed=""

for c in given:
	if re.search(r'([A-Z])', c):
		if ord(c)+void > 90:
			fixed+=chr(64+((ord(c)+void)%90))
		else:
			fixed+=chr(ord(c)+void)
	else:
		fixed+=c

print fixed
