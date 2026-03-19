import os


class ModelConfig:
    def __init__(self):
        # ----------------------------
        # Speech / Transcription
        # ----------------------------
        self.WHISPER_MODEL_NAME = os.getenv("WHISPER_MODEL_NAME", "base")

        # ----------------------------
        # Speaker Diarization
        # ----------------------------
        self.DIARIZATION_MODEL_NAME = os.getenv(
            "DIARIZATION_MODEL_NAME",
            "pyannote/speaker-diarization"
        )

        # ----------------------------
        # Translation
        # ----------------------------
        self.TRANSLATION_MODEL_NAME = os.getenv(
            "TRANSLATION_MODEL_NAME",
            "facebook/nllb-200-distilled-600M"
        )
        self.TRANSLATION_SOURCE_LANG = os.getenv("TRANSLATION_SOURCE_LANG", "auto")
        self.TRANSLATION_TARGET_LANG = os.getenv("TRANSLATION_TARGET_LANG", "eng_Latn")

        # ----------------------------
        # Summarization
        # ----------------------------
        self.SUMMARIZATION_MODEL_NAME = os.getenv(
            "SUMMARIZATION_MODEL_NAME",
            "facebook/bart-large-cnn"
        )

        # ----------------------------
        # Embeddings / Semantic Search / Comparison
        # ----------------------------
        self.EMBEDDING_MODEL_NAME = os.getenv(
            "EMBEDDING_MODEL_NAME",
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        # ----------------------------
        # General runtime settings
        # ----------------------------
        self.DEVICE = os.getenv("MODEL_DEVICE", "cpu")
        self.USE_FP16 = os.getenv("USE_FP16", "False").lower() == "true"


model_config = ModelConfig()