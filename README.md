# Cybersecurity BERT Language Model

This project fine-tunes the BERT base uncased model on cybersecurity and computer networking text using masked language modeling.

## Project Description

The model predicts a missing word in an English sentence containing the token [MASK]. For example:

`text
firewall monitors incoming and outgoing network [MASK].

## Pretrained Model Weights

The 400MB trained model weights are hosted under [GitHub Releases](https://github.com/adn654/cybersecurity-bert-model/releases/tag/v1.0.0).

### Download and Extract Instructions
To download and extract the model weights for inference or evaluation, run:

`bash
wget [https://github.com/adn654/cybersecurity-bert-model/releases/download/v1.0.0/bert_cybersecurity_model.zip](https://github.com/adn654/cybersecurity-bert-model/releases/download/v1.0.0/bert_cybersecurity_model.zip)
unzip bert_cybersecurity_model.zip
