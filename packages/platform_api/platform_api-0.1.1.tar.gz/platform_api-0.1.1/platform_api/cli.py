import click
import importlib

@click.group()
def cli():
    pass

entity_groups = [
    'tags',
    'projects'
]

for entity in entity_groups:
    try:
        module = importlib.import_module(f'platform_api.cli_commands.{entity}')
        if hasattr(module, '__all__'):
            for command_name in module.__all__:
                command = getattr(module, command_name)
                cli.add_command(command)
        else:
            click.echo(f"Module '{entity}' does not define __all__.")

    except AttributeError as e:
        click.echo(f"Failed to load commands for '{entity}': {e}")
    except ModuleNotFoundError as e:
        click.echo(f"Module '{entity}' not found: {e}")

if __name__ == '__main__':
    cli()
