class indexer:
    def __init__(
        self, filters="`~!@#$%^&*()_-+=/?:;,.\|'", split=" ", document_count=0
    ):
        self.filters = filters
        self.split = split
        self.document_count = document_count

    def fit_text(self, text):
        for cursor in text:
            self.document_count += 1
            if cursor in self.filters:
                text = text.replace(cursor, "")
        text = text.split(self.split)
        for word in text:
            if word:
                self.document_count += 1
