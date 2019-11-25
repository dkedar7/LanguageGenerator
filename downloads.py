# Downloads model(s) during docker build
# from pytorch_transformers.file_utils import cached_path

# urls = [
#     'https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-vocab.json',
#     'https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-merges.txt',
#     'https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-pytorch_model.bin',
#     'https://s3.amazonaws.com/models.huggingface.co/bert/gpt2-config.json'
# ]

# for url in urls:
#     cached_path(url)

import joblib
from pytorch_transformers import GPT2Tokenizer, GPT2LMHeadModel
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2').eval()

joblib.dump(tokenizer, 'tokenizer.pkl')
joblib.dump(model, 'model.pkl')