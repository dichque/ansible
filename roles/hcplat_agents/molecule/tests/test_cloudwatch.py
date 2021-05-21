

def test_is_cloudwatch_installed(host):
    package_cloudwatch = host.package('amazon-cloudwatch-agent')

    assert package_cloudwatch.is_installed


def test_is_cloudwatch_config_file_installed(host):
    cloudwatch_config = host.file('/opt/aws/amazon-cloudwatch-agent/etc/amazon-cloudwatch-agent.json')

    assert cloudwatch_config.exists
    assert cloudwatch_config.user == "root"
    assert cloudwatch_config.group == "root"


# FIXME: Test starting of cloudwatch
# def test_start_cloudwatch_service(host):
#     cloudwatch_service = host.run("FIXME")

#     assert 'Cloudwatch service started' in cloudwatch_service.stdout