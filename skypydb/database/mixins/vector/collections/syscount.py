"""

"""

from skypydb.security.validation import InputValidator

class SysCount:
    def count(
        self,
        collection_name: str
    ) -> int:
        """
        Count items in a collection.

        Args:
            collection_name: Name of the collection

        Returns:
            Number of items in the collection
        """

        collection_name = InputValidator.validate_table_name(collection_name)

        if not self.collection_exists(collection_name):
            raise ValueError(f"Collection '{collection_name}' not found")

        cursor = self.conn.cursor()

        cursor.execute(f"SELECT COUNT(*) FROM [vec_{collection_name}]")
        return cursor.fetchone()[0]