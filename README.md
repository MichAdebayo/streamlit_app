# Sportizza Quiz Application

Welcome to the **Sportizza Quiz Application**! This project is a configurable and interactive football-themed quiz built with Streamlit. Users can design quizzes, answer football-related questions, track their scores, and receive feedback. The application leverages Pydantic for data validation to ensure that all questions follow the required format.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
  - [Configure the Quiz](#configure-the-quiz)
  - [Take the Quiz](#take-the-quiz)
- [File Structure](#file-structure)
- [Contributing](#contributing)

---

## Project Overview

This application enables users to create, edit, and participate in a customizable football quiz. Users can add questions, specify answer options, and assign correct answers. The app keeps track of the user’s score and provides instant feedback on each answer, with the option to restart the quiz upon completion.

## Features

- **Questionnaire Configuration**: Design custom quiz questions with up to four options per question.
- **Real-Time Validation**: Ensure questions follow the required format using Pydantic validators.
- **Score Tracking**: Track your score as you answer questions in real-time.
- **Instant Feedback**: Receive immediate feedback on each answer.
- **JSON Storage**: Save and load questionnaire data from a JSON file for persistence.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/sportizza-quiz.git
   cd sportizza-quiz
2. **Set up the virtual environment**:
    ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\\Scripts\\activate`
3. **Install dependencies**:
    ```bash
   pip install -r requirements.txt

4. **Run the application**:
    ```bash
   streamlit run main.py

## Usage

### 1. Configure the Quiz

**To create or modify quiz questions:**

- Toggle the **Configure your questionnaire** option after initializing the app using (`streamlit run main.py`).

- Select a question number and enter the question, options, and the correct answer.

- Click **Add or Update Question** to save your changes.

- Preview: View saved questions and options.

### 2. Take the Quiz

To participate in the quiz:

- Toggle the **Start quiz** navigation. The quiz is displayed afterwards.
- Answer the questions by clicking on the options (A, B, C, or D).
- Receive feedback and view your score at the end.
- Restart the quiz by clicking **Restart Quiz.**


## File Structure

```bash
sportizza-quiz/
├── questionnaire.py  # Main script to configure questions
├── quiz.py   # Main quiz interface for users
├── functions.py  # Helper functions to display questions
├── models/
│   └── question_model.py  # Data model with validation for questions
└── streamlit.json  # JSON file to store questions and answers
```


- `questionnaire.py`: Configure quiz questions and save them.

- `quiz.py`: User interface to answer questions and track scores.

- `functions.py`: Provides preview functionality for saved questions.

- `models/question_model.py`: Defines the question schema and validations with Pydantic.`

## Contributing

Contributions are welcome! To contribute:

1) Fork the repository.
2) Create a new branch with a descriptive name.
3) Commit your changes and push the branch.
4) Submit a pull request.


