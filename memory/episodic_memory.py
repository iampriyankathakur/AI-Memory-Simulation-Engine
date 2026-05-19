import time

class EpisodicMemory:

    def __init__(self, content, embedding):
        self.content = content
        self.embedding = embedding
        self.timestamp = time.time()
        self.strength = 1.0
