import requests
from bs4 import BeautifulSoup
from keybert import KeyBERT
from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizerb = AutoTokenizer.from_pretrained("mrm8488/bert-mini-finetuned-age_news-classification")

modelb = AutoModelForSequenceClassification.from_pretrained("mrm8488/bert-mini-finetuned-age_news-classification")

def label(urll, token= tokenizerb, mod = modelb):
    response = requests.get(urll)
    soup = BeautifulSoup(response.text, 'html.parser')
    text_content = soup.get_text()

    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(text_content, keyphrase_ngram_range=(3, 3), use_mmr=True, diversity=0.5, top_n=10)
    
    s = ""
    for i in keywords:
      s = s + " " + i[0]
    from transformers import pipeline
    classifier = pipeline('text-classification', model=mod, tokenizer=token)
    keys = []
    for i in keywords:
      keys.append(i[0])
    keys_str = ""
    for i in keys:
      keys_str = keys_str + "," + i
    class_and_key = [classifier(s)[0]['label'], keys_str[1:]]
    return(class_and_key)

