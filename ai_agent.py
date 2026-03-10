from groq import Groq

client = Groq(api_key="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")

def analyze_resume(resume_text):

    prompt = f"""
    Analyze the following resume and provide:

    1. Skills identified
    2. Skill gaps
    3. Career suggestions
    4. Learning roadmap

    Resume:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content