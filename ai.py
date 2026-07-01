import ollama

def ask_phi(prompt):
    response = ollama.chat(
        model="phi3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response["message"]["content"]




def ask_qwen(prompt):
    response = ollama.chat(
        model="qwen2.5:1.5b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]



def ask_ai(prompt):
    if pattern.search(prompt):
        return ask_phi(prompt)
    
    response = ask_qwen(prompt)
    
    if is_low_quality(response):
        response = ask_phi(prompt)
    
    return response

def is_low_quality(response):
    bad_phrases = ["i don't know", "i'm not sure", "unable to", "as an ai"]
    return (
        len(response.strip()) < 15
        or any(p in response.lower() for p in bad_phrases)
    )

hard_keywords = [
    # Debugging / troubleshooting
    "debug", "error", "exception", "traceback", "not working",
    "fix this", "bug", "crash", "stack trace",

    # Algorithms / DSA
    "algorithm", "time complexity", "space complexity", "big o",
    "optimize", "optimization", "recursive", "recursion",
    "dynamic programming", "leetcode",

    # Deep reasoning / explanation
    "explain deeply", "explain in detail", "step by step",
    "why does", "how does", "prove", "derive", "derivation",

    # Math / stats
    "calculate", "equation", "integral", "derivative", "probability",
    "matrix", "vector", "theorem",

    # System design / architecture
    "architecture", "design pattern", "system design", "scalability",
    "trade-off", "tradeoff",

    # Code generation / review
    "refactor", "code review", "write a function", "implement",
    "unit test", "edge case",

    # Multi-step / research
    "compare", "difference between", "pros and cons", "analyze",
    "summarize research", "literature review"
]

import re


pattern = re.compile(r"\b(" + "|".join(re.escape(k) for k in hard_keywords) + r")\b", re.IGNORECASE)

# def ask_ai(prompt):
#     if pattern.search(prompt):
#         return ask_phi(prompt)
#     return ask_qwen(prompt)