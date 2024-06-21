# -*- coding: utf-8 -*-

from acore_server_metadata import api


def test():
    _ = api

    # top level API
    _ = api.exc
    _ = api.get_boto_ses_from_ec2_inside
    _ = api.settings
    _ = api.Server

    # attribute and method
    _ = api.exc.ServerNotFoundError
    _ = api.exc.ServerNotUniqueError

    _ = api.Server.get_ec2
    _ = api.Server.get_rds
    _ = api.Server.from_ec2_inside
    _ = api.Server.get_server
    _ = api.Server.batch_get_server
    _ = api.Server.is_exists
    _ = api.Server.is_running
    _ = api.Server.is_ec2_exists
    _ = api.Server.is_ec2_running
    _ = api.Server.is_rds_exists
    _ = api.Server.is_rds_running
    _ = api.Server.refresh


if __name__ == "__main__":
    from acore_server_metadata.tests import run_cov_test

    run_cov_test(__file__, "acore_server_metadata.api", preview=False)
