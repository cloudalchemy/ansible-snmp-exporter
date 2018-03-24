<p><img src="https://www.circonus.com/wp-content/uploads/2015/03/sol-icon-itOps.png" alt="graph logo" title="graph" align="right" height="60" /></p>

# Ansible Role: SNMP exporter

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-snmp-exporter.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-snmp-exporter)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.snmp_exporter-blue.svg)](https://galaxy.ansible.com/cloudalchemy/snmp-exporter/)
[![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-snmp-exporter.svg)](https://github.com/cloudalchemy/ansible-snmp-exporter/tags)
[![IRC](https://img.shields.io/badge/chat-on%20freenode-blue.svg)](http://webchat.freenode.net/?channels=cloudalchemy)

## Description

Deploy and manage prometheus [SNMP exporter](https://github.com/prometheus/snmp_exporter) using ansible.

## Requirements

- Ansible >= 2.3
- go-lang installed on deployer machine (same one where ansible is installed)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `snmp_exporter_version` | 0.8.0 | SNMP exporter package version |
| `snmp_exporter_web_listen_address` | "0.0.0.0:9116" | Address on which SNMP exporter will be listening |
| `snmp_exporter_config_file` | "" | If this is empty, role will download snmp.yml file from https://github.com/prometheus/snmp_exporter. Otherwise this should contain path to file with custom snmp exporter configuration |

## Example

### Playbook

```yaml
- hosts: all
  become: yes
  roles:
    - cloudalchemy.snmp-exporter
```

### Demo site

We provide demo site for full monitoring solution based on prometheus and grafana. Repository with code and links to running instances is [available on github](https://github.com/cloudalchemy/demo-site) and site is hosted on [DigitalOcean](https://digitalocean.com).

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v1.25). You will have to install Docker on your system. See Get started for a Docker package suitable to for your system.
All packages you need to can be specified in one line:
```sh
pip install ansible ansible-lint>=3.4.15 molecule==1.25.0 docker testinfra>=1.7.0
```
This should be similiar to one listed in `.travis.yml` file in `install` section. 
After installing test suit you can run test by running
```sh
molecule test
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/stable-1.25/).

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
