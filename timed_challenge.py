# 3. Remove Duplicates (Keep Order)
#    Return the values in the order they first appeared, without duplicates.
#    Input: ["apple", "banana", "apple", "kiwi", "banana"]
#    Output: ["apple", "banana", "kiwi"]

def remove_duplicates_keep_order(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

#test cases
print(remove_duplicates_keep_order(["apple", "banana", "apple", "kiwi", "banana"]))

print(remove_duplicates_keep_order([1, 2, 2, 3, 1, 4]))

print(remove_duplicates_keep_order([]))

    

