# Store unique values in tuples

bank_name = "SBI", "BOI", "ICICI", "BOB", "HDFC", "IDFC"
nbfc = ("Aduvanz", "Dhani", "Bajaj", "DMI")

# bank_name[2] = "Bandhan Bank" # 'tuple' object does not support item assignment
print(bank_name.count("SBI"))
print(nbfc.index("DMI"))

for bank in bank_name:
    if bank == "BOI":
        continue
    print(bank)
else: print("No other bank found\n\n")

n = len(nbfc)
while(n > 0):
    print(nbfc[n-1])
    n -= 1

