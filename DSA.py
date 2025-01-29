# Example array
array = [10, 5, 20, 3, 7, 9, 12]

# Remove duplicates and sort the array
sorted_arr = sorted(set(array))

# Ensure there are at least two distinct elements
if len(sorted_arr) < 2:
    print("Array must contain at least two distinct elements")
else:
    # Find second smallest and second largest elements
    second_smallest = sorted_arr[1]
    second_largest = sorted_arr[-2]
    
    print(f"Second Smallest: {second_smallest}")
    print(f"Second Largest: {second_largest}")
