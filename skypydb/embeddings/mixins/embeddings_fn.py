"""
Module containing the EmbeddingsFn class, which is used to generate embeddings for a list of texts.
"""

from typing import List
from skypydb.embeddings.mixins import SysGet

class EmbeddingsFn:
    def embed(
        self,
        texts: List[str],
    ) -> List[List[float]]:
        """
        Generate embeddings for a list of texts.

        Args:
            texts: List of texts to embed

        Returns:
            List of embedding vectors
        """

        embeddings = []

        for text in texts:
            embedding = self._get_embedding(text)
            embeddings.append(embedding)

            # Cache the dimension from the first embedding
            if self._dimension is None:
                self._dimension = len(embedding)

        return embeddings

    def get_embedding_function(
        model: str = "mxbai-embed-large",
        base_url: str = "http://localhost:11434",
    ) -> Callable[[List[str]], List[List[float]]]:
        """
        Get an embedding function using Ollama.
    
        This is a convenience function that returns a callable
        embedding function for use with the vector database.
    
        Args:
            model: Name of the Ollama embedding model
            base_url: Base URL for Ollama API
    
        Returns:
            Callable that takes a list of texts and returns embeddings
    
        Example:
            embed_fn = get_embedding_function(model="mxbai-embed-large")
            embeddings = embed_fn(["Hello world", "How are you?"])
        """
    
        return OllamaEmbedding(model=model, base_url=base_url)
