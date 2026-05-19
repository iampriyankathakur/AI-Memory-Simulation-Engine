from rich.console import Console
from rich.panel import Panel

console = Console()

def show_memory_results(results):

    for memory, score in results:

        console.print(
            Panel(
                f"{memory}\n\nScore: {score:.3f}",
                title="🧠 Retrieved Memory"
            )
        )
