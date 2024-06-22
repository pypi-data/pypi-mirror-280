import aiohttp
from rich.console import Console

from worker_automate_hub.api.helpers.api_helpers import handle_api_response
from worker_automate_hub.config.settings import API_AUTHORIZATION, API_BASE_URL
from worker_automate_hub.utils.logger import setup_logger
from worker_automate_hub.utils.util import get_new_task_info, get_system_info

logger = setup_logger('client_logger', 'app.log')
console = Console()
headers = {'Authorization': f'Basic {API_AUTHORIZATION}'}


async def get_new_task():
    try:
        data = await get_new_task_info()

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f'{API_BASE_URL}/robo/jobs/new-job',
                data=data,
                headers=headers,
            ) as response:
                return await handle_api_response(response)

    except Exception as e:
        logger.error(f'Erro ao obter nova tarefa: {e}')
        console.print(
            f'Erro ao obter nova tarefa: {e}',
            style='bold red',
        )
        return None


async def notify_is_alive():
    try:
        data = await get_system_info()

        async with aiohttp.ClientSession() as session:
            async with session.put(
                f'{API_BASE_URL}/robo/info/last-alive',
                data=data,
                headers=headers,
            ) as response:
                return await handle_api_response(response, last_alive=True)

    except Exception as e:
        logger.error(f'Erro ao informar is alive: {e}')
        console.print(
            f'Erro ao informar is alive: {e}',
            style='bold red',
        )
        return None


async def get_workers():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f'{API_BASE_URL}/robo',
                headers=headers,
            ) as response:
                return await response.json()

    except Exception as e:
        logger.error(f'Erro ao obter a lista de workers: {e}')
        console.print(
            f'Erro ao obter a lista de workers: {e}',
            style='bold red',
        )
        return None
