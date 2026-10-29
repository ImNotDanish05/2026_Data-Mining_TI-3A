# Conventions, Gotchas & Preferences

## Project Conventions

- **STRICT: NO SUPERVISED LABELS**: The lecturer strictly forbids manual or pseudo labeling for the primary research model. All model training MUST be Unsupervised NLP (Topic Modeling LDA). The Indo-RoBERTa classification in `dataset_komentar_labeled.csv` exists solely as an archived validation/benchmarking asset.
- **Strict Political Neutrality**: All code comments, documentation, commit messages, and variable names must remain strictly neutral, analytical, and mathematical. Never express personal, political, or partisan bias.
- **Privacy-Preserving Data Mining (UU PDP & UU Dikti)**: Under Indonesian UU No. 27/2022 (UU PDP) and academic freedom statutes (UU No. 12/2012), all author usernames and identifying info (`author` column) must be permanently dropped before analysis or publication.
- **Quota Efficiency in YouTube API**: Never paginate comment replies; use `totalReplyCount` from `commentThreads` to conserve API quota.
- **CSV Formatting Safety**: The `summary` column in `dataset_video_clean.csv` must not contain unescaped commas or double-quotes to ensure safe naive CSV splitting.
- **Academic Standards**:
  - Formulas written using KaTeX formatting ($C_v$, $\chi^2$, etc.).
  - Formal three-line tables (*tabel tiga garis*) for journal manuscripts.
  - IEEE citation style with active DOIs.

## Known Gotchas

- **Virtual Environment Shebang Issue**: Executables in `.venv/bin/` (e.g. `pip`, `pytest`) have a hardcoded shebang `#!/home/imnotdanish05/data1/...` which fails if executed directly as `./.venv/bin/pip`. Always invoke tools via `.venv/bin/python3 -m <tool>` (e.g., `.venv/bin/python3 -m pip` or `.venv/bin/python3 -m pytest`).
- **Return YouTube Dislike (RYD) API**: May return null or rate-limit; the code must default `dislike_count_est` to 0 on failure.
- **YouTube Transcripts IP Blocks**: Fetching YouTube transcripts frequently triggers IP rate-limits or captcha blocks. `fetch_youtube_transcripts.py` uses automatic Proton VPN CLI rotation (`protonvpn connect --random`) with incremental resume.
- **Pytest Template Path**: `test_collector.py` expects `Youtube_Data_Collection_API/input_videos_template.csv` at a specific relative path; verify file existence before running full test suites.

## DO NOT Touch

- `.env` — Contains private credentials (`YOUTUBE_API_KEY`).
- `informasi/catatan_pribadi/` — User's private assignments, original PPTX backups, and Word reports. Strictly gitignored and never committed.
- `data/processed/dataset_komentar_labeled.csv` — Critical archived asset containing 5,207 Indo-RoBERTa sentiment labels. DO NOT delete or overwrite.
- `models/` — Local binary caches (Hugging Face transformer weights, LDA zip files). Gitignored.

## User Preferences & Standards

- **Deliverable Standards**: Aim for publication-ready outputs aligned with ARJUNA SINTA 2 & SINTA 3 national journal indexing criteria.
- **Evidence-Based Reporting**: Always provide concrete verification evidence (commands executed, exit codes, exact counts) rather than generic status statements.
- **Self-Contained Local Execution**: Heavy machine learning models (Indo-RoBERTa) are cached strictly within `./models/` rather than global system cache directories.

