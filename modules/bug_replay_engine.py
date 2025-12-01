# bug_replay_engine.py

def build_bug_replay_prompt(buggy_code):
    """
    Create a prompt where AI simulates running the code and reproducing the bug.
    """

    return f"""
    You are a bug replay engine.

    I will give you code that contains an error.
    Your job is to:

    1. Simulate running the code.
    2. Reproduce the exact error message a compiler or runtime would show.
    3. Show the failing line.
    4. Explain the root cause.
    5. Fix the code.
    6. Show the corrected output.
    
    Code:
    {buggy_code}
    """
