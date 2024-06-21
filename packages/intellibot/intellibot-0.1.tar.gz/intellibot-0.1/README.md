
# Intellibot
 Intellibot is a terminal-based chatbot client for interacting with cloud platform. It allows users to connect to the platform using their credentials and chat with the bot through a command-line interface.

## Installation

To install Intellibot, run:

```sh
pip install Intellibot
```

## Usage

### Connect to Intellibot

To connect to Intellibot, use the `connect` command with your username and password:

```sh 
Intellibot connect 
username <your-username> 
password <your-password>
```

Example:

```sh 
Intellibot connect 
username jane@gmail.com 
password pass
```

### Chat with Intellibot

Once connected, you can send messages to the bot using the `chat` command:

```sh 
Intellibot chat "<your-message>"
```

Example:

```sh 
Intellibot chat "Hello, Intellibot!"
```

## Development

To install the package locally for development, navigate to the root directory (where `setup.py` is located) and run:

```sh
pip install .
```

You can then use the  Intellibot` CLI commands as described above to test the functionality.

## Project Structure

``` Intellibot/
├── Intellibot/
│   ├── __init__.py
│   ├── cli.py
│   └── api.py
├── setup.py
├── README.md
├── requirements.txt
└── MANIFEST.in
```

### API Module (`api.py`)

The `api.py` module contains the  IntellibotAPI` class, which handles the connection and chat functionalities.

### CLI Module (`cli.py`)

The `cli.py` module defines the command-line interface using `click`. It includes commands for connecting to the backend and chatting with the bot.

## License

This project is licensed under the MIT License.