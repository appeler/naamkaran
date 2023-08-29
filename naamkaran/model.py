import torch
import torch.nn as nn


class NameGenerator(nn.Module):
    """
    A class representing the name generator model.
    """

    def __init__(self, input_size, gender_size, hidden_size, output_size, n_layers=1):
        super(NameGenerator, self).__init__()
        self.hidden_size = hidden_size
        self.n_layers = n_layers

        self.embedding = nn.Embedding(input_size, hidden_size)
        self.gender_embedding = nn.Embedding(gender_size, hidden_size)

        # LSTM now receives 2 * hidden_size because of concatenated embeddings
        self.lstm = nn.LSTM(2 * hidden_size, hidden_size, n_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, input_seq, gender, hidden):
        """
        Forward pass of the model.
        """
        name_embedded = self.embedding(input_seq)

        # Embed the gender and expand its dimensions to match the name_embedded tensor
        gender_embedded = self.gender_embedding(gender)
        gender_embedded = gender_embedded.unsqueeze(1).expand(-1, input_seq.size(1), -1)

        combined = torch.cat((name_embedded, gender_embedded), 2)

        output, hidden = self.lstm(combined, hidden)
        output = self.fc(output)
        return output, hidden

    def init_hidden(self, batch_size, device):
        """
        Initialize the hidden state of the LSTM.
        """
        return (torch.zeros(self.n_layers, batch_size, self.hidden_size, device=device),
                torch.zeros(self.n_layers, batch_size, self.hidden_size, device=device))
