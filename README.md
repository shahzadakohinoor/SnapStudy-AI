# SnapStudy-AI

An intelligent offline study assistant designed to parse study documents, answer questions, generate quizzes, and organize study notes.

---

## Features

- **Document Processing**: Ingest and extract text from PDFs, text files, and images via OCR.
- **Context-Aware Study Assistant**: Retrieve relevant answers based on loaded notes and materials.
- **Automated Quiz Generation**: Create fill-in-the-blank practice questions directly from document text.
- **Note Taking & Storage**: Persistent local database using SQLite for notes, documents, and quizzes.
- **Hardware Diagnostics**: Profiles system compute resources (CPU, RAM, and GPU/NPU detection).

---

## Project Structure

```text
SnapStudy-AI/
├── app/
│   ├── ai/            # Embedding and question-answering logic
│   ├── database/      # SQLite database manager
│   ├── documents/     # PDF, image, and text extraction parsers
│   ├── ui/            # User interface and dashboard logic
│   ├── utils/         # Diagnostics and telemetry
│   └── main.py        # Application orchestrator
├── assets/            # Screenshots and project media
├── benchmarks/        # Hardware benchmark scripts
├── models/            # Local model weights and references
├── tests/             # Unit and integration test suite
├── requirements.txt   # Python dependency list
├── run.py             # Root launch script
└── README.md