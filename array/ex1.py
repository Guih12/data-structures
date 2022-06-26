def compare_feb_in_january(values):
    return values[1] - values[0]

def tree_months(values):
    sum = 0
    for i in range(3):
        sum += values[i]

    return sum

def find_2000_dollars(values):
    for i in range(len(values)):
        if values[i] == 2000:
            print("found")



def add_expense(values):
    values.append(1980)

values = [2200, 2350, 2600, 2130, 2190]

print(compare_feb_in_january(values))
print(tree_months(values))
find_2000_dollars(values)

add_expense(values)

##vector.append(100) O(n) -> complexity