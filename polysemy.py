import nltk
from nltk.corpus import brown

# Run the nltk downloader to download the Brown corpus
nltk.download('brown')

# Create a list of common nouns
nouns = [token for token, pos in brown.tagged_words(categories='news') if pos == 'NN']

# Create a list of informational content nouns
info_nouns = [word for word in nouns if 'message' in word or 'information' in word or 'knowledge' in word]

# Create a list of eventuality contexts
eventuality_contexts = []

# Loop through the sentences in the corpus
for sent in brown.sents():

    # Loop through the tokens in the sentence
    for i, token in enumerate(sent):

        # Check if the token is in the list of informational content nouns
        if token in info_nouns:

            # Check if the token is modified with a verb, PP, or other linguistic element that indicates an eventuality
            if i > 0 and sent[i-1] == token and sent[i] in ['is', 'was', 'were', 'will', 'would']:
                eventuality_contexts.append(sent)

            elif i > 0 and sent[i-1] == token and sent[i] in ['in', 'on', 'at', 'for', 'to']:
                eventuality_contexts.append(sent)

            elif i > 0 and sent[i-1] == token and sent[i] in ['more', 'less', 'longer', 'shorter', 'larger', 'smaller']:
                eventuality_contexts.append(sent)

# Create a list of intersection contexts
intersection_contexts = [context for context in eventuality_contexts if any(word in info_nouns for word in context)]

# Create a list of informational content contexts
info_contexts = []

# Loop through the sentences in the corpus
for sent in brown.sents():

    # Loop through the tokens in the sentence
    for i, token in enumerate(sent):

        # Check if the token is in the list of informational content nouns
        if token in info_nouns:

            # Check if the token is modified with a propositional complement clause or propositional predicate
            if i > 0 and sent[i-1] == token and sent[i] in ['that', 'whether']:
                info_contexts.append(sent)

            elif i > 0 and sent[i-1] == token and sent[i] in ['true', 'factual', 'false', 'misleading']:
                info_contexts.append(sent)

# Print out the list of informational content nouns
print('The following nouns can denote informational contents:')
print(info_nouns)

# Print out the list of eventuality contexts
print('The following contexts can denote eventualities:')
print(eventuality_contexts)

# Print out the list of intersection contexts
print('The following contexts denote both informational contents and eventualities:')
print(intersection_contexts)

# Print out the list of informational content contexts
print('The following contexts modify informational content nouns:')
print(info_contexts)
