from transformers import pipeline

import os

SUMARIZE_MAX_LEN = 130
SUMARIZE_MIN_LEN = 30
SUMARIZE_SAMPLE = False

TEST_TEXT_PATH = "test_text.txt"
MODEL_MODE = "summarization"
MODEL_ARTC = "facebook/bart-large-cnn"

summarizer = pipeline(MODEL_MODE, MODEL_ARTC)

with open(TEST_TEXT_PATH, "r") as f:
    lines = f.read().split("\n")

# Summarize part
print(
    summarizer(
        lines,
        max_length=SUMARIZE_MAX_LEN,
        min_length=SUMARIZE_MIN_LEN,
        do_sample=SUMARIZE_SAMPLE,
    )
)
