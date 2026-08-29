def calculate_average(numbers):
    # Start typing here and watch Copilot suggest the function body

question to ask in inline chat - what does this function do?
"comment on the time and space complexity of this function"
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


certain inline functions - 
/explain -  provides an explanation of the selected code
/suggest - offers code suggestions based on the current context
/tests - Generates unit tests for the selected function or class
/comment - converts comments into code snippets
/docs - Generates documentation for the selected code

