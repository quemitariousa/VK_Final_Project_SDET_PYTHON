    pipeline {

        agent any
        stages {
            stage('Clone repo') {
                steps {
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: 'main']],
                        userRemoteConfigs: [[
                            credentialsId: 'b152a4f0-a32a-4753-88fb-eb6c279eb8fc',
                            url: 'https://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@github.com/quemitariousa/VK_Final_Project_SDET_PYTHON.git']]
                    ])
                }
            }

            stage('Run docker-compose') {
                steps {
                    step([
                        $class: 'DockerComposeBuilder',
                        dockerComposeFile: 'FinalProject/docker-compose.yml',
                        option: [$class: 'StartAllServices'],
                        useCustomDockerComposeFile: true
                    ])
                }
            }
        
        
            stage('Stop myapp') {
                steps {
                    step([
                        $class: 'DockerComposeBuilder',
                        dockerComposeFile: 'FinalProject/docker-compose.yml',
                        option: [$class: 'StopAllServices'],
                        useCustomDockerComposeFile: true
                    ])
                }
            }
        }
            

        post {
            always {
                allure([
                    reportBuildPolicy: 'ALWAYS',
                    report: 'target',
                    results: [[path: 'allurdir']]
                ])
            }
        }
    }
