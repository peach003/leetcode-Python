'''  class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
       
        return str(x) == str(x)[::-1]


solution = Solution()


test_cases = [121, -121, 10, 0, 12321, 123321, 12345]


for num in test_cases:
    result = solution.isPalindrome(num)
    print(f"{num} -> {result}") '''


class Solution:
    def isPalindrome(self, x: int) -> bool:
       
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10 
            x //= 10                            

        
        return x == reverted or x == reverted // 10
    
    # =========================================================
# Python Slice Syntax
# ---------------------------------------------------------
# Format: sequence[start:end:step]
#   - start: starting index (inclusive), default 0
#   - end:   ending index (exclusive), default len(sequence)
#   - step:  step size (positive → forward, negative → backward), default 1
#
# Common examples:
#   s = "abcdef"
#   s[0:3]   -> 'abc'    # from index 0 to 2
#   s[:3]    -> 'abc'    # omit start
#   s[2:]    -> 'cdef'   # omit end
#   s[::2]   -> 'ace'    # take every second element
#   s[::-1]  -> 'fedcba' # reverse the sequence
#
# Usage in palindrome check:
#   str(x)[::-1]  # reverse the string
# =========================================================
#
# Palindrome Number Check Without Converting to String (Math Method)
# ---------------------------------------------------------
# Core idea:
#   1. Negative numbers are not palindromes.
#   2. If the number ends with 0 but is not 0, it's not a palindrome.
#   3. Reverse only the second half of the number using math operations.
#   4. Compare the first half with the reversed second half:
#      - Even length: direct comparison
#      - Odd length: remove the middle digit before comparison
#
# Key variable:
#   reverted: stores the reversed second half of the number.
#
# Loop logic:
#   while x > reverted:
#       reverted = reverted * 10 + x % 10  # append last digit to reverted
#       x //= 10                           # remove last digit
#
# Check condition:
#   return x == reverted or x == reverted // 10
#   - Even length: x == reverted
#   - Odd length:  x == reverted // 10
#
# Time complexity: O(log n)  # each loop removes one digit
# Space complexity: O(1)     # only constant extra variables
# =========================================================

# =========================================================
# [Python] Class Attributes vs Instance Attributes
# ---------------------------------------------------------
# 1. Class Attribute (类属性)
#    - Defined in the class body, outside any method.
#    - Belongs to the class, shared by all instances.
#    - Access: ClassName.attr or instance.attr
#    - Changing via class affects all instances.
#      Example:
#          class Demo:
#              species = "Human"  # class attribute
#          obj1 = Demo(); obj2 = Demo()
#          Demo.species = "Homo sapiens"
#          print(obj1.species, obj2.species)  # both changed
#
# 2. Instance Attribute (实例属性)
#    - Usually defined in __init__ using self.attr.
#    - Belongs to each instance; different instances have independent copies.
#    - Access: instance.attr
#    - Changing affects only that instance.
#      Example:
#          class Demo:
#              def __init__(self, name):
#                  self.name = name  # instance attribute
#          obj1 = Demo("Alice"); obj2 = Demo("Bob")
#          obj1.name = "Eve"  # only obj1 changes
# =========================================================
#
# [Python] Methods: Instance / Class / Static
# ---------------------------------------------------------
# 1. Instance Method (实例方法)
#    - No decorator.
#    - First parameter: self (instance itself).
#    - Can access/modify instance attributes and class attributes.
#    - Called via instance: instance.method(...)
#      Example:
#          def method(self): ...
#
# 2. Class Method (类方法)
#    - Decorator: @classmethod
#    - First parameter: cls (class itself).
#    - Can access/modify class attributes, but not instance attributes directly.
#    - Called via class or instance: ClassName.method(...) or instance.method(...)
#      Example:
#          @classmethod
#          def method(cls): ...
#
# 3. Static Method (静态方法)
#    - Decorator: @staticmethod
#    - No self or cls parameter.
#    - Cannot access instance or class attributes unless explicitly passed.
#    - Behaves like a normal function but lives in the class's namespace.
#    - Called via class or instance: ClassName.method(...) or instance.method(...)
#      Example:
#          @staticmethod
#          def method(...): ...
#
# ---------------------------------------------------------
# Method Comparison Table:
# ---------------------------------------------------------
# | Method Type      | Decorator       | First Param | Access Instance Attr | Access Class Attr | Typical Call         |
# |------------------|-----------------|-------------|----------------------|-------------------|----------------------|
# | Instance Method  | (none)          | self        | YES                  | YES               | instance.method()    |
# | Class Method     | @classmethod    | cls         | NO                   | YES               | Class.method()       |
# | Static Method    | @staticmethod   | (none)      | NO                   | NO                | Class.method()       |
# =========================================================



