import random

def get_determiner(quantity):
    """Return a randomly chosen determiner."""
    determiners = ["a", "one", "the"] if quantity == 1 else ["some", "many", "the"]
    return random.choice(determiners)

def get_noun(quantity):
    """Return a randomly chosen noun."""
    nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit"] if quantity == 1 \
        else ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits"]
    return random.choice(nouns)

def get_verb(quantity, tense):
    """Return a randomly chosen verb based on tense."""
    past = ["drank", "ate", "ran", "laughed", "talked"]
    present_singular = ["drinks", "eats", "runs", "laughs", "talks"]
    present_plural = ["drink", "eat", "run", "laugh", "talk"]
    future = ["will drink", "will eat", "will run", "will laugh", "will talk"]
    
    if tense == "past":
        return random.choice(past)
    elif tense == "present":
        return random.choice(present_singular if quantity == 1 else present_plural)
    else:  # future
        return random.choice(future)

def get_preposition():
    """Return a randomly chosen preposition."""
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    return random.choice(prepositions)

def get_adjective():
    """Return a randomly chosen adjective."""
    adjectives = ["red", "fast", "tall", "smart", "dinky", "busy", "sweet", "calm"]
    return random.choice(adjectives)

def get_adverb():
    """Return a randomly chosen adverb."""
    adverbs = ["quickly", "sweetly", "calmly", "happily", "silently"]
    return random.choice(adverbs)

def get_prepositional_phrase(quantity):
    """Return a prepositional phrase."""
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    adjective = get_adjective()
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {adjective} {noun}"

def make_sentence(quantity, tense):
    """Generate a sentence with a determiner, adjective, noun, verb, adverb, and two prepositional phrases."""
    determiner = get_determiner(quantity).capitalize()
    adjective = get_adjective()
    noun = get_noun(quantity)
    adverb = get_adverb()
    verb = get_verb(quantity, tense)
    prepositional_phrase1 = get_prepositional_phrase(quantity)
    prepositional_phrase2 = get_prepositional_phrase(quantity)
    return f"{determiner} {adjective} {noun} {prepositional_phrase1} {adverb} {verb} {prepositional_phrase2}."

def main():
    """Generate and print six sentences."""
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

if __name__ == "__main__":
    main()
