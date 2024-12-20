pipeline {
    agent any
    environment {
        INVENTORY_FILE = "inventory/hosts"
        ANSIBLE_PLAYBOOK = "playbook.yml"
        ANSIBLE_BECOME_PASS = "001999"
    }
    stages {
        stage('Preparar Entorno') {
            steps {
                script {
                    echo 'Instalando dependencias si es necesario...'
                }
                sh '''
                    if ! command -v ansible >/dev/null 2>&1; then
                        echo "Ansible no está instalado. Instalando Ansible..."
                        sudo apt update
                        sudo apt install -y ansible
                    else
                        echo "Ansible ya está instalado."
                    fi
                '''
            }
        }
        stage('Ejecutar Playbook') {
            steps {
                script {
                    echo 'Ejecutando el playbook de Ansible...'
                }
                sh """
                    ansible-playbook ${ANSIBLE_PLAYBOOK} \
                    -i ${INVENTORY_FILE} \
                    --extra-vars "ansible_become_pass=${ANSIBLE_BECOME_PASS} ansible_python_interpreter=/usr/bin/python3" \
                    --tags docker_setup,clone_repository,start_services
                """
            }
        }
    }
    post {
        always {
            echo 'Pipeline completado.'
        }
        failure {
            echo 'Pipeline fallido.'
        }
    }
}
