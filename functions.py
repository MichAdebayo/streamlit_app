
import streamlit as st

# def launch_session_state():
#     # Load questions from JSON if it exists and session state is empty
#     if "questions" not in st.session_state:
#         if os.path.exists('streamlit.json'):
#             with open('streamlit.json', 'r') as file:
#                 st.session_state["questions"] = json.load(file)
#         else:
#             st.session_state["questions"] = []


# Display saved questions
def preview_question():
    st.write("## Questions Preview")
    for q in st.session_state["questions"]:
        st.write(f"**Question {q['number']}:** {q['question']}")
        for option, value in zip(["A", "B", "C", "D"], q['options']):
            st.write(f"{option}. {value}")
        st.write(f"Correct answer is: **{q['correct_answer']}**")




