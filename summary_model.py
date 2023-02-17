import os
from transformers import pipeline

class SummaryModel():
    def __init__(self, SUMARIZE_MAX_LEN, SUMARIZE_MIN_LEN, SUMARIZE_SAMPLE, TEST_TEXT_PATH, MODEL_MODE, MODEL_ARTC):
        self.SUMARIZE_MAX_LEN = SUMARIZE_MAX_LEN # 130
        self.SUMARIZE_MIN_LEN = SUMARIZE_MIN_LEN # 30
        self.SUMARIZE_SAMPLE  = SUMARIZE_SAMPLE  # False

        self.TEST_TEXT_PATH = TEST_TEXT_PATH     # test_text.txt
        self.MODEL_MODE     = MODEL_MODE         # "summarization"
        self.MODEL_ARTC     = MODEL_ARTC         # "facebook/bart-large-cnn"

    def Model(self):
        summarizer = pipeline(self.MODEL_MODE, self.MODEL_ARTC)

        with open(self.TEST_TEXT_PATH, "r") as f:
            lines = f.read().split("\n")

        # Summarize part
        print(
            summarizer(
                lines,
                max_length=self.SUMARIZE_MAX_LEN,
                min_length=self.SUMARIZE_MIN_LEN,
                do_sample=self.SUMARIZE_SAMPLE,
            ))
