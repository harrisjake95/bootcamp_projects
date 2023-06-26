import spacy

# A list of two garden path sentences and the additional given sentences
gardenpathSentences = [
    "The old man the boats.",
    "The sour drink from the ocean.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Load the English NLP model
nlp = spacy.load('en_core_web_sm')

# Tokenize each sentence and execute named entity recognition
for sentence in gardenpathSentences:
    doc = nlp(sentence)

    # Print the entities in the sentence
    print(f'Entities in the sentence "{sentence}" are:')
    for ent in doc.ents:
        print(f'{ent.text} ({ent.label_})')

# Using spacy.explain to understand some entities
print("\nExplanation of some entities:")
print("GPE:", spacy.explain("GPE"))
print("PERSON:", spacy.explain("PERSON"))

# Comments
# 1. GPE entity refers to Countries, cities, states. It makes sense in the context of the last sentence where 'Mississippi' is a GPE entity.
# 2. PERSON entity refers to People, including fictional. It makes sense in the context of the third sentence where 'Mary' is a PERSON entity.