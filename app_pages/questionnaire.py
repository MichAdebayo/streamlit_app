# sourcery skip: avoid-builtin-shadow
import json
import os
import streamlit as st
from models.question_model import Question  # Import the validation function
from pydantic import ValidationError
from functions import preview_question

def configure_questionnaire() -> None:   

    st.title("Configure Quiz")
    st.subheader("Start designing your questionnaire")

    # Reload from JSON if questions are missing in session state
    if "questions" not in st.session_state or not st.session_state["questions"]:
        if os.path.exists('streamlit.json'):
            with open('streamlit.json', 'r') as file:
                st.session_state["questions"] = json.load(file)
        else:
            st.session_state["questions"] = []

    # Add "--" as a default option along with question numbers
    question_numbers = ["Select question"] + list(range(1, 12))
    selected_question_number = st.selectbox("", question_numbers)

    # Load existing question data if a specific number is selected, otherwise clear
    if selected_question_number != "Select question":
        # Check if selected question number already exists
        existing_question = next((q for q in st.session_state["questions"] if q.get('number') == selected_question_number), None)

        # Prepopulate inputs if editing an existing question
        question_text = existing_question["question"] if existing_question else ""
        options_text = ", ".join(existing_question["options"]) if existing_question else ""
        correct_answer_text = existing_question["correct_answer"] if existing_question else ""
    else:
        # Set fields to blank if "--" is selected
        question_text = ""
        options_text = ""
        correct_answer_text = ""

    # Form to enter or update question data
    with st.form("config_page", clear_on_submit=True, enter_to_submit=False):
        question_input = st.text_input("Enter Question", value=question_text, key="questions_widget")
        options_input = st.text_area("Enter Answer Options (separate by commas)", value=options_text, key="response_widget")
        correct_answer_input = st.text_input("Enter Correct Answer (e.g., A, B, C...)", value=correct_answer_text, key="true_widget")

        # Split the options to individuals values
        options_list = [option.strip() for option in options_input.split(",")]

        # Add button to update or add question
        add_or_update_question = st.form_submit_button("Add or Update Question")

        # If button clicked and the selected number is a real number
        if add_or_update_question and selected_question_number != "Select question":
            
            # Prepare data for validation
            question_data = {
                "number": selected_question_number,
                "question": question_input,
                "options": options_list,
                "correct_answer": correct_answer_input.upper()
            }

            # Validate and save question
            try:
                validated_question = Question(**question_data)

                # Check if existing_question is defined
                if 'existing_question' in locals() and existing_question:
                    existing_question.update(validated_question.model_dump())
                else:
                    st.session_state["questions"].append(validated_question.model_dump())

                # Save to JSON file
                # Load existing questions if the file exists
                try:
                    with open('streamlit.json', 'r') as file:
                        existing_questions = json.load(file)
                except FileNotFoundError:
                    existing_questions = []

                # Append new question to the existing list
                existing_questions.append(validated_question.model_dump())

                # Write the updated list back to the JSON file
                with open('streamlit.json', 'w') as file:
                    json.dump(existing_questions, file, indent=2, separators=(",", ":"))

                st.success(f"Question {selected_question_number} saved!")

            except ValidationError as e:
                # Display validation error if present
                st.error(f"Validation Error: {e}")

            st.rerun()

    # Display saved questions
    #preview_question() 
    # Display saved questions
    st.write("## Questions Preview")
    for q in st.session_state["questions"]:
        st.write(f"**Question {q['number']}:** {q['question']}")
        for option, value in zip(["A", "B", "C", "D"], q['options']):
            st.write(f"{option}. {value}")
        st.write(f"Correct answer is: **{q['correct_answer']}**")  