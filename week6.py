import random

# 2. Recursive Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


# 4. Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    # 1. Generate Data
    scores = [random.randint(50, 100) for _ in range(10)]
    print("Original Scores:", scores)

    # 2. Sort
    sorted_scores = merge_sort(scores)
    print("Sorted Scores:", sorted_scores)

    # 3. Search input
    try:
        target = int(input("Enter a score to search: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # 4. Execute binary search
    index = binary_search(sorted_scores, target)

    if index != -1:
        print(f"Candidate with score {target} found at rank {index}.")
    else:
        print(f"Score {target} not found.")


if __name__ == "__main__":
    main()