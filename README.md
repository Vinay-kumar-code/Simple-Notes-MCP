# Simple Notes MCP Server

A lightweight Model Context Protocol (MCP) server that provides in-memory note-taking functionality. This server allows AI assistants and other MCP clients to create, read, search, and delete notes through a simple set of tools.

## What is MCP?

Model Context Protocol (MCP) is an open protocol that enables seamless integration between AI applications and external data sources. It allows AI assistants like Claude to interact with your tools and data in a standardized way.

## Features

- **Add Notes**: Create new notes with a title and content
- **List Notes**: View all stored notes
- **Search Notes**: Find specific notes by title (case-insensitive)
- **Delete Notes**: Remove notes by title
- **In-Memory Storage**: Fast, lightweight storage that persists during runtime

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone or download this repository

2. Install the required dependencies:
```bash
pip install mcp
```

## Usage

### Running the Server

The server runs using stdio (standard input/output) transport:

```bash
python notes_server.py
```

### Connecting to MCP Clients

To use this server with Claude Desktop or other MCP clients, add it to your MCP configuration file:

#### For Claude Desktop

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "simple-notes": {
      "command": "python",
      "args": ["c:/Users/vinay/OneDrive/Documents/Codes/notes_server.py"]
    }
  }
}
```

**Configuration File Locations:**
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

After updating the configuration, restart Claude Desktop.

## Available Tools

### 1. `add_note`
Adds a new note to the in-memory storage.

**Parameters:**
- `title` (string): The title of the note
- `content` (string): The body text of the note

**Example:**
```
Add a note with title "Meeting Notes" and content "Discussed Q4 objectives"
```

### 2. `list_notes`
Retrieves all notes currently stored in memory.

**Parameters:** None

**Example:**
```
Show me all my notes
```

### 3. `get_note_by_title`
Finds a specific note by its title (case-insensitive search).

**Parameters:**
- `title` (string): The title of the note to search for

**Example:**
```
Find the note titled "Meeting Notes"
```

### 4. `delete_note`
Deletes a note by its title (case-insensitive).

**Parameters:**
- `title` (string): The title of the note to delete

**Example:**
```
Delete the note titled "Meeting Notes"
```

## How It Works

1. **FastMCP Framework**: The server uses FastMCP, a lightweight framework for building MCP servers in Python.

2. **In-Memory Storage**: Notes are stored in a Python list as dictionaries during runtime. Data is lost when the server stops.

3. **Tool Decorators**: The `@mcp.tool()` decorator exposes Python functions as MCP tools that clients can invoke.

4. **Stdio Transport**: The server communicates via standard input/output, making it compatible with various MCP clients.

## Limitations

- **No Persistence**: Notes are stored in memory only and will be lost when the server stops
- **Single User**: The server doesn't support multiple users or sessions
- **No Authentication**: No built-in security or access control

## Future Enhancements

Potential improvements for this server:

- [ ] Add persistent storage (JSON file, SQLite database)
- [ ] Implement note editing functionality
- [ ] Add tags or categories for notes
- [ ] Support for note timestamps
- [ ] Search by content, not just title
- [ ] Export notes to different formats

## Technical Details

**Built with:**
- Python 3.x
- FastMCP (Model Context Protocol SDK)

**Architecture:**
- Transport: stdio
- Storage: In-memory (Python list)
- Communication: JSON-RPC over MCP

## Troubleshooting

### Server not appearing in Claude Desktop

1. Check that the path in `claude_desktop_config.json` is correct
2. Ensure Python is in your system PATH
3. Restart Claude Desktop after configuration changes
4. Check Claude Desktop logs for errors

### Import Errors

Make sure `mcp` is installed:
```bash
pip install mcp
```

## License

This project is open source and available for use and modification.

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io)
- [FastMCP GitHub Repository](https://github.com/jlowin/fastmcp)
- [MCP Specification](https://spec.modelcontextprotocol.io)

---

**Note**: This is a simple demonstration server. For production use, consider adding persistent storage, error handling, and security features.
