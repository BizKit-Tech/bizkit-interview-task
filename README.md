# BizKit Interview Task

You did it! After a grueling interview process, you are now an official employee of Phasebook, Mark Zuckerberg's younger brother, Marc Zuckerberg's startup.

With Phasebook, you can keep track of, chat about, and share with others the different phases of your life.

This repository contains some of Phasebook's core code. Your task, as a fresh hire, is to set up the repository, implement some improvements, and develop a new feature!

Read on below to see what you need to do.

**Important Note:** This project was built using [Flask](https://flask.palletsprojects.com/en/2.2.x/), and while it's not necessary that you know Flask to finish the tasks here, it would help for you to read at least a bit about it.

## Getting Started

Your first task is, of course, to set up the Phasebook repository on your local machine by following these instructions:

1. Install [Python](https://www.python.org/downloads/) on your machine. The version should be at least 3.10.
2. Click on `Use this template` to create your own copy of this repository then clone it to your local machine.
3. Open a terminal and `cd` into the folder of the cloned repository.
4. Run the following commands based on your OS to create a virtual environment and activate it:

   **Windows:**
    ```
    py -3 -m venv venv
    venv\Scripts\activate
    ```

    **macOS/Linux:**
    ```
    python3 -m venv venv
    . venv/bin/activate
    ```

    *Note: Whenever you run this project, you need to activate the virtual environment first.*

5. Install the dependencies using the following command:
    ```
    pip install -r requirements.txt
    ```
6. Run the application with the command:
    ```
    flask --app phasebook --debug run
    ```
7. Open the url printed on the terminal: `http://127.0.0.1:5000` using your browser or a tool like [Postman](https://www.postman.com). You should get a text saying `Hello World!`.


## Improve the Matching Algorithm
Phasebook has a "matching" feature that allows users to match and chat with other users with similar interests. One aspect of this feature is matching users based on their favorite numbers.

To the team's surprise, however, some users ended up having long lists of favorite numbers, causing the matching algorithm to take a while to process.

Your task is to now optimize the matching algorithm so that users can find out if they have a match faster.

### Technical Information
- The match endpoint is: http://127.0.0.1:5000/match/{match_id}.
- Specifically, you need to optimize the `is_match` function under `phasebook/match.py`.
- The function should return `True` when all numbers in `fave_numbers_2` can be found in `fave_numbers_1`. Otherwise, it should return `False`.
- You can use the following `{match_id}` to test: `0`, `1`, `2`, `3`. Example: http://127.0.0.1:5000/match/3.

## Implement a Search Algorithm

Currently, Phasebook users find each other only by providing each other their profile links. But to improve user experience, Phasebook wants you to help implement search functionality.

### Technical Information
- The search endpoint is: http://127.0.0.1:5000/search. The user can pass the following query parameters:
  - id
  - name
  - age
  - occupation
- Specifically, you need to implement the `search_users` function under `phasebook/search.py`.
- **(IMPORTANT)** The function should return the list of users that match the search parameters, as defined in the **Search Specifications** section.
- You can test the search functionality using the data in the `USERS` constant.
- Example calls to the search endpoint are:
  - http://127.0.0.1:5000/search?id=1
  - http://127.0.0.1:5000/search?name=Joe
  - http://127.0.0.1:5000/search?id=5&name=Joe&age=25&occupation=Dev

### Search Specifications
- All of the search parameters are optional. That means a user can pass no search parameter and the function should return all users. The user can also pass just the `id` as a parameter and it should just return the user with that `id`. The user can also pass multiple parameters and the function should return all the users that match **ANY** of the parameters provided.
- The `id` is unique. If the `id` is included in the search parameters, then immediately include the user with the passed `id`.
- The `name` can be partially matched and is case insensitive. That means that if we have users with names John Doe, Jane Doe, and Joe Doe, passing the word "doe" to the `name` parameter should include all of them in the results.
- The `age` parameter should include users that are in the range of `age - 1` to `age + 1`. This means that if we pass 26 to the `age` parameter, we should include users with ages 25 to 27.
- The `occupation` parameter can be partially matched and is case insensitive. This means that if we pass "er" to the `occupation` parameter, we should include all users with an `occupation` that contains "er" in the results.
- Do not include a user in the results more than once.

### Examples
Given the following users:
```
[
    {"id": "1", "name": "John Doe", "age": 29, "occupation": "Developer"},
    {"id": "2", "name": "Jane Doe", "age": 30, "occupation": "Engineer"},
    {"id": "3", "name": "Joe Doe", "age": 25, "occupation": "Designer"},
    {"id": "4", "name": "John Smith", "age": 28, "occupation": "Architect"},
    {"id": "5", "name": "Jane Smith", "age": 31, "occupation": "Manager"},
    {"id": "6", "name": "Joe Smith", "age": 24, "occupation": "Designer"}
]
```
- **Request:** http://127.0.0.1:5000/search?id=1

  **Result:**
  ```
  [
    {"id": "1", "name": "John Doe", "age": 29, "occupation": "Developer"}
  ]
  ```

- **Request:** http://127.0.0.1:5000/search?id=2&name=John

  **Result:**
  ```
  [
    {"id": "1", "name": "John Doe", "age": 29, "occupation": "Developer"},
    {"id": "2", "name": "Jane Doe", "age": 30, "occupation": "Engineer"},
    {"id": "4", "name": "John Smith", "age": 28, "occupation": "Architect"}
  ]
  ```

- **Request:** http://127.0.0.1:5000/search?age=28

  **Result:**
  ```
  [
    {"id": "1", "name": "John Doe", "age": 29, "occupation": "Developer"},
    {"id": "4", "name": "John Smith", "age": 28, "occupation": "Architect"}
  ]
  ```

- **Request:** http://127.0.0.1:5000/search?id=5&name=Joe&age=30&occupation=Arc

  **Result:**
  ```
  [
    {"id": "1", "name": "John Doe", "age": 29, "occupation": "Developer"},
    {"id": "2", "name": "Jane Doe", "age": 30, "occupation": "Engineer"},
    {"id": "3", "name": "Joe Doe", "age": 25, "occupation": "Designer"},
    {"id": "4", "name": "John Smith", "age": 28, "occupation": "Architect"},
    {"id": "5", "name": "Jane Smith", "age": 31, "occupation": "Manager"},
    {"id": "6", "name": "Joe Smith", "age": 24, "occupation": "Designer"}
  ]
  ```

## Bonus Challenge
If you're someone who likes to go the extra mile, then this is for you! As an extra challenge, return the search results sorted based on the following priority on how they were matched:
- `id`
- `name`
- `age`
- `occupation`

That means that with the examples above, the following request: http://127.0.0.1:5000/search?id=5&name=Joe&age=30&occupation=Arc, should return:
```
  [
    {"id": "5", "name": "Jane Smith", "age": 31, "occupation": "Manager"},
    {"id": "3", "name": "Joe Doe", "age": 25, "occupation": "Designer"},
    {"id": "6", "name": "Joe Smith", "age": 24, "occupation": "Designer"},
    {"id": "1", "name": "John Doe", "age": 29, "occupation": "Developer"},
    {"id": "2", "name": "Jane Doe", "age": 30, "occupation": "Engineer"},
    {"id": "4", "name": "John Smith", "age": 28, "occupation": "Architect"}
  ]
  ```
