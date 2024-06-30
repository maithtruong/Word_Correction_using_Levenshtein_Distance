import streamlit as st
import nltk
from nltk.corpus import brown
from levenshtein_distance import levenshtein_distance

# Download the 'brown' corpus
nltk.download('brown')

# Load the vocabulary from the 'brown' corpus
vocabs = brown.words()

def main():
    st.title('Word Correction using Levenshtein Distance')
    word = st.text_input('Word:')

    if st.button('Compute'):
        leven_distances = {vocab: levenshtein_distance(
            word, vocab) for vocab in vocabs}
        sorted_distances = dict(
            sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]
        st.write('Correct Word:', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Sample Vocabulary:')
        col1.write(vocabs[:100])

        col2.write('Distances:')
        col2.write({k: sorted_distances[k]
                   for k in list(sorted_distances)[:10]})

if __name__ == '__main__':
    main()
