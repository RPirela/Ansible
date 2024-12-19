pipeline { 
    agent any

    environment {
        ANSIBLE_PLAYBOOK = "/usr/bin/ansible-playbook" // Ruta completa al ejecutable ansible-playbook
        INVENTORY_FILE = "inventory/hosts"            // Ruta al archivo de inventario
        ANSIBLE_USER = "Ruben"                        // Usuario Ansible
        ANSIBLE_PASSWORD = credentials('ansible_password') // Contraseña almacenada en Jenkins como credencial segura
    }

    stages {
        stage('Подготовка окружения') {
            steps {
                script {
                    echo "Этап 1: Подготовка окружения (установка Docker, клонирование репозиториев)"
                }
                sh """
                    ${ANSIBLE_PLAYBOOK} playbook.yml \
                    -i ${INVENTORY_FILE} \
                    --user=${ANSIBLE_USER} \
                    --extra-vars 'ansible_password=${ANSIBLE_PASSWORD}' \
                    --tags docker_setup,clone_repository
                """
            }
        }

        stage('Запуск приложений') {
            steps {
                script {
                    echo "Этап 2: Запуск приложений (Docker Compose)"
                }
                sh """
                    ${ANSIBLE_PLAYBOOK} playbook.yml \
                    -i ${INVENTORY_FILE} \
                    --user=${ANSIBLE_USER} \
                    --extra-vars 'ansible_password=${ANSIBLE_PASSWORD}' \
                    --tags start_services
                """
            }
        }
    }

    post {
        always {
            script {
                echo "Pipeline завершен."
            }
        }
        failure {
            script {
                echo "Pipeline завершен с ошибкой."
            }
        }
    }
}
