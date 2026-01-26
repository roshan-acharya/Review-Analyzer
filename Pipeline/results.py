from Topic import bert_topic
from transformers import XLMRobertaForSequenceClassification, XLMRobertaTokenizerFast

# #load model and tokenizer
# model_path = "../notebook//Models/xlm-finetuned-sentiment-save"

# # Load tokenizer and model
# tokenizer = XLMRobertaTokenizerFast.from_pretrained(model_path)
# model = XLMRobertaForSequenceClassification.from_pretrained(model_path)


if __name__ == "__main__":
    result=bert_topic("https://www.daraz.com.np/products/aluminium-alloy-metal-adjustable-laptop-stand-for-10-to-17-inches-mackbooklaptopstab-i105711486-s2280473603.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Astand%253Bnid%253A105711486%253Bsrc%253ALazadaMainSrp%253Brn%253Ac4deabf3a8687c12564718997054cd87%253Bregion%253Anp%253Bsku%253A105711486_NP%253Bprice%253A540%253Bclient%253Adesktop%253Bsupplier_id%253A900152409121%253Bbiz_source%253Ah5_external%253Bslot%253A0%253Butlog_bucket_id%253A470687%253Basc_category_id%253A99%253Bitem_id%253A105711486%253Bsku_id%253A2280473603%253Bshop_id%253A47403%253BtemplateInfo%253A-1_A3_C%25231120_L%2523&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Bagmati%20Province&price=5.4E%202&priceCompare=skuId%3A2280473603%3Bsource%3Alazada-search-voucher%3Bsn%3Ac4deabf3a8687c12564718997054cd87%3BoriginPrice%3A54000%3BdisplayPrice%3A54000%3BsinglePromotionId%3A-1%3BsingleToolCode%3AmockedSalePrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1767186062829&ratingscore=4.456942003514938&request_id=c4deabf3a8687c12564718997054cd87&review=1138&sale=5013&search=1&source=search&spm=a2a0e.searchlist.list.0&stock=1")
    print(result)
