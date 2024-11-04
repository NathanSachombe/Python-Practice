# Allows us store information using key value pairs

monthConversions = {              # Creating dictionaries
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

}

print(monthConversions["Nov"])         # Accesing items in a dictionary
print(monthConversions.get("Jul"))     # Accesing items in a dictionary
