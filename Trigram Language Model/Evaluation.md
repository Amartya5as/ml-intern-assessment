# Evaluation & Design Summary

This project implements a probabilistic trigram (N=3) language model from scratch.

## Modeling Decisions
• N = 3 was chosen to capture more context than bigrams while avoiding extreme sparsity.
• Two start tokens `<s> <s>` were used to model sentence beginnings and `</s>` for ending.
• Unknown words are replaced by a special `<UNK>` token based on frequency threshold = 1.
• Text is cleaned using regex and sentence-based tokenization.

## Data Representation
A nested dictionary is used to store trigram counts:
    counts[(w1, w2)][w3] = count
A second dictionary stores context totals:
    context_counts[(w1, w2)] = sum of all w3 counts

This allows fast probability computation during sampling.

## Generation Logic
Text generation is stochastic:
1. Start with context `<s>, <s>`
2. Convert counts to probabilities using Laplace smoothing
3. Sample a word probabilistically
4. Shift context and continue until 100 words or `</s>` is reached

This ensures varied output and avoids always picking the most likely next word.

## Strengths
• Works on any corpus
• Handles sentence boundaries and unknown words
• Generates diverse text rather than deterministic output

## Limitations
• Small corpora result in repetitive or low-coherence sentences
• Laplace smoothing is simple but not ideal for large vocabularies
• No backoff or interpolation for unseen contexts

## Conclusion
The implementation meets the assignment goals: a correct trigram model, unknown-word handling, padding, and probabilistic text generation with clean and readable Python code.
