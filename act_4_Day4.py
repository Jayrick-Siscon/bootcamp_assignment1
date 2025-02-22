def is_palindrome(s):
    # Remove spaces and convert to lowercase for comparison
    s = s.replace(" ", "").lower()
    
    # Check if the string is the same when reversed
    return s == s[::-1]

# Test the function
input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome!")
else:
    print(f"'{input_string}' is not a palindrome.")
