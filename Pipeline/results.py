from Topic import bert_topic
from transformers import XLMRobertaForSequenceClassification, XLMRobertaTokenizerFast

# #load model and tokenizer
# model_path = "../notebook//Models/xlm-finetuned-sentiment-save"

# Load tokenizer and model
# tokenizer = XLMRobertaTokenizerFast.from_pretrained(model_path)
# model = XLMRobertaForSequenceClassification.from_pretrained(model_path)
def get_result(url):
    result=bert_topic(url)
    return result

