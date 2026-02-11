"""
Binary Search Implementation in Python

This module provides an efficient binary search algorithm implementation.
Binary search is an efficient algorithm for finding an item in a sorted list.
Time Complexity: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive
"""


def binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    
    Args:
        arr (list): A sorted list of comparable elements
        target: The element to search for
        
    Returns:
        int: The index of the target element if found, -1 otherwise
        
    Examples:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3, 4, 5], 6)
        -1
        >>> binary_search([], 1)
        -1
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=None, right=None):
    """
    Perform binary search on a sorted array using recursion.
    
    Args:
        arr (list): A sorted list of comparable elements
        target: The element to search for
        left (int, optional): Left boundary index
        right (int, optional): Right boundary index
        
    Returns:
        int: The index of the target element if found, -1 otherwise
        
    Examples:
        >>> binary_search_recursive([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search_recursive([1, 2, 3, 4, 5], 6)
        -1
    """
    if not arr:
        return -1
    
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def binary_search_leftmost(arr, target):
    """
    Find the leftmost occurrence of target in a sorted array.
    
    Args:
        arr (list): A sorted list of comparable elements (may contain duplicates)
        target: The element to search for
        
    Returns:
        int: The index of the leftmost occurrence of target, -1 if not found
        
    Examples:
        >>> binary_search_leftmost([1, 2, 2, 2, 3, 4, 5], 2)
        1
        >>> binary_search_leftmost([1, 2, 3, 4, 5], 6)
        -1
    """
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def binary_search_rightmost(arr, target):
    """
    Find the rightmost occurrence of target in a sorted array.
    
    Args:
        arr (list): A sorted list of comparable elements (may contain duplicates)
        target: The element to search for
        
    Returns:
        int: The index of the rightmost occurrence of target, -1 if not found
        
    Examples:
        >>> binary_search_rightmost([1, 2, 2, 2, 3, 4, 5], 2)
        3
        >>> binary_search_rightmost([1, 2, 3, 4, 5], 6)
        -1
    """
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


if __name__ == "__main__":
    # Example usage and demonstration
    print("Binary Search Implementation Demo")
    print("=" * 50)
    
    # Test case 1: Basic binary search
    test_arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    result = binary_search(test_arr, target)
    print(f"\nArray: {test_arr}")
    print(f"Searching for: {target}")
    print(f"Index found (iterative): {result}")
    print(f"Index found (recursive): {binary_search_recursive(test_arr, target)}")
    
    # Test case 2: Target not in array
    target = 8
    result = binary_search(test_arr, target)
    print(f"\nSearching for: {target}")
    print(f"Index found: {result}")
    
    # Test case 3: Array with duplicates
    test_arr_dup = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6]
    target = 2
    print(f"\nArray with duplicates: {test_arr_dup}")
    print(f"Searching for: {target}")
    print(f"Leftmost occurrence: {binary_search_leftmost(test_arr_dup, target)}")
    print(f"Rightmost occurrence: {binary_search_rightmost(test_arr_dup, target)}")
    
    target = 5
    print(f"\nSearching for: {target}")
    print(f"Leftmost occurrence: {binary_search_leftmost(test_arr_dup, target)}")
    print(f"Rightmost occurrence: {binary_search_rightmost(test_arr_dup, target)}")
    
    # Test case 4: Edge cases
    print("\n" + "=" * 50)
    print("Edge Cases:")
    print(f"Empty array: {binary_search([], 5)}")
    print(f"Single element (found): {binary_search([5], 5)}")
    print(f"Single element (not found): {binary_search([5], 3)}")
    print(f"First element: {binary_search([1, 2, 3, 4, 5], 1)}")
    print(f"Last element: {binary_search([1, 2, 3, 4, 5], 5)}")
