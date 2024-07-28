months_named = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months_numbered = list(range(1, 13))
months_dict = dict(zip(months_named, months_numbered))

months_named.clear()
months_numbered.clear()

print("Months Dictionary:", months_dict)

months_extracted = list(months_dict.keys())
months_extracted.sort()
print("Months Extracted (Alphabetical Order):", months_extracted)

