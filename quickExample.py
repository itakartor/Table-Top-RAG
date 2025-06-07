
corpus_of_documents = [
    "Take a leisurely walk in the park and enjoy the fresh air.",
    "Visit a local museum and discover something new.",
    "Attend a live music concert and feel the rhythm.",
    "Go for a hike and admire the natural scenery.",
    "Have a picnic with friends and share some laughs.",
    "Explore a new cuisine by dining at an ethnic restaurant.",
    "Take a yoga class and stretch your body and mind.",
    "Join a local sports league and enjoy some friendly competition.",
    "Attend a workshop or lecture on a topic you're interested in.",
    "Visit an amusement park and ride the roller coasters."
]

def jaccard_similarity(query:str, document:str) -> float:
    """is similarity measure for compare query and document of knlowledge base."""
    query = query.lower().split(" ")
    document = document.lower().split(" ")
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection)/len(union)

def return_response(user_input:str, corpus:list) -> str:
    """Returns the most similar document from the corpus based on Jaccard similarity."""
    similarities = []
    for doc in corpus:
        similarity = jaccard_similarity(user_input, doc)
        similarities.append(similarity)
    print(f"Similarities: {similarities}")
    return corpus_of_documents[similarities.index(max(similarities))]

def main():
    """Main function to demonstrate the response generation."""
    user_prompt:str = "What is a leisure activity that you like?"
    print(user_prompt)
    user_input:str = "I like to go in a park"
    response:str = return_response(user_input, corpus_of_documents)
    print(f"Response: {response}")

if __name__ == "__main__":
    main()
