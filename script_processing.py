import nltk
nltk.download('punkt')  # Download punkt for sentence tokenization
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize

def process_script(script_input):
    sentences = sent_tokenize(script_input)
    cleaned_sentences = [sentence.strip() for sentence in sentences]
    return cleaned_sentences

# script = "Artificial intelligence is revolutionizing industries. It has applications in healthcare, finance, and education."
# processed_script = process_script(script)
# print(processed_script)

print("Script processing done")
__all__ = ['process_script']