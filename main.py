#!/usr/bin/python3
import nltk

# Enter sentence
sentence = input("Enter your sentence: ")
# 1. Split on tokens
tokens = nltk.word_tokenize(sentence)
print("Split on tokens: ", tokens)
# 2. Part of speech
posttagged = nltk.pos_tag(tokens)
print("Post tagged: ", posttagged)
# 3. If not imperative mood - exit program
print("--------------------------------")
imperative = False

# take first part, that consist Subject OR first verb (nltk tags it in a weird way)
parted = []
for w in posttagged:            # most common tags for an imperative verb
    if w[1] not in ['PRP', 'NNP', 'IN', 'NN', 'VB', 'VBP']:
        parted.append(w)
    else:
        parted.append(w)
        break


# Check only in first part of tags
for each in parted:
    action = space = ''

    if each[1] in ('NNP', 'IN', 'NN'):
        is_verb = "To " + each[0]
        is_verb_pos = nltk.pos_tag(nltk.word_tokenize(is_verb))
        if is_verb_pos[1][1] == 'VB':
            action = each[0]
            imperative = True

    elif each[1] == 'VB':
        action = each[0]
        imperative = True

    elif each[1] == 'VBP':
        if posttagged[posttagged.index(each)+1][1] != 'RB':
            if parted[parted.index(each)-1] != parted[-1]:
                action = parted[parted.index(each)-1][0] + ' ' + each[0]
            else:
                action = each[0]
            imperative = True
        else:
            action = each[0] + posttagged[posttagged.index(each)+1][0]
            imperative = True

    if imperative is True:
        space = sentence.replace(action+' ', '', 1)

    if space:
        print('Action:', action)
        print('Object:', space)
        break
