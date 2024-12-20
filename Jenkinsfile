pipeline {
    agent any
    environment {
        INVENTORY_FILE = "/mnt/c/Users/Ruben/PycharmProjects/Devps/DevOps3/inventory/hosts"
        ANSIBLE_PLAYBOOK = "/mnt/c/Users/Ruben/PycharmProjects/Devps/DevOps3/playbook.yml"
        ANSIBLE_USER = "Ruben"
        ANSIBLE_BECOME_PASS = "001999"
        ANSIBLE_HOST_KEY_CHECKING = "False"
    }
    stages {
        stage('Probar conexión SSH') {
            steps {
                script {
                    echo 'Probando conexión SSH con WSL...'
                }
                sh '''
                    ssh -o StrictHostKeyChecking=no ${ANSIBLE_USER}@127.0.0.1 "echo Conexión exitosa"
                '''
            }
        }
        stage('Preparar Entorno') {
            steps {
                script {
                    echo 'Instalando dependencias si es necesario...'
                }
                sh '''
                    wsl bash -c '
                    if ! command -v ansible >/dev/null 2>&1; then
                        echo "Ansible no está instalado. Instalando Ansible..."
                        sudo apt update
                        sudo apt install -y ansible
                    else
                        echo "Ansible ya está instalado."
                    fi
                    '
                '''
            }
        }
        stage('Ejecutar Playbook') {
            steps {
                script {
                    echo 'Ejecutando el playbook de Ansible...'
                }
                sh '''
                    wsl bash -c '
                    ansible-playbook ${ANSIBLE_PLAYBOOK} \
                    -i ${INVENTORY_FILE} \
                    --user=${ANSIBLE_USER} \
                    --extra-vars "ansible_become_pass=${ANSIBLE_BECOME_PASS} ansible_python_interpreter=/usr/bin/python3" \
                    --tags docker_setup,clone_repository,start_services
                    '
                '''
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
