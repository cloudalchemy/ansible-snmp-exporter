<p><img src="https://www.circonus.com/wp-content/uploads/2015/03/sol-icon-itOps.png" alt="graph logo" title="graph" align="right" height="60" /></p>

# Ansible Role: SNMP exporter

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-snmp-exporter.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-snmp-exporter)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.snmp_exporter-blue.svg)](https://galaxy.ansible.com/cloudalchemy/snmp-exporter/)
[![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-snmp-exporter.svg)](https://github.com/cloudalchemy/ansible-snmp-exporter/tags)

## Description

Deploy and manage prometheus [SNMP exporter](https://github.com/prometheus/snmp_exporter) using ansible.

## Requirements

- Ansible >= 2.7 (It might work on previous versions, but we cannot guarantee it)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `snmp_exporter_version` | 0.19.0 | SNMP exporter package version |
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

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/ansible-community/molecule) (v3.x). You will have to install Docker on your system. See "Get started" for a Docker package suitable to for your system. Running your tests is as simple as executing `molecule test`.

## Continuous Intergation

Combining molecule and circle CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix which can take more time than local testing, so please be patient.

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## Troubleshooting

See [troubleshooting](TROUBLESHOOTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
