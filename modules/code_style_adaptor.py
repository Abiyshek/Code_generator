# code_style_adaptor.py

def build_adaptive_prompt(base_prompt, level):
    """
    Create a learner-level–specific prompt.
    """

    level = level.lower()

    if level == "noob":
        style = """
        Explain in very simple beginner language.
        Add comments for every line.
        Use extremely basic constructs.
        Avoid pointers, recursion, and advanced logic.
        Provide examples for each concept.
        """
    elif level == "beginner":
        style = """
        Explain simply.
        Add comments for core logic.
        Use basic loops and conditionals.
        Avoid overly complex structures.
        """
    elif level == "intermediate":
        style = """
        Use standard programming techniques.
        Include clean explanations.
        Minimal but useful comments.
        """
    else:  # expert
        style = """
        Use advanced and optimized code.
        No basic explanations.
        Add only architecture-level notes.
        """

    adaptive_prompt = f"""
    {base_prompt}

    The user is a {level} programmer.
    Adapt the code and explanation as follows:
    {style}
    """

    return adaptive_prompt
