#!/usr/bin/env python3
import docker

# client = docker.Docker("tcp://127.0.0.1:2376") Conexão remota
client = docker.from_env() # conexão local
# print(client.containers.run('python','python3 --help'))
todos_os_containers = client.containers.list()
container = client.containers.get('jenkins_aula')
print(container.short_id)
print(container.name)
print(container.image.tags[0])
print(container.status)

