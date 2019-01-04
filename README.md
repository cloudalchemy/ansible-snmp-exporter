<p><img src="https://www.circonus.com/wp-content/uploads/2015/03/sol-icon-itOps.png" alt="graph logo" title="graph" align="right" height="60" /></p>

# Ansible Role: SNMP exporter

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-snmp-exporter.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-snmp-exporter)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.snmp_exporter-blue.svg)](https://galaxy.ansible.com/cloudalchemy/snmp-exporter/)
[![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-snmp-exporter.svg)](https://github.com/cloudalchemy/ansible-snmp-exporter/tags)
[![IRC](https://img.shields.io/badge/irc.freenode.net-%23cloudalchemy-yellow.svg)](https://kiwiirc.com/nextclient/#ircs://irc.freenode.net/#cloudalchemy)

## Description

Deploy and manage prometheus [SNMP exporter](https://github.com/prometheus/snmp_exporter) using ansible.

## Requirements

- Ansible >= 2.5 (It might work on previous versions, but we cannot guarantee it)
- go-lang installed on deployer machine (same one where ansible is installed)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `snmp_exporter_version` | 0.14.0 | SNMP exporter package version |
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

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v2.x). You will have to install Docker on your system. See "Get started" for a Docker package suitable to for your system.
We are using tox to simplify process of testing on multiple ansible versions. To install tox execute:
```sh
pip install tox
```
To run tests on all ansible versions (WARNING: this can take some time)
```sh
tox
```
To run a custom molecule command on custom environment with only default test scenario:
```sh
tox -e py27-ansible25 -- molecule test -s default
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

If you would like to run tests on remote docker host just specify `DOCKER_HOST` variable before running tox tests.

## Travis CI

Combining molecule and travis CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix (42 parallel role executions in case of [ansible-prometheus](https://github.com/cloudalchemy/ansible-prometheus)) which will take more time than local testing, so please be patient.

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
