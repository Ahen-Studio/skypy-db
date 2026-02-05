"""

"""

from typing import (
    List,
    Callable
)

class SysEmbeddings:
    def set_embedding_function(
        self,
        embedding_function: Callable[[List[str]], List[List[float]]]
    ) -> None:
        """
        Set the embedding function for the database.

        Args:
            embedding_function: Function that takes texts and returns embeddings
        """

        self.embedding_function = embedding_function