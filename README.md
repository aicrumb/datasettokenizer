# tokenizer
literally one small function to pre-tokenize non-streamed datasets for easier small scale LM training w/ huggingface

```python
!pip install git+https://github.com/aicrumb/tokenizer
from datasettokenizer import *
from transformers import GPT2TokenizerFast

dataset = load_dataset("tiny_shakespeare")
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
dataset = tokenize_dataset(dataset, tokenizer, block_size=256)
```

this is so i can feed it right into the trainer or something like that, idk if it's actually needed for this or not

it probably is not needed

but i have >5 scripts that use the entire lines of code and it's easier to just make it pip installable for one single line

so assuming you've loaded a gpt model with huggingface, and imported args and trainer

```python

training_args = TrainingArguments(
    f"user/my-model",
    push_to_hub=True,
    max_epochs=1,
    save_steps=1000
)

trainer = Trainer(
    model=gpt,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["validation"],
)
trainer.train()
```
