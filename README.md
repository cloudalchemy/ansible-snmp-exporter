<p><img src="https://www.circonus.com/wp-content/uploads/2015/03/sol-icon-itOps.png" alt="graph logo" title="graph" align="right" height="60" /></p>

Ansible Role: SNMP Exporter
===========================

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-snmp-exporter.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-snmp-exporter) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.snmp_exporter-blue.svg)](https://galaxy.ansible.com/cloudalchemy/snmp-exporter/) [![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-snmp-exporter.svg)](https://github.com/cloudalchemy/ansible-snmp-exporter/tags)

Prometheus SNMP Exporter

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: yes
  roles:
    - cloudalchemy.snmp-exporter
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
