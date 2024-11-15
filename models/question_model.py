from pydantic import BaseModel,  conlist, PydanticUserError, field_validator, model_validator

class Question(BaseModel):
    question: str
    options: conlist(str, min_length=4, max_length=4)  # type: ignore # Validate 2 to 4 options
    correct_answer: str

    # Validate each questionaire entry

    @field_validator('question', check_fields=False)
    def validate_question(cls, value):
        if not value or isinstance(int(value), int):
            raise ValueError("Question cannot be empty or an integer. Add a question.")
        else:
            return value


    @field_validator('options', check_fields=False)
    def validate_options(cls, value):
        if len(value) != 4:
            raise ValueError("You must provide 4 options")
        return value

    @field_validator('correct_answer', check_fields=False)
    def validate_correct_answer(cls, value):
        if value not in ["A", "B", "C", "D"]:
            raise ValueError("The correct option can only be one of A, B, C, or D")
        return value

    # # Validation globale du modèle
    # @model_validator(mode="before")
    # def check_all_fields(cls, values):
    #     if not values or isinstance(values['questions'], int):
    #         raise ValueError("Question cannot be empty. Add a question.")
    #     if len(values['options']) != 4:
    #         raise ValueError("You must provide 4 options.")
    #     if values["correct_answer"] not in ["A", "B", "C", "D"]:
    #         raise ValueError("The correct option can only be one of A, B, C, or D")
    #     return values


