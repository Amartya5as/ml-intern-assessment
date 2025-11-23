from model import TrigramLanguageModel
from utils import read_corpus

INPUT_FILE = "example_corpus.txt"
OUTPUT_FILE = "sample_output.txt"

def main():
    sentences = read_corpus(INPUT_FILE)
    model = TrigramLanguageModel()
    model.fit(sentences)

    generated = model.generate(max_words=100)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(generated)

    print("Training complete!")
    print("Generated text saved to sample_output.txt")

if __name__ == "__main__":
    main()
