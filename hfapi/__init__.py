import requests

class Client:
    def __init__(self):
        pass

    def _call(self, query, model):
        model_location = "https://api-inference.huggingface.co/models/" + model
        return requests.post(model_location, json=query).json()

    def question_answering(self, question, context,
           model="distilbert-base-uncased-distilled-squad"):
        query = dict(question=question, context=context)
        return self._call(query, model)

    def summarization(self, input, model="sshleifer/distilbart-xsum-12-6"):
        return self._call(input, model)

    def text_generation(self, input, model="distilgpt2"):
        return self._call(input, model)

    def fill_mask(self, input, model="distilbert-base-uncased"):
        return self._call(input, model)

    def text_classification(self, input,
                 model="distilbert-base-uncased-finetuned-sst-2-english"):
        return self._call(input, model)

    def token_classification(self, input, model="dslim/bert-base-NER"):
        return self._call(input, model)
