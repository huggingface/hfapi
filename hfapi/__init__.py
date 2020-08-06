import requests
import logging
import time


logger = logging.getLogger(__name__)


HTTP_SERVICE_UNAVAILABLE = 503

MAX_RETRIES = 60


class Client:
    def __init__(self, api_token=None):
        self.api_token = api_token

    def _call(self, query, model):
        model_location = "https://api-inference.huggingface.co/models/" + model
        headers = {}
        if self.api_token is not None:
            headers = {"Authorization": "Bearer " + self.api_token}
        retries = 0

        while retries < MAX_RETRIES:
            retries += 1
            r = requests.post(model_location, json=query, headers=headers)
            if r.status_code == HTTP_SERVICE_UNAVAILABLE:
                # We'll retry
                # If running under asyncio, be sure to use
                # `await asyncio.sleep(1)` instead.
                logger.info("Model is currently loading")
                time.sleep(1)
            else:
                break
        return r.json()

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
