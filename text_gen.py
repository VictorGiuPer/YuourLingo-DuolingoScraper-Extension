import pandas as pd
from vocabulary_choice import filtered_food
import google.generativeai as genai

genai.configure(api_key="AIzaSyDrKGFenMjGYeybKI3gyRl_skmrx2fqTNI")

# Scenario Choice
chosen_scenario = "Restaurant Visit with a Friend"

# Learned Words (from df column to string)
word_string = ", ".join(filtered_food["Learning"].astype(str).tolist())

prompt = f"""
You are a language teacher helping a beginner learn a foreign language.

Write a short and simple story in the target language (no English) about the following situation:

{chosen_scenario}

The learner already knows these words:
{word_string}

Instructions:
- Use these known words naturally throughout the story. Do not force them.
- Do NOT force words that don’t belong.
- Highlight each used word from the list with double asterisks like this: **palabra**
- Make the story feel realistic and smooth — not just a list of words.
- Keep the grammar simple, A2 level.
- The story should be about 300 words.
- Output ONLY the story, with no additional explanation.
"""


def get_gemini_response(prompt: str) -> str:
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

response_text = get_gemini_response(prompt)
print(response_text)