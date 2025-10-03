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

#Reflection:
#   - For this time challenge, I chose to use a combination of a set and a list to solve the problem of removing duplicates while preserving 
#     order. This set allowed me to move quickly to check if an item had already been seen, since lookups and insertions in a set are 0(1) on average. 
#     The list preserved the original order by appending only the first occurence of each item. Together, these two structures gave me a simple
#     and efficient 0(n) solution that directly matched the requirements of the problem.
#   - The time limit shaped my decision because I had to balance efficiency with clarity. I briefly considered other approaches,
#     such as using only a list and checking membership before adding, but that would have resulted in taking up too much time. Under time
#     constraints, I prioritized an approach that I already knew would be both correct and efficient, without overcomplicating the implementation.
#     Sticking with a set and list combination was the safest and clearest path forward. 
#   - The main trade-off I made under time pressure was simplicity over extensibility. My solution works well for hashable values like strings
#     and integers, but it would not handle unhashable inputs. Given the 30 minute time constraint, I accepted this limitation in favor of 
#     delivering a clean, working solution. In a real-world scenario with more time, I could expand the approach to support broader input
#     types or optimize memory use further. 
#
#


    

