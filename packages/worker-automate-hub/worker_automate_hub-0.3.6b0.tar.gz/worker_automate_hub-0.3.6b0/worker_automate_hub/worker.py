import asyncio

import pyfiglet
from rich.console import Console

from worker_automate_hub.api.client import get_new_task, notify_is_alive
from worker_automate_hub.config.settings import (
    LOG_LEVEL,
    NOTIFY_ALIVE_INTERVAL,
    VERSION,
)
from worker_automate_hub.tasks.task_executor import perform_task
from worker_automate_hub.utils.logger import setup_logger

logger = setup_logger('main_logger', 'app.log', LOG_LEVEL)
console = Console()


async def check_and_execute_tasks():
    while True:
        try:
            task = await get_new_task()
            logger.info(f"Executando a task: {task['data']['nomProcesso']}")
            await perform_task(task['data'])
            await asyncio.sleep(5)
        except Exception as e:
            logger.error(f'Ocorreu um erro de execução: {e}')
            await asyncio.sleep(5)


async def notify_alive():
    while True:
        try:
            logger.info('Notificando last alive...')
            await notify_is_alive()
            await asyncio.sleep(NOTIFY_ALIVE_INTERVAL)
        except Exception as e:
            logger.error(f'Erro ao notificar que está ativo: {e}')
            await asyncio.sleep(NOTIFY_ALIVE_INTERVAL)


async def main_process():
    custom_font = 'slant'
    ascii_banner = pyfiglet.figlet_format(f'Worker', font=custom_font)
    console.clear()
    console.print(ascii_banner + f' versão: {VERSION}\n', style='bold blue')
    logger.info('Worker em execução.')
    console.print('Worker em execução.\n', highlight=True)

    tasks = [check_and_execute_tasks(), notify_alive()]
    await asyncio.gather(*tasks)


def run_worker():
    try:
        while True:
            asyncio.run(main_process())
            break
    except asyncio.CancelledError:
        console.print('Aplicação encerrada pelo usuário.')
