from flask import Flask, request, render_template
import pickle
from sklearn.pipeline import make_pipeline
from lime.lime_text import LimeTextExplainer
import os
import spacy
nlp = spacy.load('en_core_web_sm')
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
import re
import string

app = Flask(__name__, template_folder='template')

infile = open('rf_model.pkl', 'rb')
model = pickle.load(infile)
infile.close()

infile = open('tf.pkl', 'rb')
vectorizer = pickle.load(infile)
infile.close()

c = make_pipeline(vectorizer, model)

class_names = {'Pro-Vaccine': 'Pro-Vaccine', 'Anti-Vaccine':'Vaccine Misinformation'}
LIME_explainer = LimeTextExplainer(class_names=class_names)


@app.route('/')
def my_index():
    # open('static/interpret.html', 'w').close()
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict_tweet():
    
    def clean_text(text):
        '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
        and remove words containing numbers.'''
        stop_words = stopwords.words('english') + ['u', 'ur', '4', '2', 'im', 'dont', 'doin', 'ure']
        text = text.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)
        text = ''.join([c for c in text if c not in string.punctuation])
        tokens = re.split('\W+', text)
        text = ' '.join([word for word in tokens if word not in stop_words])
        text = nlp(text)
        text = ' '.join([word.lemma_ for word in text])
        return text
    
    exp = None
    input_text = request.form['input_text']
    clean_output = clean_text(input_text)
    text = list([clean_output])
    LIME_exp = LIME_explainer.explain_instance(text[0], c.predict_proba)
    exp = LIME_exp.as_html()

    pred = round(100 * c.predict_proba(text)[0][1], 2)

    if pred >= 50:
        return render_template('index.html', exp=exp, prediction=f'Vaccine-Misinformation; confidence ({pred}%)')
    else:
        return render_template('index.html', exp=exp, prediction=f'Pro-Vaccine; confidence ({100-pred}%)')


if __name__ == '__main__':
    port = 8080

    if port:
        app.run(host='0.0.0.0', port=port) #int(port)
    else:
        app.run()
