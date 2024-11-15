# import streamlit as st
# import json
# import os
# from pydantic import BaseModel, field_validator, model_validator, ValidationError
# from typing import List

# st.markdown("# Création d'un quiz🎉")
# st.sidebar.markdown("# Créer un quiz 🎉")

# if 'reset' not in st.session_state:
#     st.session_state.reset = False

# # Clear input fields by checking the reset flag
# if st.session_state.reset:
#     st.session_state["question"] = ''
#     st.session_state["answer_1"] = ''
#     st.session_state["answer_2"] = ''
#     st.session_state["answer_3"] = ''
#     st.session_state["answer_4"] = ''
#     st.session_state["good_answer"] = ''
#     # Set the reset flag back to False
#     st.session_state.reset = False


# class Quiz(BaseModel):
#     question: str
#     answers: List[str]
#     good_answer: int

#     # Validations des champs individuels
#     @field_validator('question')
#     def validate_question(cls, value):
#         if not value:
#             raise ValueError("La question ne peut pas être vide.")
#         return value

#     @field_validator('answers')
#     def validate_answers(cls, value):
#         if len(value) != 4:
#             raise ValueError("Il faut exactement 4 réponses possibles.")
#         if any(not answer for answer in value):
#             raise ValueError("Toutes les réponses doivent être renseignées.")
#         return value

#     @field_validator('good_answer')
#     def validate_good_answer(cls, value):
#         if value not in [1, 2, 3, 4]:
#             raise ValueError("La réponse correcte doit être un chiffre entre 1 et 4.")
#         return value

#     # Validation globale du modèle
#     @model_validator(mode="before")
#     def check_all_fields(cls, values):
#         if not values.get('question'):
#             raise ValueError("La question ne peut pas être vide.")
#         if len(values['answers']) != 4:
#             raise ValueError("Il faut exactement 4 réponses possibles.")
#         if values["good_answer"] not in ["1", "2", "3", "4"]:
#             raise ValueError("La réponse correcte doit être un nombre entre 1 et 4.")
#         return values


# question = st.text_input('Type a question', key="question")
# # answer_number = st.text_input('Type a number of possible answers', key="answer_number")
# # number_list = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eigth"]
# # for i in range(answer_number):
# # st
# answer_1 = st.text_input('Type the first possible answer', key="answer_1")
# answer_2 = st.text_input('Type the second possible answer', key="answer_2")
# answer_3 = st.text_input('Type the third possible answer', key="answer_3")
# answer_4 = st.text_input('Type the fourth possible answer', key="answer_4")
# good_answer = st.text_input('Type the number of the good answer', key="good_answer")


# if st.button('Save your question'):
#     # with open('quiz_data.json', 'w') as file:
#     #     json.dump({"Question :" : question, "Answers :" : [answer_1,answer_2,answer_3,answer_4], "good_answer :" : good_answer}, file)

#     try:
#         # Valider l'objet Quiz avec les données saisies
#         quiz_data = Quiz(
#             question=question,
#             answers=[answer_1, answer_2, answer_3, answer_4],
#             good_answer=good_answer
#         )

#         if os.path.exists('quiz_data.json'):
#         # Open the file and load the existing data
#             with open('quiz_data.json', 'r') as file:
#                 data = json.load(file)
            
#             # Add the new question to the data (assuming it's a list of questions)
#             data.append({"Question :" : question, "Answers :" : [answer_1,answer_2,answer_3,answer_4], "good_answer :" : good_answer})
#         else:
#             # If the file doesn't exist, start with an empty list
#             data = [{"Question :" : question, "Answers :" : [answer_1,answer_2,answer_3,answer_4], "good_answer :" : good_answer}]

#         # Write the updated data back to the JSON file
#         with open('quiz_data.json', 'w') as file:
#             json.dump(data, file, indent=4)
        
#         st.session_state.reset = True

#         st.rerun()

#     except ValidationError as e:
#         # Afficher les erreurs de validation
#         st.error(f"Erreur de validation : {e}")



# def launch_session_state():
#     # Load questions from JSON if it exists and session state is empty
#     if "questions" not in st.session_state:
#         if os.path.exists('streamlit.json'):
#             with open('streamlit.json', 'r') as file:
#                 st.session_state["questions"] = json.load(file)
#         else:
#             st.session_state["questions"] = []



