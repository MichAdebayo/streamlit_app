# sourcery skip: avoid-builtin-shadow
import json
import os
import streamlit as st
from models.question_model import Question
from pydantic import ValidationError
from preview import preview_question

def configure_questionnaire():
    """
    Provides a visually enhanced interface for creating, updating, and managing quiz questions.

    This function offers a structured layout for questionnaire configuration.
    Users can add new questions through an expander form and view, edit, or delete
    existing questions listed below. The state is managed using Streamlit's
    session state, and questions are persisted in a JSON file.

    Args:
        None

    Returns:
        None
    """
    st.title("📝 Questionnaire Builder")
    st.subheader("Design and manage your quiz questions.")

    # Initialize session state for questions if it doesn't exist
    if "questions" not in st.session_state:
        if os.path.exists('streamlit.json'):
            try:
                with open('streamlit.json', 'r') as file:
                    st.session_state["questions"] = json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                st.session_state["questions"] = []
        else:
            st.session_state["questions"] = []

    # --- Form for Adding a New Question ---
    with st.expander("➕ Add a New Question", expanded=False):
        with st.form("new_question_form", clear_on_submit=True):
            st.markdown("### New Question Details")
            question_input = st.text_input("Enter the question")
            options_input = st.text_area("Enter answer options, separated by commas")
            correct_answer_input = st.text_input("Enter the correct option (e.g., A, B, C)")

            submitted = st.form_submit_button("Save Question")
            if submitted:
                options_list = [opt.strip() for opt in options_input.split(",") if opt.strip()]
                
                # New questions are assigned the next available number
                new_question_number = len(st.session_state["questions"]) + 1

                question_data = {
                    "number": new_question_number,
                    "question": question_input,
                    "options": options_list,
                    "correct_answer": correct_answer_input.upper()
                }

                try:
                    # Validate data using Pydantic model
                    validated_question = Question(**question_data)
                    st.session_state["questions"].append(validated_question.model_dump())
                    
                    # Save all questions to JSON file
                    save_questions_to_file()
                    st.success(f"Question {new_question_number} has been added successfully!")
                except ValidationError as e:
                    st.error(f"Validation Error: {e}")
                
                st.rerun()

    st.markdown("---")
    st.subheader("📖 Existing Questions")

    # Display existing questions for editing or viewing
    if not st.session_state["questions"]:
        st.info("No questions have been added yet. Use the form above to add one.")
    else:
        for idx, q in enumerate(st.session_state["questions"]):
            with st.container():
                st.markdown(f"**Q{idx + 1}: {q['question']}**")
                
                cols = st.columns([0.8, 0.1, 0.1])
                with cols[0]:
                    st.write(f"Options: {', '.join(q['options'])}")
                    st.write(f"Correct Answer: {q['correct_answer']}")
                
                with cols[1]:
                    if st.button("✏️", key=f"edit_{idx}"):
                        # For simplicity, editing can be handled by instructing user to delete and re-add
                        # A more complex implementation would involve a modal or separate form
                        st.info("To edit, please delete this question and add a new one with the updated details.")

                with cols[2]:
                    if st.button("🗑️", key=f"delete_{idx}"):
                        st.session_state["questions"].pop(idx)
                        save_questions_to_file()
                        st.rerun()
                st.markdown("---")

    # Display a preview of all saved questions
    if st.session_state["questions"]:
        st.subheader("📋 Live Preview")
        preview_question()

def save_questions_to_file():
    """
    Saves the current list of questions from the session state to 'streamlit.json'.
    """
    try:
        with open('streamlit.json', 'w') as file:
            # Re-number questions to ensure they are sequential
            for i, question in enumerate(st.session_state["questions"]):
                question['number'] = i + 1
            json.dump(st.session_state["questions"], file, indent=4)
    except IOError as e:
        st.error(f"Could not save questions to file: {e}")

