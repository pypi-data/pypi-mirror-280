# -*- coding: utf-8 -*-

"""
todo: doc string
"""

import typing as T
import dataclasses

from acore_constants.api import ServerLifeCycle


@dataclasses.dataclass
class Server:
    """
    Per Game Server configuration.

    :param id: Server id, the naming convention is ``${env_name}-${server_name}``.
    :param ec2_ami_id: the AMI id for the game server.
    :param ec2_instance_type: the EC2 instance type for the game server.
    :param ec2_subnet_id: the EC2 subnet id for the game server.
    :param ec2_key_name: the EC2 ssh key name for the game server.
    :param ec2_eip_allocation_id: if you need a static IP, then create
        an Elastic IP address and put the allocation id here. otherwise,
        use the automatic public IP address.
    :param acore_soap_app_version: the acore_soap_app-project git tag for bootstrap.
    :param acore_server_bootstrap_version: the acore_server_bootstrap-project
        git tag for bootstrap.
    :param db_snapshot_id: the snapshot id to create the RDS DB instance.
    :param db_instance_class: the RDS instance class for the game database.
    :param db_engine_version: the RDS engine version (all the way to minor).
    :param db_admin_username: the RDS admin username, usually this is admin.
    :param db_admin_password: the RDS admin password, we need this password.
        to create the database user for game server.
    :param db_username: the database user for game server.
    :param db_password: the database password for game server.
    :param lifecycle: the logic "game server (both EC2 and RDS)" lifecycle definition.
    :param authserver_conf: custom config for authserver.conf.
    :param worldserver_conf: custom config for worldserver.conf.
    :param mod_lua_engine_conf: custom config for mod_LuaEngine.conf.
    """

    id: T.Optional[str] = dataclasses.field(default=None)
    # EC2 related
    ec2_ami_id: T.Optional[str] = dataclasses.field(default=None)
    ec2_instance_type: T.Optional[str] = dataclasses.field(default=None)
    ec2_subnet_id: T.Optional[str] = dataclasses.field(default=None)
    ec2_key_name: T.Optional[str] = dataclasses.field(default=None)
    ec2_eip_allocation_id: T.Optional[str] = dataclasses.field(default=None)
    acore_soap_app_version: T.Optional[str] = dataclasses.field(default=None)
    acore_db_app_version: T.Optional[str] = dataclasses.field(default=None)
    acore_server_bootstrap_version: T.Optional[str] = dataclasses.field(default=None)
    # RDS related
    db_snapshot_id: T.Optional[str] = dataclasses.field(default=None)
    db_instance_class: T.Optional[str] = dataclasses.field(default=None)
    db_engine_version: T.Optional[str] = dataclasses.field(default=None)
    db_admin_username: T.Optional[str] = dataclasses.field(default=None)
    db_admin_password: T.Optional[str] = dataclasses.field(default=None)
    db_username: T.Optional[str] = dataclasses.field(default=None)
    db_password: T.Optional[str] = dataclasses.field(default=None)
    # EC2 and RDS related
    lifecycle: T.Optional[str] = dataclasses.field(default=None)
    # authserver.conf, worldserver.conf, ...
    authserver_conf: T.Dict[str, str] = dataclasses.field(default_factory=dict)
    worldserver_conf: T.Dict[str, str] = dataclasses.field(default_factory=dict)
    mod_lua_engine_conf: T.Dict[str, str] = dataclasses.field(default_factory=dict)

    def __post_init__(self):
        if self.lifecycle not in [
            ServerLifeCycle.running,
            ServerLifeCycle.smart_running,
            ServerLifeCycle.stopped,
            ServerLifeCycle.deleted,
        ]:  # pragma: no cover
            raise ValueError(f"{self.lifecycle!r} is not a valid lifecycle definition!")

    def is_ready_for_create_new_server(self) -> bool:
        """
        Check if the configuration is sufficient for creating new server.

        See: https://acore-server.readthedocs.io/en/latest/search.html?q=Operation+and+Workflow&check_keywords=yes&area=default#
        """
        not_none_fields = [
            "id",
            "ec2_ami_id",
            "ec2_instance_type",
            "ec2_subnet_id",
            "ec2_key_name",
            "acore_soap_app_version",
            "acore_db_app_version",
            "acore_server_bootstrap_version",
            "db_instance_class",
            "db_engine_version",
            "db_admin_username",
            "db_admin_password",
            "db_username",
            "db_password",
        ]
        for field in not_none_fields:
            if getattr(self, field) is None:
                return False
        return True

    def is_ready_for_create_cloned_server(self) -> bool:
        """
        Check if the configuration is sufficient for creating cloned server.

        See: https://acore-server.readthedocs.io/en/latest/search.html?q=Operation+and+Workflow&check_keywords=yes&area=default#
        """
        not_none_fields = [
            "id",
            "ec2_instance_type",
            "ec2_subnet_id",
            "ec2_key_name",
            "acore_soap_app_version",
            "acore_db_app_version",
            "acore_server_bootstrap_version",
            "db_instance_class",
            # "db_engine_version", # clone 的时候不需要指定 engine version, 会自动继承
            # "db_admin_username", # clone 的时候不需要指定 admin username, 会自动继承
            "db_admin_password",
            "db_username",
            "db_password",
        ]
        for field in not_none_fields:
            if getattr(self, field) is None:
                return False
        return True

    def is_ready_for_create_updated_server(self) -> bool:
        """
        Check if the configuration is sufficient for creating updated server.

        See: https://acore-server.readthedocs.io/en/latest/search.html?q=Operation+and+Workflow&check_keywords=yes&area=default#
        """
        not_none_fields = [
            "id",
            "ec2_ami_id",
            "ec2_instance_type",
            "ec2_subnet_id",
            "ec2_key_name",
            "acore_soap_app_version",
            "acore_db_app_version",
            "acore_server_bootstrap_version",
            "db_instance_class",
            # "db_engine_version", # update server 的时候不需要指定 engine version, 因为我们会用已经存在的数据库
            # "db_admin_username", # update server 的时候不需要指定 admin username, 因为我们会用已经存在的数据库
            "db_admin_password",
            "db_username",
            "db_password",
        ]
        for field in not_none_fields:
            if getattr(self, field) is None:
                return False
        return True

    def is_ready_for_stop_server(self) -> bool:
        """
        Check if the configuration is sufficient for stopping server.

        See: https://acore-server.readthedocs.io/en/latest/search.html?q=Operation+and+Workflow&check_keywords=yes&area=default#
        """
        not_none_fields = [
            "id",
        ]
        for field in not_none_fields:
            if getattr(self, field) is None:
                return False
        return True

    def is_ready_for_start_server(self) -> bool:
        """
        Check if the configuration is sufficient for starting server.

        See: https://acore-server.readthedocs.io/en/latest/search.html?q=Operation+and+Workflow&check_keywords=yes&area=default#
        """
        not_none_fields = [
            "id",
        ]
        for field in not_none_fields:
            if getattr(self, field) is None:
                return False
        return True

    def is_ready_for_delete_server(self) -> bool:
        """
        Check if the configuration is sufficient for deleting server.

        See: https://acore-server.readthedocs.io/en/latest/search.html?q=Operation+and+Workflow&check_keywords=yes&area=default#
        """
        not_none_fields = [
            "id",
        ]
        for field in not_none_fields:
            if getattr(self, field) is None:
                return False
        return True


@dataclasses.dataclass
class ServerMixin:
    servers: T.Dict[str, Server] = dataclasses.field(default_factory=dict)

    @property
    def server_blue(self) -> Server:
        return self.servers["blue"]

    @property
    def server_green(self) -> Server:
        return self.servers["green"]

    @property
    def server_black(self) -> Server:
        return self.servers["black"]

    @property
    def server_white(self) -> Server:
        return self.servers["white"]

    @property
    def server_yellow(self) -> Server:
        return self.servers["yello"]

    @property
    def server_orange(self) -> Server:
        return self.servers["orange"]
