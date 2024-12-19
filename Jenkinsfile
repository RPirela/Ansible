pipeline { 
    agent any

    environment {
        ANSIBLE_PLAYBOOK = "playbook.yml" // Ruta al archivo playbook de Ansible
        INVENTORY_FILE = "inventory/hosts" // Ruta al archivo de inventario
        ANSIBLE_USER = "Ruben" // Usuario Ansible
        ANSIBLE_PASSWORD = credentials('ansible_password') // Credencial segura almacenada en Jenkins
    }

    stages {
        stage('Preparar Entorno') {
            steps {
                script {
                    echo "Etapa 1: Preparar entorno - Instalación de dependencias y configuración"
                }
                sh """
                    ansible --version
                    which ansible-playbook
                """
            }
        }

        stage('Ejecutar Playbook') {
            steps {
                script {
                    echo "Etapa 2: Ejecutar playbook de Ansible"
                }
                sh """
                    ansible-playbook ${ANSIBLE_PLAYBOOK} \
                    -i ${INVENTORY_FILE} \
                    --user=${ANSIBLE_USER} \
                    --extra-vars "ansible_become_pass=${ANSIBLE_PASSWORD}" \
                    --tags docker_setup,clone_repository
                """
            }
        }

        stage('Iniciar Aplicaciones') {
            steps {
                script {
                    echo "Etapa 3: Iniciar aplicaciones"
                }
                sh """
                    ansible-playbook ${ANSIBLE_PLAYBOOK} \
                    -i ${INVENTORY_FILE} \
                    --user=${ANSIBLE_USER} \
                    --extra-vars "ansible_become_pass=${ANSIBLE_PASSWORD}" \
                    --tags start_services
                """
            }
        }
    }

    post {
        always {
            echo "Pipeline completado."
        }
        failure {
            echo "Pipeline fallido."
        }
    }
}
