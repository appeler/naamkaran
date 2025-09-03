#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Optional

try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files

import joblib
import torch

from .model import NameGenerator


class Naamkaran:
    """
    Generates names for the given start_letter, end_letter
    """

    @staticmethod
    def generate(
        start_letter: str,
        end_letter: Optional[str],
        how_many: int,
        max_length: int,
        gender: str,
        temperature: float,
        model_fn: str,
        vocab_fn: str,
    ) -> List[str]:
        """
        Generates names for the given dataframe.
        """
        MODEL = files(__name__).joinpath(model_fn)
        VOCAB = files(__name__).joinpath(vocab_fn)

        vectorizer = joblib.load(VOCAB)
        vocab = list(vectorizer.get_feature_names_out())
        n_letters = len(vocab)
        all_letters = "".join(vocab)
        oob = n_letters + 1

        # Hyperparameters
        hidden_size = 100
        n_layers = 1
        gender_size = 2

        vocab_size = n_letters + 1 + 1  # vocab + oob + 1
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        # Initialize the model
        model = NameGenerator(
            vocab_size, gender_size, hidden_size, vocab_size, n_layers
        )
        model.load_state_dict(torch.load(MODEL, map_location=device))
        model.to(device)

        # set the model to evaluation mode
        model.eval()
        generated_names = []

        gender_to_idx = {"F": 0, "M": 1}
        while how_many:
            # Convert start_letter to a tensor
            input_tensor = torch.full(
                (1,), all_letters.find(start_letter), dtype=torch.long
            ).to(device)

            # Initialize hidden state
            hidden = model.init_hidden(1, device)

            # Convert gender to a tensor
            gender_tensor = (
                torch.tensor(gender_to_idx[gender], dtype=torch.long)
                .unsqueeze(0)
                .to(device)
            )

            # Initialize the generated name with the start letter
            generated_name = start_letter
            # Repeatedly predict the next character
            for _ in range(max_length - 1):
                # Forward pass
                with torch.no_grad():
                    output, hidden = model(
                        input_tensor.unsqueeze(0), gender_tensor, hidden
                    )
                    output_dist = torch.softmax(output[0] / temperature, dim=-1)
                    top_idx = torch.multinomial(output_dist, 1).item()

                # Check if the index is out-of-bounds, which might signal the end
                if top_idx == oob or top_idx == 0:
                    break

                # Append the predicted letter to the generated name
                next_letter = all_letters[top_idx]
                generated_name += next_letter

                # Update the input tensor for the next iteration
                input_tensor = torch.tensor([top_idx], dtype=torch.long).to(device)

            if (
                end_letter is None
                or generated_name[-1] == end_letter
                and generated_name not in generated_names
            ):
                generated_names.append(generated_name)
                how_many -= 1

        return generated_names
