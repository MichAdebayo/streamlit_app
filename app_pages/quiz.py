import streamlit as st
import json
import os
import time

def quiz_page():
    """
    Renders a visually appealing, app-like quiz page for the Sportizza application.

    This function enhances the user experience with a modern layout, including a
    progress bar, score display, and styled question cards. It manages the quiz
    state through Streamlit's session state, guiding the user through the questions
    and providing instant feedback. At the end of the quiz, it presents a detailed
    summary of the results and allows the user to restart.

    Args:
        None

    Returns:
        None
    """
    st.title("🏆 Sportizza Quiz Challenge")
    st.subheader("Ready to showcase your football knowledge?")

    # Custom CSS for a more polished, app-like feel
    st.markdown("""
        <style>
            .stButton>button {
                width: 100%;
                border-radius: 10px;
                padding: 10px 0;
                margin: 5px 0;
                border: 2px solid #4CAF50;
                background-color: transparent;
                color: #4CAF50;
                transition: all 0.3s ease;
            }
            .stButton>button:hover {
                background-color: #4CAF50;
                color: white;
            }
            .question-card {
                background-color: #f9f9f9;
                border-radius: 15px;
                padding: 25px;
                margin-bottom: 20px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            .results-card {
                background-color: #e8f5e9;
                border-left: 7px solid #4CAF50;
                padding: 20px;
                border-radius: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Load questions from the JSON file
    try:
        if os.path.exists('streamlit.json'):
            with open('streamlit.json', 'r') as file:
                questions = json.load(file)
        else:
            questions = []
    except (json.JSONDecodeError, FileNotFoundError):
        questions = []

    if not questions:
        st.warning("No quiz questions found. Please go to the 'Questionnaire' page to create some first.")
        return

    # Initialize or reset session state for the quiz
    if "current_question_index" not in st.session_state or st.session_state.get("questions_loaded") != questions:
        st.session_state.current_question_index = 0
        st.session_state.score = 0
        st.session_state.user_answers = [""] * len(questions)
        st.session_state.questions_loaded = questions

    current_index = st.session_state.current_question_index

    if current_index < len(questions):
        # --- Quiz in Progress ---
        question_data = questions[current_index]
        
        # Display progress and score
        st.progress((current_index) / len(questions))
        st.info(f"Score: {st.session_state.score}/{len(questions)}")

        with st.container():
            st.markdown('<div class="question-card">', unsafe_allow_html=True)
            st.markdown(f"<h4>Question {current_index + 1}</h4>", unsafe_allow_html=True)
            st.write(f"**{question_data['question']}**")

            # Display options in two columns for a cleaner look
            cols = st.columns(2)
            for i, option in enumerate(question_data["options"]):
                with cols[i % 2]:
                    if st.button(option, key=f"option_{i}"):
                        selected_option_char = chr(65 + i)
                        st.session_state.user_answers[current_index] = selected_option_char
                        
                        # Provide feedback on the answer
                        if selected_option_char == question_data["correct_answer"]:
                            st.session_state.score += 1
                            st.success("That's correct! 🎉")
                        else:
                            st.error(f"Not quite! The correct answer was {question_data['correct_answer']}.")
                        
                        # Pause briefly before moving to the next question
                        time.sleep(1)
                        st.session_state.current_question_index += 1
                        st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    else:
        # --- End of Quiz ---
        st.balloons()
        st.success("Quiz Complete!")
        
        st.markdown('<div class="results-card">', unsafe_allow_html=True)
        st.markdown(f"### Your Final Score: **{st.session_state.score} out of {len(questions)}**")
        
        # Display a summary of answers
        st.write("**Your Answers:**")
        for i, q in enumerate(questions):
            user_ans = st.session_state.user_answers[i]
            correct_ans = q['correct_answer']
            if user_ans == correct_ans:
                st.write(f"Q{i+1}: {q['question']} - Your answer: {user_ans} (✔️ Correct)")
            else:
                st.write(f"Q{i+1}: {q['question']} - Your answer: {user_ans} (❌ Incorrect, Correct was: {correct_ans})")
        st.markdown('</div>', unsafe_allow_html=True)

        # Restart button
        if st.button("🔄 Restart Quiz", key="restart"):
            # Reset state for a new quiz attempt
            st.session_state.current_question_index = 0
            st.session_state.score = 0
            st.session_state.user_answers = [None] * len(questions)
            st.rerun()
