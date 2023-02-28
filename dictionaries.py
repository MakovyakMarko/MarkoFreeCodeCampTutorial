monthConversions = {
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
    12: "December",
}

print(monthConversions["Nov"])
print(monthConversions["Mar"])
print(monthConversions["Aug"])

print(monthConversions.get("Dec"))
print(monthConversions.get("Luv"))
print(monthConversions.get("Luv", "Not a valid key"))




