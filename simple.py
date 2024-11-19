import random


questions = {
    "Python": [
        {"question": "What is the output of print(type([]))?", "options": ["A) <class 'list'>", "B) <class 'dict'>", "C) <class 'tuple'>", "D) <class 'set'>"], "answer": "A"},
        {"question": "Which syntax is correct to create a function in Python?", "options": ["A) function myFunction()", "B) def myFunction():", "C) create myFunction()", "D) func myFunction():"], "answer": "B"},
        {"question": "What is the result of 3 * 1 ** 3?", "options": ["A) 3", "B) 1", "C) 9", "D) 27"], "answer": "A"},
        {"question": "How do you insert a comment in Python?", "options": ["A) // This is a comment", "B) # This is a comment", "C) /* This is a comment */", "D) <!-- This is a comment -->"], "answer": "B"},
        {"question": "Which method removes whitespace from both ends of a string?", "options": ["A) strip()", "B) trim()", "C) len()", "D) slice()"], "answer": "A"},
        {"question": "What is the output of print(2 == 2 == 1)?", "options": ["A) True", "B) False", "C) 1", "D) 0"], "answer": "B"},
        {"question": "Which is not a valid variable name?", "options": ["A) my_var", "B) 2ndVar", "C) var_2", "D) _myVar"], "answer": "B"},
        {"question": "What will print(bool(0)) return?", "options": ["A) True", "B) False", "C) None", "D) Error"], "answer": "B"},
        {"question": "Which data type is immutable in Python?", "options": ["A) List", "B) Set", "C) Dictionary", "D) Tuple"], "answer": "D"},
        {"question": "What does the len() function do?", "options": ["A) Returns the length of an object", "B) Returns the first element", "C) Returns the type", "D) Returns the last element"], "answer": "A"},
        {"question": "Which keyword handles exceptions in Python?", "options": ["A) try", "B) catch", "C) handle", "D) except"], "answer": "A"},
        {"question": "What is the purpose of the pass statement?", "options": ["A) To skip the next iteration", "B) To indicate nothing happens", "C) To exit a loop", "D) To skip the next statement"], "answer": "B"},
        {"question": "How do you create a list in Python?", "options": ["A) list[]", "B) []", "C) list()", "D) new list()"], "answer": "B"},
        {"question": "What will print({1, 2, 2, 3}) return?", "options": ["A) {1, 2, 3}", "B) {1, 2, 2, 3}", "C) [1, 2, 3]", "D) Error"], "answer": "A"},
        {"question": "What is the correct way to import a module?", "options": ["A) import module", "B) include module", "C) require module", "D) using module"], "answer": "A"},
        {"question": "Which function converts a string to an integer?", "options": ["A) int()", "B) str()", "C) float()", "D) char()"], "answer": "A"},
        {"question": "What is the output of print('Hello'[1])?", "options": ["A) H", "B) e", "C) l", "D) o"], "answer": "B"},
        {"question": "Which formats strings in Python?", "options": ["A) %", "B) .format()", "C) f-strings", "D) All of the above"], "answer": "D"},
        {"question": "What is a lambda function?", "options": ["A) A function that returns a value", "B) A function defined with 'lambda'", "C) A function with any arguments", "D) None of the above"], "answer": "B"},
        {"question": "How do you check if a key exists in a dictionary?", "options": ["A) key in dict", "B) dict.has_key(key)", "C) key in dict.keys()", "D) All of the above"], "answer": "D"}
    ],
    "RDBMS": [
        {"question": "What does DDL stand for?", "options": ["A) Data Description Language", "B) Data Definition Language", "C) Data Delete Language", "D) Data Distribution Language"], "answer": "B"},
        {"question": "Which of the following is a DDL command?", "options": ["A) SELECT", "B) INSERT", "C) CREATE", "D) UPDATE"], "answer": "C"},
        {"question": "What is the purpose of a primary key?", "options": ["A) Allow duplicate values", "B) Uniquely identify records", "C) Create indexes", "D) Link tables"], "answer": "B"},
        {"question": "Which SQL clause is used to filter records?", "options": ["A) WHERE", "B) HAVING", "C) ORDER BY", "D) SELECT"], "answer": "A"},
        {"question": "What does the JOIN clause do?", "options": ["A) Combines rows from multiple tables", "B) Deletes rows", "C) Filters columns", "D) Updates rows"], "answer": "A"},
        {"question": "Which SQL clause is used to filter records?", "options": ["A) WHERE", "B) HAVING", "C) ORDER BY", "D) SELECT"], "answer": "A"},
        {"question": "What does the JOIN clause do?", "options": ["A) Combines rows from multiple tables", "B) Deletes rows", "C) Filters columns", "D) Updates rows"], "answer": "A"},
        {"question": "Which command removes all rows from a table?", "options": ["A) DROP", "B) DELETE", "C) TRUNCATE", "D) REMOVE"], "answer": "C"},
        {"question": "What does ACID stand for in databases?", "options": ["A) Atomicity, Consistency, Isolation, Durability", "B) Algorithm, Cache, Index, Durability", "C) Atomicity, Coherence, Integrity, Distribution", "D) Aggregation, Consistency, Indexing, Design"], "answer": "A"},
        {"question": "Which statement is used to rename a table?", "options": ["A) ALTER TABLE", "B) RENAME TABLE", "C) MODIFY TABLE", "D) UPDATE TABLE"], "answer": "B"},
        {"question": "Which of the following is a transaction control command?", "options": ["A) COMMIT", "B) SELECT", "C) DELETE", "D) INSERT"], "answer": "A"},
        {"question": "What does the HAVING clause do?", "options": ["A) Filters aggregated data", "B) Limits records", "C) Filters columns", "D) Updates rows"], "answer": "A"},
        # Add up to 20 RDBMS questions
    ],
    "JavaScript": [
        {"question": "Which keyword declares a variable?", "options": ["A) var", "B) let", "C) const", "D) All of the above"], "answer": "D"},
        {"question": "How do you write 'Hello World' in an alert box?", "options": ["A) alertBox('Hello World')", "B) msg('Hello World')", "C) alert('Hello World')", "D) message('Hello World')"], "answer": "C"},
        {"question": "What does NaN mean in JavaScript?", "options": ["A) Null and None", "B) Not a Number", "C) No Action Needed", "D) No Applicable Number"], "answer": "B"},
        {"question": "How do you create a function in JavaScript?", "options": ["A) function = myFunction()", "B) function myFunction()", "C) create myFunction()", "D) func myFunction()"], "answer": "B"},
        {"question": "Which of the following is not a JavaScript data type?", "options": ["A) Number", "B) String", "C) Boolean", "D) Character"], "answer": "D"},
        {"question": "What will be the output of: console.log(3 + '3')?", "options": ["A) 6", "B) '33'", "C) Error", "D) NaN"], "answer": "B"},
        {"question": "Which method is used to add an element to the end of an array?", "options": ["A) push()", "B) pop()", "C) shift()", "D) unshift()"], "answer": "A"},
        {"question": "What will be the output of: typeof null?", "options": ["A) null", "B) object", "C) undefined", "D) string"], "answer": "B"},
        {"question": "How can you detect the client's browser name in JavaScript?", "options": ["A) navigator.browserName", "B) window.browserName", "C) navigator.appName", "D) browser.name"], "answer": "C"},
        {"question": "What is the correct syntax to write an 'if' statement in JavaScript?", "options": ["A) if i = 5 then", "B) if (i == 5)", "C) if i == 5 then", "D) if i = 5"], "answer": "B"},
        {"question": "What is the default value of an uninitialized variable in JavaScript?", "options": ["A) null", "B) undefined", "C) 0", "D) NaN"], "answer": "B"},
        {"question": "Which of the following is used to define a block of JavaScript code?", "options": ["A) {}", "B) []", "C) ()", "D) <>"], "answer": "A"},
        {"question": "How can you include JavaScript code inside an HTML file?", "options": ["A) <script>", "B) <javascript>", "C) <code>", "D) <js>"], "answer": "A"}
    ]
}

def run_quiz():
    print("Select a topic:")
    topics = list(questions.keys())
    for i, topic in enumerate(topics):
        print(f"{i + 1}) {topic}")
    
    try:
        topic_choice = int(input("Enter the number of your topic choice: "))
        if topic_choice < 1 or topic_choice > len(topics):
            raise ValueError
    except ValueError:
        print("Invalid choice. Restart and select a valid topic.")
        return

    chosen_topic = topics[topic_choice - 1]
    print(f"\nYou selected: {chosen_topic}\n")
    selected_questions = questions[chosen_topic]
    
    score = 0
    asked_questions = random.sample(selected_questions, 5)  # Pick 5 random questions
    
    for q in asked_questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        
        answer = input("Enter your answer (A, B, C, D): ").upper()
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['answer']}\n")
    
    print(f"Your final score: {score}/5\n")

run_quiz()
