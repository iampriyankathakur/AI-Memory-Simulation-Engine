from src.embedding_engine import Embedder
from src.memory_manager import MemoryManager
from src.memory_scorer import emotional_score
from src.retriever import retrieve_relevant
from app.interface import show_memory_results

def main():

    embedder = Embedder()

    manager = MemoryManager()

    print("\n🧠 AI Memory Simulation Engine\n")

    while True:

        text = input("Enter memory (or 'exit'): ")

        if text.lower() == "exit":
            break

        embedding = embedder.encode(text)

        score = emotional_score(text)

        manager.add_memory(
            text,
            embedding,
            score
        )

        print("\nMemory stored.\n")

    query = input("\nAsk memory query: ")

    query_embedding = embedder.encode(query)

    memories = manager.get_memories()

    results = retrieve_relevant(
        query_embedding,
        memories
    )

    show_memory_results(results)

if __name__ == "__main__":
    main()
