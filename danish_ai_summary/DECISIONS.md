# Decision Log

### D-007 — Never Filter Core Domain Policy Keywords into Stopwords (2026-10-31)
- Context: During multi-algorithm benchmarking, an attempt to treat frequent domain keywords (`mbg`, `makan`, `bergizi`, `gratis`, `program`, `anak`, `sekolah`) as domain stopwords stripped away the central research topic and degraded model coherence.
- Decision: Retain all substantive policy terms in the vocabulary. Stopwords are strictly limited to structural/grammatical connectors. The dataset `dataset_komentar_clean.csv` is already 100% preprocessed and must not undergo destructive re-cleaning.
- Rejected: Treating frequent domain nouns/verbs as stopwords (destroys policy topic discovery).
- Revisit if: Never. Substantive domain terms are mandatory for the research findings.

### D-006 — Store confidential assignments & drafts in `informasi/catatan_pribadi/` (2026-10-15)
- Context: University assignments, personal Word reports, and presentation slide decks contain student metadata and assignment prompts.
- Decision: Place them in `informasi/catatan_pribadi/`, gitignore them completely, and protect them under "DO NOT touch".
- Rejected: Committing them to the public git repository (violates privacy and academic submission integrity).
- Revisit if: Lecturer or department mandates open-source release of final graded files.

### D-005 — Dual-Tier Deliverable Strategy (2026-10-15)
- Context: The course requires both immediate weekly lab deliverables and a high-impact final term output.
- Decision: Split deliverables into Target 1 (Lab Report Bab I-V + Presentation slide deck, due 22 Oct 2026) and Target 2 (Pre-UAS: SINTA 3 baseline journal + SINTA 2 cross-modal framing journal).
- Rejected: Single report attempting to serve both lab grading and journal publication simultaneously (differing structures and rigorousness).
- Revisit if: Semester UAS requirements change.

### D-004 — Optimal Topic Coherence K=2 for LDA Model (2026-10-15)
- Context: Latent Dirichlet Allocation requires choosing number of topics $K$.
- Decision: Select $K=2$ based on empirical maximum coherence score $C_v = 0.3911$ evaluated across $K \in [2, 10]$.
- Rejected: Choosing $K=3$ or $K=5$ arbitrarily without empirical coherence backing.
- Revisit if: Dataset volume is expanded significantly beyond 5,207 comments.

### D-003 — Cross-Modal Media Packaging & Chi-Square Test for SINTA 2 (2026-10-15)
- Context: Standard LDA topic modeling is typical of SINTA 3/4 papers and lacks theoretical framing depth required for SINTA 2 accreditation.
- Decision: Categorize videos into 3 media framing packages (*Meme/Satir*, *Serious Opinion/Edukasi*, *News Formal*) and perform cross-tabulation with Chi-Square test ($\chi^2 = 212.4579, df=2, p < 0.0001$).
- Rejected: Relying solely on descriptive frequency distributions.
- Revisit if: Reframing dataset into additional media genres (e.g. Talkshow).

### D-002 — Pivot from Supervised Classification to Unsupervised LDA (2026-10-15)
- Context: Initial exploration utilized Indo-RoBERTa for supervised sentiment labeling (5,207 comments labeled). Lecturer subsequently established strict guideline prohibiting manual/pseudo labeling for the project.
- Decision: Pivot core pipeline to 100% Unsupervised NLP (Topic Modeling using LDA). Preserve Indo-RoBERTa labeled dataset in `data/processed/dataset_komentar_labeled.csv` as an archived validation baseline.
- Rejected: Discarding the labeled dataset completely or attempting pseudo-label clustering.
- Revisit if: Lecturer permits hybrid/semi-supervised validation in Target 2 journal article.

### D-001 — Selection of Topic 1: MBG YouTube Comments (2026-10-08)
- Context: 5 potential research topics were proposed for the Data Mining TI-3A course.
- Decision: Select Topic 1 ("Unsupervised NLP Topic Modeling on MBG YouTube Comments using LDA") as officially approved by course lecturer.
- Rejected: Topics 2 through 5 (e.g., student performance prediction, e-commerce reviews).
- Revisit if: Not applicable (formal topic approval locked).

