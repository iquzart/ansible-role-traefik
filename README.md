Traefik Reverse Proxy
=========

[![Ansible Galaxy](https://img.shields.io/badge/galaxy-iquzart.traefik-blue)](https://galaxy.ansible.com/iquzart/traefik)
![Molecule Test](https://github.com/iquzart/ansible-role-traefik/workflows/Molecule%20Test/badge.svg?) 
[![License](https://img.shields.io/:license-mit-blue.svg)](https://badges.mit-license.org)


Ansible Role for Traefik Reverse Proxy on Container

Features
---------
```
    1. Basic Authentication
    2. HTTPS Redirection
    3. IP Whitelist
    4. Letsencrypt
    5. TLS 1.2 and 1.3
    6. Access logs to file
```


Role Variables
--------------

| Variable Name| Description | Default |
|---|---|---|
| traefik_version  | Traefik Container Version | v2.2.1 |
| traefik_install_dir  | container confi directory  | /opt/containers/traefik |
| traefik_domain_name  | traefik UI Domain Name  | example.com |
| traefik_log_level  | Traefik Log level  | WARN  |
| traefik_check_new_version | Check new version | false | 
| traefik_send_anonymous_usage | Send anonymous usage | false |
| traefik_api_dashboard | Enable or Disable Traefik UI | true |
| traefik_auth | Basic Auth credentials. htaccess password with MD5/SHA1/Bcrypt  | **** |
| traefik_ip_white_list | IP source to allow access | 127.0.0.1/32 |


Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: iquzart.traefik }

License
-------

MIT

Author Information
------------------

Muhammed Iqbal <iquzart@hotmail.com>

