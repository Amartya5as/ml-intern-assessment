import random
from collections import defaultdict, Counter
import math

class TrigramLanguageModel:
    def __init__(self):
        self.UNK = "<UNK>"
        self.START = "<s>"
        self.END = "</s>"
        self.counts = defaultdict(Counter)
        self.context_counts = Counter()
        self.vocab = set()

    def _pad(self, tokens):
        return [self.START, self.START] + tokens + [self.END]

    def build_vocab(self, sentences, unk_threshold=1):
        word_freq = Counter()
        for sent in sentences:
            for w in sent:
                word_freq[w] += 1
        self.vocab = {w for w, c in word_freq.items() if c > unk_threshold}
        self.vocab.add(self.UNK)

    def _replace_unk(self, tokens):
        return [w if w in self.vocab else self.UNK for w in tokens]

    def fit(self, sentences):
        self.build_vocab(sentences)
        for sent in sentences:
            sent = self._replace_unk(sent)
            padded = self._pad(sent)
            for i in range(2, len(padded)):
                context = (padded[i-2], padded[i-1])
                target = padded[i]
                self.counts[context][target] += 1
                self.context_counts[context] += 1

    def _prob(self, context):
        vocab_list = list(self.vocab)
        total = self.context_counts[context] + len(self.vocab)
        return vocab_list, [(self.counts[context][w] + 1) / total for w in vocab_list]

    def generate(self, max_words=100):
        context = (self.START, self.START)
        generated = []
        for _ in range(max_words):
            vocab_list, probs = self._prob(context)
            next_word = random.choices(vocab_list, probs)[0]
            if next_word == self.END:
                break
            generated.append(next_word)
            context = (context[1], next_word)
        return " ".join(generated)
