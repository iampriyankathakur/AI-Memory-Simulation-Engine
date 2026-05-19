import json

from memory.episodic_memory import EpisodicMemory
from memory.emotional_memory import EmotionalMemory

class MemoryManager:

    def __init__(self):
        self.memories = []

    def add_memory(self, text, embedding, emotion_score):

        memory = EpisodicMemory(text, embedding)

        emotional_memory = EmotionalMemory(
            text,
            emotion_score
        )

        self.memories.append({
            "memory": memory,
            "emotion": emotional_memory
        })

    def get_memories(self):
        return self.memories
