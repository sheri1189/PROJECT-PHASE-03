from transformers import BertForSequenceClassification
import torch

def load_model():
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=6)
    return model

def predict_toxicity(model, tokenizer, text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
    outputs = model(**inputs)
    logits = outputs.logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    predicted_class = torch.argmax(probabilities, dim=-1).item()
    return predicted_class
