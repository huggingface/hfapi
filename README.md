<p align="center>
<img src="https://raw.githubusercontent.com/huggingface/nlp/master/docs/source/imgs/nlp_logo_name.png" width="100" />
</p>

# HF API

Beta API client for Hugging Face Inference API, e.g. inference widget on https://huggingface.co/distilbert-base-uncased .


See full set of models here: https://huggingface.co/models


```python
import hfapi
client = hfapi.Client()
```


```python
client.question_answering("Where does she live?", "She lives in Berlin.")
```

> {'score': 0.9375529668751711, 'start': 13, 'end': 19, 'answer': 'Berlin.'}
```python
client.text_generation("My name is Julien and I like to ")
```

```
> [{'generated_text': "My name is Julien and I like to ~~~\n\nIf I'm not so successful I go to my school and I am no longer able to attend school (like, I'm not a full-time student in a country, and"}]
```

```python
client.summarization("The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.")
```

> [{'summary_text': ' The Eiffel Tower in Paris has officially opened its doors to the public.'}]

```python
client.fill_mask("Paris is the [MASK] of France."))
```

> [{'sequence': '[CLS] paris is the capital of france. [SEP]', 'score': 0.9815465807914734, 'token': 3007, 'token_str': 'capital'}, {'sequence': '[CLS] paris is the birthplace of france. [SEP]', 'score': 0.00334245921112597, 'token': 14508, 'token_str': 'birthplace'}, {'sequence': '[CLS] paris is the northernmost of france. [SEP]', 'score': 0.001044721808284521, 'token': 22037, 'token_str': 'northernmost'}, {'sequence': '[CLS] paris is the centre of france. [SEP]', 'score': 0.001004318823106587, 'token': 2803, 'token_str': 'centre'}, {'sequence': '[CLS] paris is the southernmost of france. [SEP]', 'score': 0.0007803254993632436, 'token': 21787, 'token_str': 'southernmost'}]

```python
client.text_classification("I hated the movie!")
```

> [[{'label': 'NEGATIVE', 'score': 0.9996837973594666}, {'label': 'POSITIVE', 'score': 0.0003162133798468858}]]

```python
client.token_classification("My name is Sarah and I live in London")
```

> [{'entity_group': 'B-PER', 'score': 0.9985478520393372, 'word': 'Sarah'}, {'entity_group': 'B-LOC', 'score': 0.999621570110321, 'word': 'London'}]
