"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    seen = set()
    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)
    return False    

   
#Justification:
#   - I chose a set because it offers 0(1) average-time lookup and insertion.
#   - As we iterate, we check if the current product ID already exists in the set.
#   - This ensures detection of duplicates in 0(n) time when 0(n) extra space, which is more efficient than nested loops.


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""
from collections import deque

class TaskQueue:
    def __init__(self):
        self.queue = deque()
        

    def add_task(self, task):
        self.queue.append(task)

    def remove_oldest_task(self):
       if self.queue:
           return self.queue.popleft()
       return None

#Justification:
#   - I chose a deque from Python's collections because it allows 0(1) appends
#     and 0(1) pops from poth ends, unlike lists which take 0(n) when removing from the front. 
#   - this matches the required "first in, first out" behavior. 
    

"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)

#Justification
#   - I chose a set because it automatically ensures uniqueness of elements.
#   - Insertion is 0(1) average time, and getting the count of unique values is 0(1).
#   - This makes the tracker efficient for streaams of data where duplicates are common. 