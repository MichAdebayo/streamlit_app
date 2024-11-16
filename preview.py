import streamlit as st

# Display saved questions
def preview_question():
    st.write("## Questions Preview")
    for q in st.session_state["questions"]:
        st.write(f"**Question {q['number']}:** {q['question']}")
        for option, value in zip(["A", "B", "C", "D"], q['options']):
            st.write(f"{option}. {value}")
        st.write(f"Correct answer is: **{q['correct_answer']}**")



