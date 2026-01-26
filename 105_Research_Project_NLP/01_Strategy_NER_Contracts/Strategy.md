# Research Project: NLP (Named Entity Recognition)

## 1. Problem Understanding
*   **Context**: Automating Legal Review. We need to find "Effective Date", "Party Name", and "Jurisdiction" in thousands of PDFs.
*   **Why not Regex?**: "This agreement starts on Jan 1st" vs "Dated: Jan 1st". Regex is brittle. BERT understands context.
*   **The Data**: [CONLL-2003](https://huggingface.co/datasets/conll2003) is standard, but for RESEARCH we simulate a Legal Dataset (Contract Understanding Atticus Dataset - CUAD).

## 2. Research Strategy
*   **Token Classification**: Unlike Text Classification (One label per sentence), NER assigns a label to EVERY token (word piece).
    *   `Alice` -> `B-PER` (Beginning Person)
    *   `Corp` -> `I-PER` (Inside Person)
    *   `signed` -> `O` (Outside)
*   **Model**: `DistilBERT` (Lighter, faster than BERT).
*   **Metric**: Seqeval F1-Score. We utilize the "IOB" format (Inside, Outside, Beginning).

## 3. Step-by-Step Plan
1.  **Tokenization**: Use `AutoTokenizer`. Crucial: We must align labels! If "Alice" splits into ["Al", "##ice"], both sub-tokens must inherit the `B-PER` label (or -100 to ignore).
2.  **Dataset**: Class `LegalDataset(torch.utils.data.Dataset)`. Returns `input_ids`, `attention_mask`, `labels`.
3.  **Training**: `Trainer` API from HuggingFace.
    *   `data_collator`: dynamcially pads the batch to the longest sequence (efficiency hack).
4.  **Inference**: Pipeline `ner = pipeline("ner", model=model, aggregation_strategy="simple")`.
