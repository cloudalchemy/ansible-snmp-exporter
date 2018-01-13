from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_files(host):
    files = [
        "/etc/systemd/system/snmp_exporter.service",
        "/opt/snmp_exporter/snmp_exporter",
        "/opt/snmp_exporter/snmp.yml"
    ]
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_service(host):
    s = host.service("snmp_exporter")
    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    s = host.socket("tcp://127.0.0.1:9116")
    assert s.is_listening
