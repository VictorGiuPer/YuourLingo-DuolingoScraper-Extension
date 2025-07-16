# import google.generativeai as genai
import pandas as pd

order_food = ["menu", "food", "drink", "order", "eat", "bread", "water", "waiter", "bill", "restaurant", "hungry"]
doctor = ["doctor", "appointment", "feel", "sick", "pain", "medicine", "head", "fever", "symptom"]
introduce = ["name", "live", "work", "job", "from", "old", "years", "language", "like", "hobby"]


scenario_concepts = {"ordering_food": order_food,
                     "doctor_appointment": doctor,
                     "self_introduction": introduce}

# Load Learned Words
spanish = pd.read_json("C:\\Users\\victo\\VSCode Folder\\Duolingo\\DuolingoSupport\\Data\\spanish.json")
french = pd.read_json("C:\\Users\\victo\\VSCode Folder\\Duolingo\\DuolingoSupport\\Data\\french.json")

# Rename the columns correctly
spanish.rename(columns={"Spanish": "Learning"}, inplace=True)
french.rename(columns={"French": "Learning"}, inplace=True)

# Filtering function
import re

def filter_vocab_by_concepts(df, scenario, concept_dict):
    concepts = concept_dict.get(scenario, [])
    concepts = [re.escape(c.lower()) for c in concepts]  # escape special characters
    pattern = r'\b(?:' + '|'.join(concepts) + r')\b'  # build regex pattern to match whole words only

    def matches_any_concept(translation):
        translation = translation.lower()
        return re.search(pattern, translation) is not None

    return df[df["Translation"].apply(matches_any_concept)]

filtered_food = filter_vocab_by_concepts(spanish, "ordering_food", scenario_concepts)