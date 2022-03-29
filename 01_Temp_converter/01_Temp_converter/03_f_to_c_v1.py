# quick component to convert degrees F to C.
# Function takes in value, does conversion and puts answer into a list


def to_c(from_f):
    Centigrade = (from_f * 9/5) + 32
    return Centigrade


# Main routine
temperatures = [0, 32, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees F is {} degrees C".format(item, answer)
    converted.append(ans_statement)

print(converted)