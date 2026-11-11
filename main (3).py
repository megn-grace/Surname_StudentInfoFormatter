fname = input("Enter first name: ").strip
lname = input("Enter last name: ").strip
section = input("Enter section: ").strip
fsub = input("Enter favorite subject: ").strip

fulln = f"{fname.strip().title()} {lname.strip().title()}"

formatedn = fname.title()
ncode = fname.upper()
fsection = section.upper()
ffsub = fsub.title()
ccount = len(formatedn)

print("\nFormatted Output")
print(f"Name: ", fulln)
print(f"Name Code: ", fulln)
print(f"Section: ", section)
print(f"Favorite Subject: ", fsub)
print(f"Character Count: ", ccount)