from typing import ClassVar as _ClassVar
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

CLOUD_PROVIDER_KIND_AWS: CloudProviderKind
CLOUD_PROVIDER_KIND_GCP: CloudProviderKind
CLOUD_PROVIDER_KIND_UNKNOWN: CloudProviderKind
CLOUD_PROVIDER_KIND_UNSPECIFIED: CloudProviderKind
DESCRIPTOR: _descriptor.FileDescriptor

class AWSCloudConfig(_message.Message):
    __slots__ = [
        "account_id",
        "cloud_watch_config",
        "external_id",
        "management_role_arn",
        "region",
        "secret_manager_config",
    ]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_WATCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    MANAGEMENT_ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    SECRET_MANAGER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    cloud_watch_config: AWSCloudWatchConfig
    external_id: str
    management_role_arn: str
    region: str
    secret_manager_config: AWSSecretManagerConfig
    def __init__(
        self,
        account_id: _Optional[str] = ...,
        management_role_arn: _Optional[str] = ...,
        region: _Optional[str] = ...,
        external_id: _Optional[str] = ...,
        cloud_watch_config: _Optional[_Union[AWSCloudWatchConfig, _Mapping]] = ...,
        secret_manager_config: _Optional[_Union[AWSSecretManagerConfig, _Mapping]] = ...,
    ) -> None: ...

class AWSCloudWatchConfig(_message.Message):
    __slots__ = ["log_group_path"]
    LOG_GROUP_PATH_FIELD_NUMBER: _ClassVar[int]
    log_group_path: str
    def __init__(self, log_group_path: _Optional[str] = ...) -> None: ...

class AWSSecretManagerConfig(_message.Message):
    __slots__ = ["secret_kms_arn", "secret_prefix", "secret_tags"]
    class SecretTagsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

    SECRET_KMS_ARN_FIELD_NUMBER: _ClassVar[int]
    SECRET_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SECRET_TAGS_FIELD_NUMBER: _ClassVar[int]
    secret_kms_arn: str
    secret_prefix: str
    secret_tags: _containers.ScalarMap[str, str]
    def __init__(
        self,
        secret_kms_arn: _Optional[str] = ...,
        secret_tags: _Optional[_Mapping[str, str]] = ...,
        secret_prefix: _Optional[str] = ...,
    ) -> None: ...

class CloudConfig(_message.Message):
    __slots__ = ["aws", "gcp"]
    AWS_FIELD_NUMBER: _ClassVar[int]
    GCP_FIELD_NUMBER: _ClassVar[int]
    aws: AWSCloudConfig
    gcp: GCPCloudConfig
    def __init__(
        self,
        aws: _Optional[_Union[AWSCloudConfig, _Mapping]] = ...,
        gcp: _Optional[_Union[GCPCloudConfig, _Mapping]] = ...,
    ) -> None: ...

class Environment(_message.Message):
    __slots__ = [
        "active_deployment_id",
        "additional_cron_env_vars",
        "additional_env_vars",
        "bigtable_instance_name",
        "bigtable_table_name",
        "branch_kube_cluster_name",
        "branch_url",
        "cloud_account_locator",
        "cloud_config",
        "cloud_provider",
        "cloud_region",
        "cloud_tenancy_id",
        "default_planner",
        "emq_uri",
        "engine_docker_registry_path",
        "engine_kube_cluster_name",
        "feature_store_secret",
        "id",
        "is_sandbox",
        "kube_cluster_name",
        "kube_job_namespace",
        "kube_preview_namespace",
        "kube_service_account_name",
        "metrics_bus_topic",
        "name",
        "offline_store_secret",
        "online_persistence_mode",
        "online_store_kind",
        "online_store_secret",
        "postgres_secret",
        "private_pip_repositories",
        "project_id",
        "result_bus_topic",
        "service_url",
        "shadow_engine_kube_cluster_name",
        "skip_offline_writes_for_online_cached_features",
        "source_bundle_bucket",
        "spec_config_json",
        "streaming_query_service_uri",
        "team_id",
        "vpc_connector_name",
        "worker_url",
    ]
    class AdditionalCronEnvVarsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

    class AdditionalEnvVarsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

    class SpecConfigJsonEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(
            self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...
        ) -> None: ...

    ACTIVE_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_CRON_ENV_VARS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_ENV_VARS_FIELD_NUMBER: _ClassVar[int]
    BIGTABLE_INSTANCE_NAME_FIELD_NUMBER: _ClassVar[int]
    BIGTABLE_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    BRANCH_KUBE_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    BRANCH_URL_FIELD_NUMBER: _ClassVar[int]
    CLOUD_ACCOUNT_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CLOUD_REGION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_TENANCY_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PLANNER_FIELD_NUMBER: _ClassVar[int]
    EMQ_URI_FIELD_NUMBER: _ClassVar[int]
    ENGINE_DOCKER_REGISTRY_PATH_FIELD_NUMBER: _ClassVar[int]
    ENGINE_KUBE_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    FEATURE_STORE_SECRET_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_SANDBOX_FIELD_NUMBER: _ClassVar[int]
    KUBE_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    KUBE_JOB_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    KUBE_PREVIEW_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    KUBE_SERVICE_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    METRICS_BUS_TOPIC_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_STORE_SECRET_FIELD_NUMBER: _ClassVar[int]
    ONLINE_PERSISTENCE_MODE_FIELD_NUMBER: _ClassVar[int]
    ONLINE_STORE_KIND_FIELD_NUMBER: _ClassVar[int]
    ONLINE_STORE_SECRET_FIELD_NUMBER: _ClassVar[int]
    POSTGRES_SECRET_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_PIP_REPOSITORIES_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_BUS_TOPIC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_URL_FIELD_NUMBER: _ClassVar[int]
    SHADOW_ENGINE_KUBE_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    SKIP_OFFLINE_WRITES_FOR_ONLINE_CACHED_FEATURES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_BUNDLE_BUCKET_FIELD_NUMBER: _ClassVar[int]
    SPEC_CONFIG_JSON_FIELD_NUMBER: _ClassVar[int]
    STREAMING_QUERY_SERVICE_URI_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    VPC_CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    WORKER_URL_FIELD_NUMBER: _ClassVar[int]
    active_deployment_id: str
    additional_cron_env_vars: _containers.ScalarMap[str, str]
    additional_env_vars: _containers.ScalarMap[str, str]
    bigtable_instance_name: str
    bigtable_table_name: str
    branch_kube_cluster_name: str
    branch_url: str
    cloud_account_locator: str
    cloud_config: CloudConfig
    cloud_provider: CloudProviderKind
    cloud_region: str
    cloud_tenancy_id: str
    default_planner: str
    emq_uri: str
    engine_docker_registry_path: str
    engine_kube_cluster_name: str
    feature_store_secret: str
    id: str
    is_sandbox: bool
    kube_cluster_name: str
    kube_job_namespace: str
    kube_preview_namespace: str
    kube_service_account_name: str
    metrics_bus_topic: str
    name: str
    offline_store_secret: str
    online_persistence_mode: str
    online_store_kind: str
    online_store_secret: str
    postgres_secret: str
    private_pip_repositories: str
    project_id: str
    result_bus_topic: str
    service_url: str
    shadow_engine_kube_cluster_name: str
    skip_offline_writes_for_online_cached_features: bool
    source_bundle_bucket: str
    spec_config_json: _containers.MessageMap[str, _struct_pb2.Value]
    streaming_query_service_uri: str
    team_id: str
    vpc_connector_name: str
    worker_url: str
    def __init__(
        self,
        name: _Optional[str] = ...,
        project_id: _Optional[str] = ...,
        id: _Optional[str] = ...,
        team_id: _Optional[str] = ...,
        active_deployment_id: _Optional[str] = ...,
        worker_url: _Optional[str] = ...,
        service_url: _Optional[str] = ...,
        branch_url: _Optional[str] = ...,
        offline_store_secret: _Optional[str] = ...,
        online_store_secret: _Optional[str] = ...,
        feature_store_secret: _Optional[str] = ...,
        postgres_secret: _Optional[str] = ...,
        online_store_kind: _Optional[str] = ...,
        emq_uri: _Optional[str] = ...,
        vpc_connector_name: _Optional[str] = ...,
        kube_cluster_name: _Optional[str] = ...,
        branch_kube_cluster_name: _Optional[str] = ...,
        engine_kube_cluster_name: _Optional[str] = ...,
        shadow_engine_kube_cluster_name: _Optional[str] = ...,
        kube_job_namespace: _Optional[str] = ...,
        kube_preview_namespace: _Optional[str] = ...,
        kube_service_account_name: _Optional[str] = ...,
        streaming_query_service_uri: _Optional[str] = ...,
        skip_offline_writes_for_online_cached_features: bool = ...,
        result_bus_topic: _Optional[str] = ...,
        online_persistence_mode: _Optional[str] = ...,
        metrics_bus_topic: _Optional[str] = ...,
        bigtable_instance_name: _Optional[str] = ...,
        bigtable_table_name: _Optional[str] = ...,
        cloud_account_locator: _Optional[str] = ...,
        cloud_region: _Optional[str] = ...,
        cloud_tenancy_id: _Optional[str] = ...,
        source_bundle_bucket: _Optional[str] = ...,
        engine_docker_registry_path: _Optional[str] = ...,
        default_planner: _Optional[str] = ...,
        additional_env_vars: _Optional[_Mapping[str, str]] = ...,
        additional_cron_env_vars: _Optional[_Mapping[str, str]] = ...,
        private_pip_repositories: _Optional[str] = ...,
        is_sandbox: bool = ...,
        cloud_provider: _Optional[_Union[CloudProviderKind, str]] = ...,
        cloud_config: _Optional[_Union[CloudConfig, _Mapping]] = ...,
        spec_config_json: _Optional[_Mapping[str, _struct_pb2.Value]] = ...,
    ) -> None: ...

class GCPCloudConfig(_message.Message):
    __slots__ = ["management_service_account", "project_id", "region"]
    MANAGEMENT_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    management_service_account: str
    project_id: str
    region: str
    def __init__(
        self,
        project_id: _Optional[str] = ...,
        region: _Optional[str] = ...,
        management_service_account: _Optional[str] = ...,
    ) -> None: ...

class CloudProviderKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
