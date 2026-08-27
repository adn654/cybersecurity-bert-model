import gradio as gr
import torch
from transformers import pipeline

MODEL_ID = "adnan-865/bert-base-cybersecurity-mlm"
DEVICE = 0 if torch.cuda.is_available() else -1

fill_mask = pipeline(
    task="fill-mask",
    model=MODEL_ID,
    tokenizer=MODEL_ID,
    device=DEVICE
)


def predict_masked_text(text):
    if not text or text.count("[MASK]") != 1:
        return {
            "Error: enter one English sentence containing [MASK]": 1.0
        }

    results = fill_mask(text, top_k=5)

    return {
        result["token_str"].strip(): float(result["score"])
        for result in results
    }


demo = gr.Interface(
    fn=predict_masked_text,
    inputs=gr.Textbox(
        lines=3,
        label="Cybersecurity sentence",
        placeholder="Example: firewall protects the [MASK] from unauthorized access"
    ),
    outputs=gr.Label(
        num_top_classes=5,
        label="Top predicted words"
    ),
    title="Cybersecurity BERT Language Model",
    description=(
        "A BERT masked-language model fine-tuned on cybersecurity and networking text. "
        "Enter an English sentence containing exactly one [MASK]."
    ),
    examples=[
        ["a computer [MASK] connects multiple devices together."],
        ["firewall monitors incoming and outgoing network [MASK]."],
        ["ip address is used to identify devices on a [MASK]."],
        ["encryption protects sensitive [MASK] from attackers."]
    ]
)

if name == "main":
    demo.launch(share= True)
