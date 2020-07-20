import hfapi
client = hfapi.Client()

print("""

```python
import hfapi
client = hfapi.Client()
```

""")

print("""```python
client.question_answering("Where does she live?", "She lives in Berlin.")
```
""")

print(">", client.question_answering("Where does she live?", "She lives in Berlin."))

print("""```python
client.text_generation("My name is Julien and I like to ")
```
""")
print("```")
print(">", client.text_generation("My name is Julien and I like to ", model="gpt2"))
print("```")
print()

print("""```python
client.summarization("The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.")
```
""")

print(">", client.summarization("The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."))
print()

print("""```python
client.fill_mask("Paris is the [MASK] of France."))
```
""")

print(">",client.fill_mask("Paris is the [MASK] of France."))
print()


print("""```python
client.text_classification("I hated the movie!")
```
""")

print(">", client.text_classification("I hated the movie!"))
print()


print("""```python
client.token_classification("My name is Sarah and I live in London")
```
""")

print(">", client.token_classification("My name is Sarah and I live in London"))
print()
