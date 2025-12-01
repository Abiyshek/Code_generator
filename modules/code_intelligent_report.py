# code_intelligence_report.py

def build_cir_prompt(generated_code):
    """
    Build prompt to analyze code quality, security, and performance.
    """

    return f"""
    Analyze the following code and produce a **Code Intelligence Report (CIR)**.
    
    Code:
    {generated_code}

    The CIR must include:
    - Security vulnerabilities
    - Code smells
    - Performance bottlenecks
    - Memory usage analysis
    - Time complexity
    - Cyclomatic complexity
    - Recommended refactorings
    - Overall code grade (A, B, C, D)
    """
