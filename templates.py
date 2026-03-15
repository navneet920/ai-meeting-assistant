import os
import logging
from pathlib import Path

logging.basicConfig(format='[%(pastime)s]:%(message)s:')

list_of_files=[
    #Github workflow
    ".github/workflows/.gitkeep",

    #Backend
    "backend/app/__init__.py",
    "backend/app/main.py",
    "backend/app/config.py",
    "backend/app/dependencies.py",

    #api
    "backend/app/api/routes/__init__.py",
    "backend/app/api/routes/meeting_routes.py",
    "backend/app/api/routes/transcript_routes.py",
    "backend/app/api/routes/summary_routes.py",
    "backend/app/api/routes/comparison_routes.py",

    #schemas
    "backend/app/schemas/__init__.py",
    "backend/app/schemas/meeting_schema.py",
    "backend/app/schemas/summary_schema.py",
    "backend/app/schemas/comparison_schema.py",

    #models
    "backend/app/models/__init__.py",
    "backend/app/models/meeting_model.py",
    "backend/app/models/transcript_model.py",
    "backend/app/models/summary_model.py",
    "backend/app/models/comparison_model.py",

    #services
    "backend/app/services/__init__.py",
    "backend/app/services/meeting_service.py",
    "backend/app/services/transcript_service.py",
    "backend/app/services/summary_service.py",
    "backend/app/services/comparison_service.py",

    #repositories
    "backend/app/repositories/__init__.py",
    "backend/app/repositories/meeting_repository.py",
    "backend/app/repositories/summary_repository.py",
    "backend/app/repositories/comparison_repository.py",

    #db
    "backend/app/db/__init__.py",
    "backend/app/db/base.py",
    "backend/app/db/session.py",
    "backend/app/db/init_db.py",

    #utils
    "backend/app/utils/__init__.py",
    "backend/app/utils/file_handler.py",
    "backend/app/utils/logger.py",
    "backend/app/utils/helpers.py",
    "backend/app/utils/response_builder.py",

    #core
    "backend/app/core/__init__.py",
    "backend/app/core/constants.py",
    "backend/app/core/expections.py",
    "backend/app/core/security.py",

    #uploads
    "backend/uploads/raw_audio",
    "backend/uploads/processed_audio",
    "backend/uploads/temp",

    #tests
    "backend/tests/__init__.py",
    "backend/tests/test_meeting_api.py",
    "backend/tests/test_summary_api.py",
    "backend/tests/test_comparison_api.py",

    #requirements
    "backend/requirements.txt",


    # AI/pipelines
    "ai/pipelines/__init__.py",
    "ai/pipelines/meeting_pipeline.py",
    "ai/pipelines/transcription_pipeline.py",
    "ai/pipelines/diarization_pipeline.py",
    "ai/pipelines/translation_pipeline.py",
    "ai/pipelines/summarization_pipeline.py",
    "ai/pipelines/extraction_pipeline.py",
    "ai/pipelines/comparison_pipeline.py",

    #models
    "ai/models/__init__.py",
    "ai/models/whisper_model.py",
    "ai/models/diarization_model.py",
    "ai/models/translation_model.py",
    "ai/models/summarizer_model.py",
    "ai/models/embedding_model.py",

    #services
    "ai/services/__init__.py",
    "ai/services/transcription_service.py",
    "ai/services/diarization_service.py",
    "ai/services/translation_service.py",
    "ai/services/summarization_service.py",
    "ai/services/extraction_service.py",
    "ai/services/comparison_service.py",

    #processors
    "ai/processors/__init__.py",
    "ai/processors/audio_preprocessor.py",
    "ai/processors/transcript_cleaner.py",
    "ai/processors/speaker_aligner.py",
    "ai/processors/language_detector.py",

    #prompts
    "ai/prompts/__init__.py",
    "ai/prompts/summary_prompt.txt",
    "ai/prompts/action_items_prompt.txt",
    "ai/prompts/decisions_prompt.txt",
    "ai/prompts/comparison_prompt.txt",

    #vector_store
    "ai/vector_store/__init__.py",
    "ai/vector_store/faiss_index.py",
    "ai/vector_store/retriever.py",

    #artifacts
    "ai/artifacts/transcripts/.gitkeep",
    "ai/artifacts/summaries/.gitkeep",
    "ai/artifacts/embeddings/.gitkeep",
    "ai/artifacts/comparisons/.gitkeep",

    #config
    "ai/config/__init__.py",
    "ai/config/model_config.py",
    "ai/config/pipeline_config.py",

    #utils
    "ai/utils/__init__.py",
    "ai/utils/chunking.py",
    "ai/utils/time_utils.py",
    "ai/utils/text_utils.py",
    "ai/utils/json_utils.py",

    #tests
    "ai/tests/__init__.py",
    "ai/tests/test_transcription.py",
    "ai/tests/test_translation.py",
    "ai/tests/test_summary.py",
    "ai/tests/test_comparison.py",

    ".gitignore",
    "README.md",
]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory : {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file :{filepath}")

    else:
        logging.info(f"{filename} is already exists")