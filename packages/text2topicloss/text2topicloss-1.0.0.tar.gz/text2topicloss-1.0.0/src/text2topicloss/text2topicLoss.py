from sentence_transformers import SentenceTransformer
import torch
from torch import nn, Tensor
from typing import Dict, Iterable

class Text2TopicLoss(nn.Module):
    def __init__(
            self, 
            model: SentenceTransformer,
            concatenation_sent_rep: bool = True, 
            concatenation_sent_difference: bool = True, 
            concatenation_sent_mul: bool = True,
            dropout_prob: float = 0.1
    ):
        super(Text2TopicLoss, self).__init__()
        self.concatenation_sent_rep = concatenation_sent_rep
        self.concatenation_sent_difference = concatenation_sent_difference
        self.concatenation_sent_multiplication = concatenation_sent_mul
        self.model = model
        self.dropout_prob = dropout_prob
        self.sigmoid = nn.Sigmoid()
        self.loss = nn.BCEWithLogitsLoss()
        
        sentence_embedding_dimension = model.get_sentence_embedding_dimension()

        i = 0
        if self.concatenation_sent_rep: i += 2
        if self.concatenation_sent_difference: i += 1
        if self.concatenation_sent_multiplication: i += 1

        d_E = sentence_embedding_dimension * i

        self.ffn1 = nn.Sequential(
            nn.Linear(d_E, sentence_embedding_dimension, device=self.model.device),
            nn.ReLU(),
            nn.Dropout(dropout_prob)
        )
        

        self.ffn2 = nn.Linear(sentence_embedding_dimension, 1, device=self.model.device)
    
    def logits(self, u: Tensor, v: Tensor):
        embedding = []

        if self.concatenation_sent_rep:
            embedding.append(u)
            embedding.append(v)

        if self.concatenation_sent_difference:
            embedding.append(torch.abs(u - v))

        if self.concatenation_sent_multiplication:
            embedding.append(u * v)
        
        embedding = torch.cat(embedding, 1)

        embedding = self.ffn1(embedding)
        logits = self.ffn2(embedding)
        return logits.squeeze(dim=1)
    
    def predict(self, u: Tensor, v: Tensor):
        with torch.no_grad():
            logits = self.logits(u, v)
            probs = self.sigmoid(logits)
            return probs.cpu().numpy().astype('float32')[0]

    def encode_and_predict(self, topic: str, sentence: str):
        topic_embedding = self.model.encode(topic, convert_to_tensor=True).view(1, -1)
        sentence_embedding = self.model.encode(sentence, convert_to_tensor=True).view(1, -1)
        return self.predict(topic_embedding, sentence_embedding)

    def forward(self, sentence_features: Iterable[Dict[str, Tensor]], labels: Tensor):
        reps = [self.model(sentence_feature)["sentence_embedding"] for sentence_feature in sentence_features]
        u, v = reps
        logits = self.logits(u, v)
        return self.loss(logits, labels.view(-1).float())