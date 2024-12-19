pipeline { 
    agent any

    environment {
        ANSIBLE_PLAYBOOK = "/usr/bin/ansible-playbook" // Asegúrate de que esta ruta sea correcta
        INVENTORY_FILE = "inventory/hosts"
        ANSIBLE_USER = "Ruben"
        ANSIBLE_PASSWORD = credentials('ansible_password')
    }

    stages {
        stage('Debug Ansible') {
            steps
            steps {
                sh """
                    which ansible-playbook
                    ansible-playbook --version
                """
            }
        }

        stage('Подготовка окружения') {
            steps {
                script {
                    echo "Этап 1: Подготовка окружения (установка Docker, клонирование репозиториев)"
                }
                sh """
                    ${ANSIBLE_PLAYBOOK} ${ANSIBLE_PLAYBOOK} \
                    -i ${INVENTORY_FILE} \
                    --user=${ANSIBLE_USER} \
                    --extra-vars 'ansible_become_pass=${ANSIBLE_PASSWORD} ansible_python_interpreter=/usr/bin/python3' \
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
                    ${ANSIBLE_PLAYBOOK} ${ANSIBLE_PLAYBOOK} \
                    -i ${INVENTORY_FILE} \
                    --user=${ANSIBLE_USER} \
                    --extra-vars 'ansible_become_pass=${ANSIBLE_PASSWORD} ansible_python_interpreter=/usr/bin/python3' \
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
