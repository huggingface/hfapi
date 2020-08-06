from hfapi import Client

client = Client()

BATCH_SIZE = 4

LONG_LIST_OF_INPUTS = [
    "I like you. </s></s> I love you.",
    "At the other end of Pennsylvania Avenue, people began to line up for a White House tour. </s></s> People formed a line at the end of Pennsylvania Avenue.",
] * 500

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

all_results = []

for inputs in chunker(LONG_LIST_OF_INPUTS, BATCH_SIZE):
    result = client.text_classification(inputs, model="roberta-large-mnli")
    print(result)
    all_results += result


print("Done!")
