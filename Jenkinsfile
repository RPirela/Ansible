pipeline {
    agent {
        docker {
            image 'ansible/ansible:latest'
        }
    }
    environment {
        ANSIBLE_PLAYBOOK = "playbook.yml"
        INVENTORY_FILE = "inventory/hosts"
        ANSIBLE_USER = "Ruben"
        ANSIBLE_PASSWORD = credentials('ansible_password')
    }
    stages {
        stage('Preparar Entorno') {
            steps {
                script {
                    echo "Etapa 1: Preparar entorno - Instalación de dependencias y configuración"
                }
                sh """
                    ansible --version
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
