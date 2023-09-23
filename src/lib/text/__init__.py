class DocObj(object):
    """Definition of an standard document object common to all readers and vocoders."""

    def __init__(self):
        self.doc = []

    def __len__(self):
        """Get the number of pages in the document."""
        return len(self.doc)

    def insert_page(self, page_text):
        """Insert a page in the book."""
        self.doc.append(page_text)

    def get_page(self, page_id):
        """Get the page in a document."""
        return self.doc[page_id]

    def get_all_text(self):
        """This function returns all the text concatenated, regardless of the number of pages or sections.

        Returns
        ------
        str
            text of the book
        """
        return " ".join(self.doc)
