from mcp.server.fastmcp import FastMCP

# Initialize the FastMCP server
mcp = FastMCP("Simple Notes")

# In-memory storage using a Python list
# Each note will be a dictionary: {"title": str, "content": str}
notes = []

@mcp.tool()
def add_note(title: str, content: str) -> str:
    """
    Adds a new note to the in-memory list.
    
    Args:
        title: The title of the note.
        content: The body text of the note.
    """
    note = {"title": title, "content": content}
    notes.append(note)
    return f"Note '{title}' added successfully."

@mcp.tool()
def list_notes() -> str:
    """
    Retrieves all notes currently stored in memory.
    """
    if not notes:
        return "No notes found."
    
    # Format the notes into a readable string
    result = "Current Notes:\n\n"
    for i, note in enumerate(notes, 1):
        result += f"{i}. {note['title']}\n   {note['content']}\n\n"
    
    return result.strip()

@mcp.tool()
def get_note_by_title(title: str) -> str:
    """
    Finds a specific note by its title.
    
    Args:
        title: The title of the note to search for.
    """
    for note in notes:
        if note['title'].lower() == title.lower():
            return f"Found note:\nTitle: {note['title']}\nContent: {note['content']}"
            
    return f"No note found with title '{title}'"

@mcp.tool()
def delete_note(title: str) -> str:
    """
    Deletes a note by its title.

    Args:
        title: The title of the note to delete.
    """
    global notes
    initial_count = len(notes)
    notes = [note for note in notes if note['title'].lower() != title.lower()]
    
    if len(notes) < initial_count:
        return f"Note '{title}' deleted."
    return f"Note '{title}' not found."

if __name__ == "__main__":
    # Runs the server over stdio
    mcp.run()