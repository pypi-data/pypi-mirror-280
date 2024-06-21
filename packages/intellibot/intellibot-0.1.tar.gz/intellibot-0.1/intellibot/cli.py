import click
from intellibot.api import IntelliBotAPI
from colorama import Fore, Style, init

init(autoreset=True)

intelli_bot = IntelliBotAPI()


@click.group()
def cli():
    pass


@cli.command()
@click.option("--username", prompt="Username", help="Username to connect")
@click.option(
    "--password",
    prompt=True,
    hide_input=True,
    confirmation_prompt=True,
    help="Password to connect",
)
def connect(username, password):
    """Connect to the intellibot."""
    response = intelli_bot.connect(username, password)
    if response.status_code == 200:
        click.echo(Fore.GREEN + "Connected successfully!\n\n")
        click.echo(Fore.GREEN + "\t\t**** Welcome to intelligent chatbot!  ****\n\n")
        click.echo(Fore.GREEN + '\t\t**** Type "exit" to quit the chat. ****\n\n')

        while True:
            message = click.prompt(Fore.BLUE + f"{username}", type=str)
            if message.lower() in ["exit", "quit"]:
                click.echo(Fore.YELLOW + "\n\n \t\t\t***** Goodbye! *****\n\n")
                break
            send_message(message)
    else:
        click.echo("Connection failed!")


def send_message(message):
    try:
        response = intelli_bot.chat(message)
        if response.status_code == 200:
            click.echo(Fore.YELLOW + "\nintellibot: " + Style.RESET_ALL + f'{response.json().get("response")}\n')
        else:
            click.echo(Fore.RED + "Failed to get a response from the bot.")
    except Exception as e:
        click.echo(str(e))


@cli.command()
@click.argument("message")
def chat(message):
    """Chat with the intellibot."""
    try:
        response = intelli_bot.chat(message)
        if response.status_code == 200:
            click.echo(Fore.YELLOW + "\nintellibot :" + Style.RESET_ALL + f'{response.json().get("response")}')
        else:
            click.echo(Fore.RED + "Failed to get a response from the bot.")
    except Exception as e:
        click.echo(Fore.RED + str(e))


if __name__ == "__main__":
    cli()
