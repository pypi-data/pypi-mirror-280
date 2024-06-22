import importlib.metadata
import subprocess
import sys

import requests
from packaging import version
from rich.console import Console

console = Console()


def update_package():
    """Update the current package to the latest version."""
    package_name = 'worker-automate-hub'

    try:
        # Execute o comando pip para instalar a última versão do pacote
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install', '--upgrade', package_name]
        )
        console.print('Package atualizado com sucesso!', style='green')
    except subprocess.CalledProcessError as e:
        console.print(f'Falha ao atualizar o package: {e}', style='bold red')
        sys.exit(1)


def check_for_update():
    """Check if there is a new version of the package available on PyPI."""
    package_name = 'worker-automate-hub'
    current_version = importlib.metadata.version(package_name)

    response = requests.get(f'https://pypi.org/pypi/{package_name}/json')
    latest_version = response.json()['info']['version']

    if version.parse(latest_version) > version.parse(current_version):
        console.print(
            f'Uma nova versão [bold cyan]({latest_version})[/bold cyan] está disponível. Atualizando...'
        )
        update_package()
    else:
        console.print(
            '\nVocê está usando a versão mais atualizada.', style='green'
        )
