# Python Quiz Application

A simple, interactive Python-based quiz application. This program allows users to answer multiple-choice questions, tracks their results, and provides feedback. The quiz is customizable and supports validation to ensure questions and options align correctly.

## Features

- **Multiple Choice Questions**: Users answer questions with options (A, B, C, D).  
- **Score Calculation**: Calculates and displays the user's score at the end of the quiz.  
- **Attempts Management**: Users are allowed multiple attempts to retake the quiz.  
- **Input Validation**: Ensures only valid inputs (A, B, C, or D) are accepted.  
- **Error Handling**: Checks if the number of questions and options are aligned before starting the quiz.  

---

## File Structure

- **main.py**  
  The main script to execute the quiz. Includes logic for displaying questions, validating answers, and calculating scores.  

- **quiz_data.py**  
  Contains the questions, their correct answers, and the corresponding options. Also includes acceptable "yes" responses for retrying the quiz.  

---

## Example Usage

```plaintext
1- Who created Python: 
    A. Dennis Ritchie
    B. Guido van Rossum
    C. James Gosling
    D. Bjarne Stroustrup
    Enter (A, B, C, or D): B

2- In what year was Python first released: 
    A. 1989
    B. 1991
    C. 1995
    D. 2000
    Enter (A, B, C, or D): B

---------------------------
        RESULTS
---------------------------
Your Answers: B B 
Correct Answers: B B 
Your score is 100 %
---------------------------
