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

To use this server with Claude Desktop or other MCP clients, add it to your MCP configuration file.

After updating the configuration, restart Claude Desktop.


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


## License

This project is open source and available for use and modification.

## Contributing

Feel free to fork this project and submit pull requests for improvements!
