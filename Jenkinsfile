pipeline { 
    agent any

    environment {
        ANSIBLE_PLAYBOOK = "playbook.yml"            // Ruta al playbook de Ansible
        INVENTORY_FILE = "inventory/hosts"          // Ruta al archivo de inventario
        ANSIBLE_USER = "Ruben"                      // Usuario de Ansible
        ANSIBLE_PASSWORD = credentials('ansible_password') // Contraseña almacenada en Jenkins como credencial segura
    }

    stages {
        stage('Подготовка окружения') {
            steps {
                script {
                    echo "Этап 1: Подготовка окружения (установка Docker, клонирование репозиториев)"
                }
                sh """
                    ansible-playbook ${ANSIBLE_PLAYBOOK} \
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
                    ansible-playbook ${ANSIBLE_PLAYBOOK} \
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
