# Convert miles to kilometers

# Example
miles = 500
kilometers = miles * 1.609344
print(kilometers)

# Trip 1 - Seattle to San Francisco: 808 miles
# Trip 2 - San Francisco to Austin: 1,766 miles
# Trip 3 - Austin to Tampa: 1,145 miles

miles_t1 = 808
miles_t2 = 1766
miles_t3 = 1145
miles_total = miles_t1 + miles_t2 + miles_t3
print("total in miles: " + str(miles_total))

kilo_t1 = miles_t1 * 1.609344
kilo_t2 = miles_t2 * 1.609344
kilo_t3 = miles_t3 * 1.609344
kilo_total = miles_total * 1.609344
print("total in kilometers: " + str(kilo_total))

print("For the roadtrip from Seattle, Washington to Tampa, Florida, we would drive " + str(miles_total) + " miles")
print("or " + str(kilo_total) + " kilometers.")
