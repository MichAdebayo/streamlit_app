import streamlit as st
# import time

def quiz_page():
    st.title("Welcome to Sportizza")
    st.subheader("Ready to test your football knowledge?")
    # Initialize session state if not already present
    if "current_question_index" not in st.session_state:
        st.session_state["current_question_index"] = 0
        st.session_state["score"] = 0  # Store user's score
        #st.session_state["timer_start_time"] = time.time()  # Start timer for the first question
    
    # Get the current question index and the list of questions from session state
    current_question_index = st.session_state["current_question_index"]
    questions = st.session_state["questions"]
    
    if current_question_index < len(questions):
        question_data = questions[current_question_index]
        question = question_data["question"]
        options = question_data["options"]
        correct_answer = question_data["correct_answer"]
        
        # Display the current question
        st.write(f"**Question {current_question_index + 1}:** {question}")
        
        # Create clickable buttons for A, B, C, D options
        button_clicked = False
        for i, option in enumerate(options):
            if st.button(f"{chr(65 + i)}. {option}", key=f"option_{i}"):
                selected_option = chr(65 + i)  # Get the option corresponding to A, B, C, D
                button_clicked = True
                break
        
        if button_clicked:
            # Check if the answer is correct
            if selected_option == correct_answer:
                st.session_state["score"] += 1
                st.success(f"Correct answer: {selected_option}")
            else:
                st.error(f"Incorrect answer. Correct answer was: {correct_answer}")
            
            # Move to the next question after a short delay
            st.session_state["current_question_index"] += 1
            # st.session_state["timer_start_time"] = time.time()  # Reset the timer for the next question
            # time.sleep(1)  # Give a brief moment for feedback to be displayed
            st.rerun()  # Refresh the page to move to the next question

    else:
        # End of quiz
        st.write("Quiz Complete!")
        st.write(f"Your score: {st.session_state['score']} / {len(questions)}")
        
        # Reset button to start the quiz over
        if st.button("Restart Quiz"):
            st.session_state["current_question_index"] = 0
            st.session_state["score"] = 0
            # st.session_state["timer_start_time"] = time.time()  # Reset the timer for the new quiz
            st.rerun()  # Refresh the page to restart the quiz




