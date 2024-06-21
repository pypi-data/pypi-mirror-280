class Acknowledgement:
    def __init__(self, acknowledgement: str, message: str, data=None):
        self.acknowledgement_id = acknowledgement
        self.message = message
        self.data = data

    def __str__(self):
        return f"Acknowledgement(acknowledgement={self.acknowledgement_id}, message={self.message})"
