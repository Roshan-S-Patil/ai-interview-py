# If you want to wrap or extend memory saving, or perhaps swap persistence backend

# For now, we just import MemorySaver from langgraph
from langgraph.checkpoint.memory import MemorySaver

def get_memory_saver():
    return MemorySaver()
