from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from chalk._gen.chalk.utils.v1 import encoding_pb2 as _encoding_pb2

DESCRIPTOR: _descriptor.FileDescriptor
PERMISSION_AUTHENTICATED: Permission
PERMISSION_CHALK_ADMIN: Permission
PERMISSION_CRON_CREATE: Permission
PERMISSION_CRON_READ: Permission
PERMISSION_DEPLOY_CREATE: Permission
PERMISSION_DEPLOY_PREVIEW: Permission
PERMISSION_DEPLOY_READ: Permission
PERMISSION_DEPLOY_REDEPLOY: Permission
PERMISSION_FIELD_NUMBER: _ClassVar[int]
PERMISSION_INSECURE_UNAUTHENTICATED: Permission
PERMISSION_LOGS_LIST: Permission
PERMISSION_MIGRATE_EXECUTE: Permission
PERMISSION_MIGRATE_PLAN: Permission
PERMISSION_MIGRATE_READ: Permission
PERMISSION_MONITORING_CREATE: Permission
PERMISSION_MONITORING_READ: Permission
PERMISSION_PROJECT_CREATE: Permission
PERMISSION_QUERY_OFFLINE: Permission
PERMISSION_QUERY_ONLINE: Permission
PERMISSION_SECRETS_DECRYPT: Permission
PERMISSION_SECRETS_LIST: Permission
PERMISSION_SECRETS_WRITE: Permission
PERMISSION_TEAM_ADD: Permission
PERMISSION_TEAM_ADMIN: Permission
PERMISSION_TEAM_DELETE: Permission
PERMISSION_TEAM_LIST: Permission
PERMISSION_TOKENS_LIST: Permission
PERMISSION_TOKENS_WRITE: Permission
PERMISSION_UNSPECIFIED: Permission
permission: _descriptor.FieldDescriptor

class Permission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
