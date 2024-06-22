# Este arquivo localiza o job pelo uuid do processo
from worker_automate_hub.tasks.jobs.fazer_pudim import (
    current_task_status,
    fazer_pudim,
)

# TODO obter lista de tarefas via request
task_definitions = {
    '5b295021-8df7-40a1-a45e-fe7109ae3902': fazer_pudim,
}

task_status = current_task_status
