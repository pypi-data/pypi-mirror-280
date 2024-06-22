import psutil
from prompt_toolkit.shortcuts import checkboxlist_dialog, radiolist_dialog
from rich.console import Console

from worker_automate_hub.config.settings import UUID_ROBO, VERSION
from worker_automate_hub.tasks.task_definitions import (  # Importando a variável global corretamente
    task_status,
)

console = Console()


async def get_system_info():
    max_cpu = psutil.cpu_percent(interval=10.0)
    cpu_percent = psutil.cpu_percent(interval=1.0)
    memory_info = psutil.virtual_memory()

    return {
        'uuidRobo': UUID_ROBO,
        'maxCpu': f'{max_cpu}%',
        'maxMem': f'{memory_info.total / (1024 ** 3):.2f} GB',
        'usoCpu': f'{cpu_percent}%',
        'usoMem': f'{memory_info.used / (1024 ** 3):.2f} GB',
        'situacao': f'{task_status}',
    }


async def get_new_task_info():
    return {
        'uuidRobo': UUID_ROBO,
        'versao': VERSION,
    }


def multiselect_prompt(options, title='Select options'):
    result = checkboxlist_dialog(
        values=[(option, option) for option in options],
        title=title,
        text='Use space to select multiple options.\nPress Enter to confirm your selection.',
    ).run()

    if result is None:
        console.print('[red]No options selected.[/red]')
    else:
        return result


def select_prompt(options, chave_1, title='Selecione uma opção'):
    values = [(index, option[chave_1]) for index, option in enumerate(options)]

    result = radiolist_dialog(
        values=values,
        title=title,
        text='Use as teclas de seta para navegar e Enter para selecionar uma opção.',
    ).run()

    if result is None:
        console.print('[red]Nenhuma opção selecionada.[/red]')
    else:
        # Retorna o dicionário correspondente ao índice selecionado
        return options[result]
