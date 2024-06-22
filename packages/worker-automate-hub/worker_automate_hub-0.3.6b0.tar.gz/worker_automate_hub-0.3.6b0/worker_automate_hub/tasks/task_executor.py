from worker_automate_hub.tasks.task_definitions import (
    task_definitions,
    task_status,
)
from worker_automate_hub.utils.logger import setup_logger

logger = setup_logger('executor_logger', 'app.log')


async def perform_task(task):
    try:
        logger.info(f"Processo a ser executado: {task['nomProcesso']}")
        task_uuid = task['uuidProcesso']
        if task_uuid in task_definitions:
            result = await task_definitions[task_uuid]()
            return result
        else:
            logger.error(f'Processo não encontrado: {task_uuid}')
            return None
    except Exception as e:
        logger.error(f'Erro ao performar o processo: {e}')
