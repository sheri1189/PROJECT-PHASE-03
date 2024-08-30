from model.model import load_model, predict_toxicity
from model.tokenizer import load_tokenizer
model = load_model()
tokenizer = load_tokenizer()
toxic_words = {
    'toxic': ['nasty', 'harsh'],
    'severe toxic': ['extremely harsh'],
    'obscene': ['vulgar', 'rude'],
    'threat': ['warning', 'intimidation'],
    'insult': ['offense', 'disrespect'],
    'identity hate': ['discrimination', 'prejudice']
}
toxicity_labels = {
    0: 'toxic',
    1: 'severe toxic',
    2: 'obscene',
    3: 'threat',
    4: 'insult',
    5: 'identity hate'
}

def classify_toxicity(text):
    """
    Classify the toxicity of the given text using the pre-trained BERT model.
    """
    label_id = predict_toxicity(model, tokenizer, text)
    return toxicity_labels.get(label_id, 'unknown')

def replace_toxic_words(text):
    """
    Replace toxic words in the given text with their synonyms.
    """
    toxic_word_detected = None
    for category, synonyms in toxic_words.items():
        for toxic_word in synonyms:
            if toxic_word in text:
                text = text.replace(toxic_word, synonyms[0])
                toxic_word_detected = category
    return text, toxic_word_detected
