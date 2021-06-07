"""Role testing files using testinfra."""


def test_docker_is_installed(host):
    docker_package = host.package("docker-ce")
    assert docker_package.is_installed

def test_docker_running_and_enabled(host):
    docker_service = host.service("docker")
    assert docker_service.is_running
    assert docker_service.is_enabled
    
def test_traefik_container_running(host):
    traefik = host.docker("traefik")
    assert traefik.is_running