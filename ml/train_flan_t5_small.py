import numpy as np
from datasets import load_from_disk
from transformers import DataCollatorForSeq2Seq, Seq2SeqTrainingArguments, Seq2SeqTrainer
from ml.src.gec.modeling import get_model, get_tokenizer

TRAIN_PATH = "/home/thanhfvux/GrammarFixer/ml/data/processed/train_tok"
VAL_PATH   = "/home/thanhfvux/GrammarFixer/ml/data/processed/val_tok"
OUT_DIR    = "/home/thanhfvux/GrammarFixer/ml/outputs/gec_flan_t5_small"

tokenizer = get_tokenizer()
model = get_model()

train_tok = load_from_disk(TRAIN_PATH)
val_tok   = load_from_disk(VAL_PATH)

data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model, padding=True)

def compute_metrics(eval_pred):
    preds, labels = eval_pred
    decoded_preds = tokenizer.batch_decode(preds, skip_special_tokens=True)
    labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
    decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)
    em = np.mean([p.strip() == l.strip() for p, l in zip(decoded_preds, decoded_labels)])
    return {"exact_match": float(em)}

args = Seq2SeqTrainingArguments(
    output_dir=OUT_DIR,

    fp16=True,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=8,
    gradient_accumulation_steps=4,

    eval_strategy="steps",
    eval_steps=500,

    save_strategy="steps",
    save_steps=500,
    save_total_limit=2,          

    predict_with_generate=True,
    generation_max_length=128,

    logging_steps=50,
    report_to="none",
)

trainer = Seq2SeqTrainer(
    model=model,
    args=args,
    train_dataset=train_tok,
    eval_dataset=val_tok,
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

trainer.train()
