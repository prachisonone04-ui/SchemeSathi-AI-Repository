def get_language_instruction(language):
    instructions = {
        "मराठी": "उत्तर सोप्या मराठी भाषेत द्या.",
        "हिंदी": "उत्तर सरल हिंदी भाषा में दें।",
        "English": "Answer in simple English."
    }

    return instructions.get(
        language,
        "Answer in simple English."
    )