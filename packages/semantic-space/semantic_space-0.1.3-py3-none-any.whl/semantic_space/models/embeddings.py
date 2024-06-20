"""
    A collection of models related to embeddings.
"""

import numpy as np
from typing import List, Union, Tuple
from ..utils.log import logger
from ..tools.tokens import token16, token32, detokenify

def contexts(tokens: Union[List[Union[token16, token32]], List[int]],
                  window: int = 3) -> Tuple[List[int], List[int]]:
    """
        Match words with their context words given the window size.

        Args:
            tokens: An ordered token list or a list of integers,
                representing the token ids.

            window (int): The window size to pick context tokens
                from. The window goes both forwards and backwards
                from the current location of an investigated token.

        Returns:
            A tuple of length 2. First element is the list of tokens
            ids that are investigated. Second element is alist of
            lists, each containing corresponding context tokens to
            the investigated ones in order.
    """
    if isinstance(tokens[0], Union[token16, token32]):
        tokens = detokenify(tokens)

    contexts = {}
    begin: int
    end: int
    N = len(tokens)
    for i, token in enumerate(tokens):
        if token not in contexts:
            contexts[token] = []

        begin = max(0, i - window)
        end = min(i + window + 1, N)

        for context in tokens[begin:end]:
            if context == token:
                continue
            contexts[token].append(context)

    return list(contexts.keys()), list(contexts.values())

def negatives(vocab_size: int, count: int = 15) -> Tuple[List[int], List[int]]:
    """
        Create "negative" tokens for each given token in the vocabulary.

        Args:
            vocab_size (int): Vocabulary size of the text that is the subject.

            count (int): The count of negatives words to match with each token
                in the vocabulary.

        Returns:
            A tuple of lists. The first list is the list of token ids. The second
            list, is a list of lists where each sublist is the collection of negative
            words corresponding to the same indexed token in the first list.
    """
    return list(range(vocab_size)), [[np.random.randint(0, vocab_size) for l in range(count)] for k in range(vocab_size)]

class SkipGram:
    """
        Default skipgram model as it was in word2vec.
    """

    def __init__(self, vocab_size: int, dim: int, mean: np.float32 = 0, std: np.float32 = 1):
        self.vocab_size = vocab_size
        self.dim = dim
        self.core = np.random.normal(mean, std, (2*vocab_size, dim,))
        # The bottom half of the matrix is "context" vectors

    def __getitem__(self, item: int):
        return self.core[item]

    def step_positive(self, input: int, context: int, lr: np.float32):
        """
            Takes a positive step, which means, gets the input vector
            closer to the given context vectors.

            Args:
                input (int): An integer representing a token-id.

                context (int): An integer representing the token-id
                    of a context word.

                lr (np.float32): Learning rate. No default values given.
        """
        new_input = self.core[input] + lr * self.core[self.vocab_size + context]
        new_context = self.core[self.vocab_size + context] + lr * self.core[input]
        self.core[input] = new_input
        self.core[self.vocab_size + context] = new_context

    def step_negative(self, input: int, negative: int, lr: np.float32):
        """
            Takes a negative step, which means, gets the input vector
                further from the given negative vectors.

            Args:
                input (int): An integer representing a token-id.

                negative (int): An integer representing the token-id
                    of a negative word.

                lr (np.float32): Learning rate. No default values given.
        """
        new_input = self.core[input] - lr * self.core[self.vocab_size + negative]
        new_negative = self.core[self.vocab_size - negative] - lr * self.core[input]
        self.core[input] = new_input
        self.core[self.vocab_size + negative] = new_negative

    def loss(self, inputs: List[int], contexts: List[List[int]], negatives: List[List[int]]) -> np.float32:
        """
            Calculate the loss of an embedding system with the
            dot product similarity.

            Args:
                inputs: A list of integers containing token-ids of
                    all relevant tokens.

                contexts: A list-matrix of integers containing all
                    relevant context token-ids.

                negatives: A list-matrix of integers containing all
                    relevant negative token-ids.

            Returns:
                The calculated total error of the model, of type
                numpy.float32.
        """
        e: np.float32 = 0
        for i, input in enumerate(inputs):
            for context in contexts[i]:
                e -= np.dot(self.core[input], self.core[self.vocab_size + context])
            for negative in negatives[i]:
                e += np.dot(self.core[input], self.core[self.vocab_size + negative])
        return e / (len(contexts) + len(negatives))

    def fit(self, inputs: List[int], contexts: List[List[int]], negatives: List[List[int]],
            epochs: int = 1, lr: np.float32 = 0.001, lr_decay: np.float32 = 1):
        """
            Train the SkipGram model on given tokens, context tokens and negative
            tokens.

            Args:
                inputs: A list of integers containing token-ids of
                    all relevant tokens.

                contexts: A list-matrix of integers containing all
                    relevant context token-ids.

                negatives: A list-matrix of integers containing all
                    relevant negative token-ids.

                epochs (int): Integer representing the total count of
                    epochs to train the model during.

                lr (np.float32): Learning rate of the training. Default
                    value is 0.001.

                lr_decay (mp.float32): Decay of the learning rate to
                    perform after each epoch. By default, the value is
                    1. Meaning, there is no decay.
        """
        for epoch in range(epochs):
            for i, input in enumerate(inputs):
                for context in contexts[i]:
                    self.step_positive(input, context, lr)
                for negative in negatives[i]:
                    self.step_negative(input, negative, lr)
            logger.info(f"Loss at epoch {epoch + 1}: {self.loss(inputs, contexts, negatives)}")
            lr *= lr_decay

    def save(self, path: str):
        """
            Save the core embedding vector-matrix of the model.
            The saved file will be a numpy array file.

            Args:
                path (str): Path of the embedding file. Extension
                    needs to be included. The file will naturally
                    be a .npy file.
        """
        np.save(path, self.core)

    @staticmethod
    def load(path: str):
        """
            Load a SkipGram model from an .npy or compatible file.

            Args:
                path (str): Path to the ndarray file.

            Returns:
                Returns the SkipGram object created from the embedding
                vectors.
        """
        core = np.load(path)
        vocab_size = core.shape[0] // 2
        dim = core.shape[1]
        model = SkipGram(vocab_size, dim)
        model.core = core
        return model





