import requests

class Client:
    def __init__(self):
        pass

    def _call(self, query, model):
        model_location = "https://api-inference.huggingface.co/models/" + model
        return requests.post(model_location, json=query).json()

    def qa(self, question, context,
           model="distilbert-base-uncased-distilled-squad"):
        query = dict(question=question, context=context)
        return self._call(query, model)

    def summarize(self, input, model="sshleifer/distilbart-xsum-12-6"):
        return self._call(input, model)

    def text_generate(self, input, model="distilgpt2"):
        return self._call(input, model)

    def mask_fill(self, input, model="distilbert-base-uncased"):
        return self._call(input, model)

    def classify(self, input,
                 model="distilbert-base-uncased-finetuned-sst-2-english"):
        return self._call(input, model)
