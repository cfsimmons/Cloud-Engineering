# immutable (object cannot be updated during runtime)
# variable assignment

x = 10
y = x

print(f"Type: {type(x)}")

x = 20

print(f"x: {x}")
print(f"y: {y}")

# mutable (object can be updated during runtime)
x = [1, 2, 3]
y = x

x.append(4)

print(f"x: {x}")
print(f"y: {y}")

"""
    Not: Most python bugs come from not asking questions:
        - Did I modify the object?
    or
        - Did I simply make my variable point somewhere else?
"""


# Lesson 2 - Lists vs. Tuples vs. Sets vs. Dictionaries

# List
servers = [
    "fw",
    "kali",
    "server"
]

# Tuple
coordinates = (10, 20)

# Set
ips = {
    "10.0.0.1",
    "10.0.0.2",
    "10.0.0.3",
    "10.0.0.3"
}

# Set - Unique values and fast membership checks. Automatically prevents duplicates, and
# checking whether an item exists is typically much faster than searching a list, 
# especially as the dataset grows.


print("\nprint sets:")
print(ips)

# Dictionary
host = {
    "hostname": "fw1",
    "ip": "10.10.1.1",
    "status": "Online"
}

print(f"\nhostname: ", host["hostname"])
print("ip: ", host["ip"])


# Can talk about this in interview
# Makes it easier to:
    # - count errors
    # - summarize findings
    # - feed structured data to an AI model 
    # - build dashboards later
status_handle = {
                "ERROR": [
                    "Disk full",
                    "Timeout",
                    "Connection Lost"
                ],
                "WARNING": [
                    "CPU High"
                ],
                "INFO": [
                    "Login Successful"
                ]
            }

# Entire ERROR list
print("\nError: ", status_handle["ERROR"])

# Disk full
print("Error: ", status_handle["ERROR"][0])

# Timeout
print("Error: ", status_handle["ERROR"][1])

# Connection Lost
print("Error: ", status_handle["ERROR"][2])
