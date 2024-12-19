pipeline {
    agent any

    environment {
        ANSIBLE_PLAYBOOK = "/usr/bin/ansible-playbook" // Ruta completa al ejecutable ansible-playbook
        PLAYBOOK_PATH = "ansible/main.yml"            // Ruta al playbook
        INVENTORY_FILE = "ansible/inventory"          // Ruta al inventory
    }

    stages {
        stage('Подготовка окружения') {
            steps {
                script {
                    echo "Этап 1: Подготовка окружения (установка Docker, клонирование репозиториев)"
                }
                sh """
                    ${ANSIBLE_PLAYBOOK} ${PLAYBOOK_PATH} -i ${INVENTORY_FILE} --tags docker_setup,clone_repository
                """
            }
        }

        stage('Запуск приложений') {
            steps {
                script {
                    echo "Этап 2: Запуск приложений (Docker Compose)"
                }
                sh """
                    ${ANSIBLE_PLAYBOOK} ${PLAYBOOK_PATH} -i ${INVENTORY_FILE} --tags start_services
                """
            }
        }
    }
}
