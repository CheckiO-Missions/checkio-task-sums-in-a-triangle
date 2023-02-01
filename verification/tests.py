"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [[
                [1],
                [2, 3],
                [3, 3, 1],
                [3, 1, 5, 4],
                [3, 1, 3, 1, 3],
                [2, 2, 2, 2, 2, 2],
                [5, 6, 4, 5, 6, 4, 3]
            ]],
            "answer": 23,
            "explanation": [0, 1, 1, 2, 2, 3, 4]
        },
        {
            "input": [[
                [1],
                [2, 1],
                [1, 2, 1],
                [1, 2, 1, 1],
                [1, 2, 1, 1, 1],
                [1, 2, 1, 1, 1, 1],
                [1, 2, 1, 1, 1, 1, 9]
            ]],
            "answer": 15,
            "explanation": [0, 1, 2, 3, 4, 5, 6]
        },
        {
            "input": [[
                [9],
                [2, 2],
                [3, 3, 3],
                [4, 4, 4, 4]
            ]],
            "answer": 18,
            "explanation": [0, 1, 2, 3]
        },
        {
            "input": [[
                [2],
                [7, 9],
                [0, 8, 6],
                [4, 7, 6, 8],
                [0, 5, 5, 4, 1],
                [9, 1, 0, 1, 6, 9]
            ]],
            "answer": 35,
            "explanation": [0, 1, 2, 3, 4, 5]
        },
        {
            "input": [[
                [4],
                [3, 0],
                [5, 1, 1],
                [2, 0, 2, 0],
                [1, 1, 1, 8, 3],
                [5, 3, 4, 8, 2, 8],
                [1, 0, 5, 0, 4, 3, 1]
            ]],
            "answer": 30,
            "explanation": [0, 0, 1, 2, 3, 3, 4]
        },
        {
            "input": [[
                [6],
                [7, 9],
                [3, 8, 3],
                [3, 4, 0, 2],
                [6, 9, 9, 6, 8],
                [3, 7, 0, 8, 2, 2],
                [0, 6, 3, 0, 0, 6, 7]
            ]],
            "answer": 49,
            "explanation": [0, 1, 1, 1, 1, 1, 1]
        },
        {
            "input": [[
                [6],
                [0, 6],
                [3, 0, 7],
                [0, 4, 2, 9],
                [4, 4, 3, 6, 9],
                [3, 1, 0, 5, 9, 0],
                [8, 9, 7, 7, 3, 4, 5]
            ]],
            "answer": 50,
            "explanation": [0, 1, 2, 3, 4, 4, 5]
        },
        {
            "input": [[
                [6],
                [6, 9],
                [7, 1, 4],
                [6, 9, 9, 7],
                [1, 6, 7, 9, 7],
                [5, 7, 2, 6, 0, 9],
                [1, 2, 2, 6, 0, 1, 6],
                [8, 5, 0, 3, 1, 4, 3, 1],
                [9, 6, 4, 1, 1, 9, 3, 7, 9],
                [5, 8, 4, 3, 5, 4, 5, 1, 8, 3]
            ]],
            "answer": 66,
            "explanation": [0, 1, 2, 3, 4, 5, 6, 7, 8, 8]
        },
    ],
    "Extra": [
        {
            "input": [[
                [4],
                [4, 0],
                [3, 0, 9],
                [7, 5, 7, 1],
                [9, 1, 4, 1, 7],
                [5, 6, 5, 6, 5, 8],
                [3, 9, 9, 8, 3, 3, 7],
                [4, 7, 2, 6, 0, 6, 6, 7],
                [6, 6, 2, 9, 6, 1, 0, 2, 5],
                [9, 0, 7, 5, 3, 1, 4, 6, 0, 3]
            ]],
            "answer": 62,
            "explanation": [0, 0, 0, 0, 0, 1, 2, 3, 3, 3]
        },
        {
            "input": [[
                [2],
                [7, 7],
                [2, 5, 9],
                [0, 5, 8, 4],
                [3, 2, 1, 5, 2],
                [6, 4, 2, 6, 7, 2],
                [7, 5, 9, 4, 7, 6, 6],
                [1, 9, 4, 4, 5, 7, 3, 1],
                [9, 3, 1, 0, 0, 1, 1, 0, 9],
                [7, 6, 4, 8, 3, 6, 8, 7, 9, 0]
            ]],
            "answer": 61,
            "explanation": [0, 1, 2, 2, 3, 4, 4, 5, 6, 6]
        },
        {
            "input": [[
                [3],
                [7, 8],
                [4, 7, 3],
                [4, 7, 1, 6],
                [6, 3, 7, 1, 4],
                [3, 4, 8, 4, 4, 5],
                [3, 8, 1, 0, 1, 9, 6],
                [7, 1, 4, 1, 9, 8, 5, 5],
                [6, 4, 5, 8, 5, 3, 1, 0, 5]
            ]],
            "answer": 54,
            "explanation": [0, 1, 1, 1, 2, 2, 3, 4, 4]
        },
        {
            "input": [[
                [5],
                [5, 6],
                [5, 0, 5],
                [0, 1, 7, 1],
                [5, 8, 3, 4, 6],
                [9, 0, 7, 6, 9, 1],
                [8, 0, 3, 3, 1, 2, 2]
            ]],
            "answer": 38,
            "explanation": [0, 1, 2, 2, 3, 4, 5]
        },
        {
            "input": [[
                [5],
                [8, 2],
                [1, 9, 6],
                [4, 9, 9, 9],
                [9, 5, 5, 0, 2],
                [6, 8, 4, 1, 7, 7]
            ]],
            "answer": 44,
            "explanation": [0, 0, 1, 1, 1, 1]
        },
        {
            "input": [[
                [1],
                [6, 7],
                [0, 3, 5],
                [4, 2, 9, 3],
                [2, 1, 3, 6, 5],
                [2, 9, 7, 0, 6, 7],
                [6, 6, 8, 5, 9, 9, 7],
                [1, 8, 4, 9, 2, 1, 5, 1],
                [7, 0, 3, 6, 2, 6, 2, 4, 2]
            ]],
            "answer": 55,
            "explanation": [0, 1, 2, 2, 2, 2, 2, 3, 3]
        },
        {
            "input": [[
                [6],
                [5, 8],
                [7, 4, 0],
                [1, 0, 8, 8],
                [2, 6, 6, 1, 1],
                [0, 7, 1, 6, 1, 6],
                [1, 4, 9, 5, 3, 1, 1]
            ]],
            "answer": 43,
            "explanation": [0, 1, 1, 2, 2, 3, 3]
        },
        {
            "input": [[
                [2],
                [2, 7],
                [8, 1, 1],
                [3, 6, 1, 6],
                [4, 6, 4, 0, 6]
            ]],
            "answer": 24,
            "explanation": [0, 0, 0, 1, 1]
        },
        {
            "input": [[
                [9],
                [4, 3],
                [4, 9, 5],
                [8, 9, 6, 0],
                [7, 6, 1, 7, 1],
                [5, 5, 2, 7, 0, 1],
                [0, 2, 6, 8, 1, 2, 9],
                [4, 9, 5, 0, 9, 6, 1, 0],
                [0, 0, 6, 4, 6, 7, 5, 9, 1]
            ]],
            "answer": 66,
            "explanation": [0, 0, 1, 2, 3, 3, 3, 4, 5]
        },
        {
            "input": [[
                [4],
                [1, 4],
                [9, 2, 9],
                [7, 9, 7, 8],
                [4, 9, 0, 1, 5]
            ]],
            "answer": 32,
            "explanation": [0, 0, 0, 1, 1]
        },
        {
            "input": [[
                [1],
                [1, 1],
                [1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1]
            ]],
            "answer": 9,
            "explanation": [0, 1, 2, 3, 4, 3, 4, 5, 3]
        },
        {
            "input": [[
                [4],
                [1, 7],
                [9, 9, 7],
                [4, 9, 9, 3],
                [3, 5, 3, 7, 5],
                [1, 7, 5, 3, 5, 6],
                [6, 5, 5, 8, 3, 3, 3],
                [6, 8, 6, 8, 7, 3, 7, 5],
                [7, 9, 9, 1, 6, 8, 7, 5, 9],
                [2, 8, 2, 5, 5, 5, 2, 5, 7, 8],
                [1, 3, 5, 2, 4, 5, 3, 5, 1, 1, 6],
                [8, 6, 1, 1, 3, 4, 7, 5, 3, 6, 1, 9],
                [5, 8, 6, 6, 2, 6, 9, 3, 7, 4, 6, 9, 9],
                [3, 3, 5, 4, 4, 6, 9, 2, 5, 7, 7, 1, 6, 7],
                [8, 1, 4, 4, 6, 8, 4, 9, 7, 6, 1, 8, 4, 2, 9],
                [6, 5, 8, 6, 8, 3, 2, 4, 8, 8, 1, 5, 6, 8, 8, 7],
                [6, 3, 9, 1, 5, 6, 7, 7, 2, 2, 6, 2, 2, 1, 8, 8, 6],
                [4, 7, 8, 7, 5, 2, 8, 8, 2, 2, 7, 1, 3, 8, 1, 9, 4, 7],
                [1, 7, 8, 1, 4, 3, 8, 6, 6, 9, 6, 3, 5, 4, 7, 6, 4, 5, 6],
                [1, 1, 4, 9, 9, 8, 3, 3, 8, 1, 8, 1, 7, 6, 6, 3, 2, 1, 1, 6]
            ]],
            "answer": 139,
            "explanation": None
        },
    ]
}
