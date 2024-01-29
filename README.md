# Objective

Design and implement a version of the classic game Hangman using Object-Oriented
Programming (OOP) principles. This exercise is intended to assess your skills in OOP
design patterns, testing, and overall software engineering capabilities. An optional challenge
is to add networked multiplayer functionality. You have the option to use one of the following
programming languages: Python, Golang, or JavaScript.

# Solution:

## Tests

To run the tests, execute the following command from the root folder.

```shell
python -m unittest discover -s tests
```

# Requirements:

Core Gameplay:

- Implement the basic Hangman gameplay where a player guesses letters to reveal a hidden word.
- The game should track the number of incorrect guesses and end when the maximum is
  reached.

Design Patterns:

- Utilise appropriate OOP design patterns to structure your code (e.g., Factory, Singleton,
  Strategy, Observer, etc.).
- Clearly document where and why specific design patterns are used.

User Interface:

- Implement a simple user interface (UI) for the game.
- This can be a console-based UI or a graphical user interface (GUI).
- Ensure the UI is user-friendly and intuitive.

Testing:

- Write comprehensive unit tests covering critical components of your code.
- Demonstrate the use of mock objects, test doubles, or other testing strategies.

Code Quality:

- Your code should be well-organised, commented, and adhere to best coding practices.
- Make sure the code is scalable and maintainable.

Optional Networked Multiplayer:

- As an additional challenge, implement a multiplayer mode where players can play against each other over a network.

- You may use raw sockets or HTTP for network communication. Explain your choice.
- Focus on ensuring the networked gameplay is stable and provides a seamless experience.

## Evaluation Criteria:

1. OOP Design: Elegance and effectiveness of OOP patterns and principles applied.
2. Code Quality: Readability, maintainability, and adherence to standard coding
   practices.
3. Testing: Depth and breadth of testing, including the use of different testing
   strategies.
4. Network Implementation (Optional): Robustness and efficiency of the networked
   multiplayer functionality (if implemented).
5. Problem Solving: Creativity and efficiency in solving problems encountered during
   development.
6. UI/UX Design: Usability and design of the user interface.

## Post-Submission Interview:

You will be required to participate in a follow-up call to discuss your submission.
Be prepared to explain in detail your design decisions, choice of technologies, and any
specific challenges you encountered and overcame.
This discussion aims to ensure a deep understanding of your submission and to confirm that
the work is entirely your own.

## Submission:

Submit your code through a version control repository (e.g., GitHub).
Include a README file with instructions on how to run your application and tests, and any
other relevant documentation.

## Timeline:

There is no strict time limit for this test, but a well-organised, thoroughly tested, and
complete submission is expected within a reasonable timeframe.
