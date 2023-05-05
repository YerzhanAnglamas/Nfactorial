import random

with open("names.txt", "r", encoding="utf-8") as f:
    names = f.read().split()

bigram_counts = {}
for name in names:
    for i in range(len(name) - 1):
        bigram = name[i:i + 2]
        bigram_counts[bigram] = bigram_counts.get(bigram, 0) + 1

total_bigrams = sum(bigram_counts.values())
bigram_probabilities = {}
for bigram, count in bigram_counts.items():
    bigram_probabilities[bigram] = count / total_bigrams

first_letters = set(name[0] for name in names)


def generate_name():
    first_letter = random.choice(list(first_letters))
    name = first_letter

    for i in range(1,100):
        last_letter = name[-1]

        possible_bigrams = [bigram for bigram in bigram_probabilities.keys() if bigram.startswith(last_letter)]

        if not possible_bigrams:
            break

        next_bigram = \
        random.choices(possible_bigrams, weights=[bigram_probabilities[bigram] for bigram in possible_bigrams])[0]
        next_letter = next_bigram[1]
        name += next_letter

    return name


def print_bigram_probabilities():
    print("Биграмма\tВероятность")
    for bigram, probability in bigram_probabilities.items():
        print(f"{bigram}\t{probability:.4f}")


print(bigram_counts)
print(total_bigrams)
print(first_letters)
print(generate_name())
print_bigram_probabilities()
