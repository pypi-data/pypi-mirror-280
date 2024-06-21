# -*- coding: utf-8 -*-

from acore_server_config import api


def test():
    _ = api

    _ = api.IS_LOCAL
    _ = api.IS_GITHUB_CI
    _ = api.IS_EC2
    _ = api.IS_CODEBUILD_CI
    _ = api.EnvEnum
    _ = api.Env
    _ = api.Config
    _ = api.Server
    _ = api.get_server
    _ = api.Ec2ConfigLoader
    _ = api.ConfigLoader
    _ = api.bsm

    _ = api.Server.is_ready_for_create_new_server
    _ = api.Server.is_ready_for_create_cloned_server
    _ = api.Server.is_ready_for_create_updated_server
    _ = api.Server.is_ready_for_stop_server
    _ = api.Server.is_ready_for_start_server
    _ = api.Server.is_ready_for_delete_server

    _ = api.Env.server_blue
    _ = api.Env.server_green
    _ = api.Env.server_black
    _ = api.Env.server_white
    _ = api.Env.server_yellow
    _ = api.Env.server_orange


if __name__ == "__main__":
    from acore_server_config.tests import run_cov_test

    run_cov_test(__file__, "acore_server_config.api", preview=False)
