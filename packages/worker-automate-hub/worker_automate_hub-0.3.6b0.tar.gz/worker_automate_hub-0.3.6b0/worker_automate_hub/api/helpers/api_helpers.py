from worker_automate_hub.utils.logger import setup_logger
from worker_automate_hub.utils.updater import check_for_update

logger = setup_logger('helpers_logger', 'app.log')


async def handle_api_response(response, last_alive=False):
    status = response.status
    match status:
        case 200:
            if last_alive:
                print('Last alive informado salvo com sucesso')
            else:
                data = await response.json()
                return {'data': data, 'update': False}
        case 204:
            logger.info('204 - Nenhum processo encontrado')
        case 300:
            logger.info('300 - Necessário atualização!')
            check_for_update()
        case 401:
            logger.error('401 - Acesso não autorizado!')
        case 404:
            logger.error('404 - Nenhum processo disponível!')
        case 500:
            logger.error('500 - Erro interno da API!')
        case _:
            logger.error(f'Status não tratado: {status}')
    return None
