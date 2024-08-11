c_problems = [
    {
        "id": 1,
        "title": "Two Sum",
        "description": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
        "test_cases": ["[2,7,11,15]\n9", "[3,2,4]\n6", "[3,3]\n6"],
        "expected_outputs": ["[0,1]", "[1,2]", "[0,1]"]
    },
    {
        "id": 2,
        "title": "Reverse String",
        "description": "Write a function that reverses a string. The input string is given as an array of characters s.",
        "test_cases": ['["h","e","l","l","o"]', '["H","a","n","n","a","h"]'],
        "expected_outputs": ['["o","l","l","e","h"]', '["h","a","n","n","a","H"]']
    },
    {
        "id": 3,
        "title": "Fibonacci Number",
        "description": "Given n, calculate F(n), where F(n) is the n-th Fibonacci number.",
        "test_cases": ["2", "3", "4"],
        "expected_outputs": ["1", "2", "3"]
    },
    {
        "id": 4,
        "title": "Valid Parentheses",
        "description": "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
        "test_cases": ['"{()}"', '"({[)]"', '"()[]{}?"'],
        "expected_outputs": ["true", "false", "false"]
    }

]

def add_problem(c_problem):
    c_problem['id'] = len(c_problems) + 1
    c_problems.append(c_problem)