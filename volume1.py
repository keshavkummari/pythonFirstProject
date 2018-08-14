# Liters in a 12-ounce can and a two-liter bottle

CAN_VOLUME=0.355
BOTTLE_VOLUME=2.0

# Number of cans per pack
cansPerPack=6

# Calculate total volume in the cans

totalVolume = cansPerPack * CAN_VOLUME

print("A Six Pack of 12-ounce cans contains", totalVolume,"liters of water.")

# Calculate total volume in the cans and a 2-liter bottle

totalVolume = totalVolume + BOTTLE_VOLUME

print("A six-pack and a two-liter bottle contain",totalVolume,"liters.")