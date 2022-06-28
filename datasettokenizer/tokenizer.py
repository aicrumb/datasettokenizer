_block_size = 128

def group_texts(examples):
    global _block_size
    concatenated_examples = {k: sum(examples[k], []) for k in examples.keys()}
    total_length = len(concatenated_examples[list(examples.keys())[0]])
    total_length = (total_length // _block_size) * _block_size
    result = {
        k: [t[i : i + _block_size] for i in range(0, total_length, _block_size)]
        for k, t in concatenated_examples.items()
    }
    result["labels"] = result["input_ids"].copy()
    return result

def tokenize_dataset(lm_datasets, tokenizer, block_size):
    # sketchy ass code
    global _block_size
    _block_size = block_size
    
    tokenize_function = lambda examples: tokenizer(examples["text"])
    tokenized_datasets = lm_datasets.map(tokenize_function, batched=True, num_proc=4, remove_columns=["text"])
    lm_datasets = tokenized_datasets.map(
        group_texts,
        batched=True,
        batch_size=1000,
        num_proc=4,
    )
    return lm_datasets
