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
                    echo 'Preparando el entorno e instalando dependencias...'
                }
                sh '''
                    # Verificar e instalar Ansible
                    if ! command -v ansible >/dev/null 2>&1; then
                        echo "Ansible no está instalado. Instalando..."
                        apt-get update && apt-get install -y ansible
                    else
                        echo "Ansible ya está instalado."
                    fi
                '''
            }
        }
        stage('Clonar Repositorio') {
            steps {
                script {
                    echo 'Clonando el repositorio...'
                }
                sh '''
                    rm -rf /tmp/test-repo || true
                    git clone https://github.com/RPirela/DevOps3.git /tmp/test-repo
                '''
            }
        }
        stage('Ejecutar Playbook') {
            steps {
                script {
                    echo 'Ejecutando el playbook de Ansible...'
                }
                dir('/tmp/test-repo') {
                    sh '''
                        ansible-playbook ${ANSIBLE_PLAYBOOK} \
                        -i ${INVENTORY_FILE} \
                        --extra-vars "ansible_become_pass=${ANSIBLE_BECOME_PASS} ansible_python_interpreter=/usr/bin/python3" \
                        --tags docker_setup,clone_repository,start_services
                    '''
                }
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
