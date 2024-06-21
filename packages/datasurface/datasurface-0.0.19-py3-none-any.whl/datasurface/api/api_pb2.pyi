from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCTION: _ClassVar[ProductionStatus]
    NON_PRODUCTION: _ClassVar[ProductionStatus]

class DeprecationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEPRECATED: _ClassVar[DeprecationStatus]
    NOT_DEPRECATED: _ClassVar[DeprecationStatus]

class IngestionConsistencyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SINGLE_DATASET: _ClassVar[IngestionConsistencyType]
    MULTI_DATASET: _ClassVar[IngestionConsistencyType]

class CloudVendor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AWS: _ClassVar[CloudVendor]
    AZURE: _ClassVar[CloudVendor]
    GCP: _ClassVar[CloudVendor]
    IBM: _ClassVar[CloudVendor]
    ORACLE: _ClassVar[CloudVendor]
    ALIBABA: _ClassVar[CloudVendor]
    AWS_CHINA: _ClassVar[CloudVendor]
    TEN_CENT: _ClassVar[CloudVendor]
    HUAWEI: _ClassVar[CloudVendor]
    AZURE_CHINA: _ClassVar[CloudVendor]

class AzureVaultObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HSM_KEYS: _ClassVar[AzureVaultObjectType]
    SOFTWARE_KEYS: _ClassVar[AzureVaultObjectType]
    SECRETS: _ClassVar[AzureVaultObjectType]
    CERTIFICATES: _ClassVar[AzureVaultObjectType]
    STORAGE_ACTION_KEYS: _ClassVar[AzureVaultObjectType]
PRODUCTION: ProductionStatus
NON_PRODUCTION: ProductionStatus
DEPRECATED: DeprecationStatus
NOT_DEPRECATED: DeprecationStatus
SINGLE_DATASET: IngestionConsistencyType
MULTI_DATASET: IngestionConsistencyType
AWS: CloudVendor
AZURE: CloudVendor
GCP: CloudVendor
IBM: CloudVendor
ORACLE: CloudVendor
ALIBABA: CloudVendor
AWS_CHINA: CloudVendor
TEN_CENT: CloudVendor
HUAWEI: CloudVendor
AZURE_CHINA: CloudVendor
HSM_KEYS: AzureVaultObjectType
SOFTWARE_KEYS: AzureVaultObjectType
SECRETS: AzureVaultObjectType
CERTIFICATES: AzureVaultObjectType
STORAGE_ACTION_KEYS: AzureVaultObjectType

class InfrastructureLocation(_message.Message):
    __slots__ = ("name", "vendorName")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VENDORNAME_FIELD_NUMBER: _ClassVar[int]
    name: _containers.RepeatedScalarFieldContainer[str]
    vendorName: str
    def __init__(self, name: _Optional[_Iterable[str]] = ..., vendorName: _Optional[str] = ...) -> None: ...

class InfrastructureVendor(_message.Message):
    __slots__ = ("name", "hardCloudVendor", "locations")
    class LocationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: InfrastructureLocation
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[InfrastructureLocation, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    HARDCLOUDVENDOR_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    hardCloudVendor: CloudVendor
    locations: _containers.MessageMap[str, InfrastructureLocation]
    def __init__(self, name: _Optional[str] = ..., hardCloudVendor: _Optional[_Union[CloudVendor, str]] = ..., locations: _Optional[_Mapping[str, InfrastructureLocation]] = ...) -> None: ...

class Dataset(_message.Message):
    __slots__ = ("name", "datastoreName", "schema")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATASTORENAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    name: str
    datastoreName: str
    schema: Schema
    def __init__(self, name: _Optional[str] = ..., datastoreName: _Optional[str] = ..., schema: _Optional[_Union[Schema, _Mapping]] = ...) -> None: ...

class Schema(_message.Message):
    __slots__ = ("primaryKeys", "ingestionPartitionKeys", "ddlSchema")
    PRIMARYKEYS_FIELD_NUMBER: _ClassVar[int]
    INGESTIONPARTITIONKEYS_FIELD_NUMBER: _ClassVar[int]
    DDLSCHEMA_FIELD_NUMBER: _ClassVar[int]
    primaryKeys: _containers.RepeatedScalarFieldContainer[str]
    ingestionPartitionKeys: _containers.RepeatedScalarFieldContainer[str]
    ddlSchema: DDLSchema
    def __init__(self, primaryKeys: _Optional[_Iterable[str]] = ..., ingestionPartitionKeys: _Optional[_Iterable[str]] = ..., ddlSchema: _Optional[_Union[DDLSchema, _Mapping]] = ...) -> None: ...

class DDLSchema(_message.Message):
    __slots__ = ("ddl", "columns")
    DDL_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    ddl: str
    columns: _containers.RepeatedCompositeFieldContainer[DDLColumn]
    def __init__(self, ddl: _Optional[str] = ..., columns: _Optional[_Iterable[_Union[DDLColumn, _Mapping]]] = ...) -> None: ...

class DDLColumn(_message.Message):
    __slots__ = ("name", "type", "isNullable")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ISNULLABLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    isNullable: bool
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., isNullable: bool = ...) -> None: ...

class CaptureMetaData(_message.Message):
    __slots__ = ("ingestionConsistencyType", "container")
    INGESTIONCONSISTENCYTYPE_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    ingestionConsistencyType: IngestionConsistencyType
    container: DataContainer
    def __init__(self, ingestionConsistencyType: _Optional[_Union[IngestionConsistencyType, str]] = ..., container: _Optional[_Union[DataContainer, _Mapping]] = ...) -> None: ...

class Datastore(_message.Message):
    __slots__ = ("name", "teamName", "datasets", "captureMetaData")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEAMNAME_FIELD_NUMBER: _ClassVar[int]
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    CAPTUREMETADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    teamName: str
    datasets: _containers.RepeatedCompositeFieldContainer[Dataset]
    captureMetaData: CaptureMetaData
    def __init__(self, name: _Optional[str] = ..., teamName: _Optional[str] = ..., datasets: _Optional[_Iterable[_Union[Dataset, _Mapping]]] = ..., captureMetaData: _Optional[_Union[CaptureMetaData, _Mapping]] = ...) -> None: ...

class Team(_message.Message):
    __slots__ = ("name", "zoneName", "datastores")
    class DatastoresEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Datastore
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Datastore, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ZONENAME_FIELD_NUMBER: _ClassVar[int]
    DATASTORES_FIELD_NUMBER: _ClassVar[int]
    name: str
    zoneName: str
    datastores: _containers.MessageMap[str, Datastore]
    def __init__(self, name: _Optional[str] = ..., zoneName: _Optional[str] = ..., datastores: _Optional[_Mapping[str, Datastore]] = ...) -> None: ...

class GovernanceZone(_message.Message):
    __slots__ = ("name", "ecosystemName", "teams")
    class TeamsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Team
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ECOSYSTEMNAME_FIELD_NUMBER: _ClassVar[int]
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    name: str
    ecosystemName: str
    teams: _containers.MessageMap[str, Team]
    def __init__(self, name: _Optional[str] = ..., ecosystemName: _Optional[str] = ..., teams: _Optional[_Mapping[str, Team]] = ...) -> None: ...

class Ecosystem(_message.Message):
    __slots__ = ("name", "zones")
    class ZonesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: GovernanceZone
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[GovernanceZone, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ZONES_FIELD_NUMBER: _ClassVar[int]
    name: str
    zones: _containers.MessageMap[str, GovernanceZone]
    def __init__(self, name: _Optional[str] = ..., zones: _Optional[_Mapping[str, GovernanceZone]] = ...) -> None: ...

class ObjectStorage(_message.Message):
    __slots__ = ("endPointURI", "bucketName", "prefix")
    ENDPOINTURI_FIELD_NUMBER: _ClassVar[int]
    BUCKETNAME_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    endPointURI: str
    bucketName: str
    prefix: str
    def __init__(self, endPointURI: _Optional[str] = ..., bucketName: _Optional[str] = ..., prefix: _Optional[str] = ...) -> None: ...

class SQLDatabase(_message.Message):
    __slots__ = ("databaseName",)
    DATABASENAME_FIELD_NUMBER: _ClassVar[int]
    databaseName: str
    def __init__(self, databaseName: _Optional[str] = ...) -> None: ...

class AuroraDatabase(_message.Message):
    __slots__ = ("databaseName", "endpointName")
    DATABASENAME_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTNAME_FIELD_NUMBER: _ClassVar[int]
    databaseName: str
    endpointName: str
    def __init__(self, databaseName: _Optional[str] = ..., endpointName: _Optional[str] = ...) -> None: ...

class DataContainer(_message.Message):
    __slots__ = ("name", "locations", "s3Bucket", "auroraDatabase")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    S3BUCKET_FIELD_NUMBER: _ClassVar[int]
    AURORADATABASE_FIELD_NUMBER: _ClassVar[int]
    name: str
    locations: _containers.RepeatedCompositeFieldContainer[InfrastructureLocation]
    s3Bucket: ObjectStorage
    auroraDatabase: AuroraDatabase
    def __init__(self, name: _Optional[str] = ..., locations: _Optional[_Iterable[_Union[InfrastructureLocation, _Mapping]]] = ..., s3Bucket: _Optional[_Union[ObjectStorage, _Mapping]] = ..., auroraDatabase: _Optional[_Union[AuroraDatabase, _Mapping]] = ...) -> None: ...

class Credential(_message.Message):
    __slots__ = ("userPasswordCredential", "awsSecretCredential", "azureKeyVaultCredential")
    USERPASSWORDCREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    AWSSECRETCREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    AZUREKEYVAULTCREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    userPasswordCredential: UserPasswordCredential
    awsSecretCredential: AWSSecretCredential
    azureKeyVaultCredential: AzureKeyVaultCredential
    def __init__(self, userPasswordCredential: _Optional[_Union[UserPasswordCredential, _Mapping]] = ..., awsSecretCredential: _Optional[_Union[AWSSecretCredential, _Mapping]] = ..., azureKeyVaultCredential: _Optional[_Union[AzureKeyVaultCredential, _Mapping]] = ...) -> None: ...

class UserPasswordCredential(_message.Message):
    __slots__ = ("username", "password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AWSSecretCredential(_message.Message):
    __slots__ = ("secretName", "location")
    SECRETNAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    secretName: str
    location: InfrastructureLocation
    def __init__(self, secretName: _Optional[str] = ..., location: _Optional[_Union[InfrastructureLocation, _Mapping]] = ...) -> None: ...

class AzureKeyVaultCredential(_message.Message):
    __slots__ = ("vaultName", "objectType", "objectName")
    VAULTNAME_FIELD_NUMBER: _ClassVar[int]
    OBJECTTYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECTNAME_FIELD_NUMBER: _ClassVar[int]
    vaultName: str
    objectType: AzureVaultObjectType
    objectName: str
    def __init__(self, vaultName: _Optional[str] = ..., objectType: _Optional[_Union[AzureVaultObjectType, str]] = ..., objectName: _Optional[str] = ...) -> None: ...

class DataStoreRequest(_message.Message):
    __slots__ = ("ecoSystemName", "dataStoreName")
    ECOSYSTEMNAME_FIELD_NUMBER: _ClassVar[int]
    DATASTORENAME_FIELD_NUMBER: _ClassVar[int]
    ecoSystemName: str
    dataStoreName: str
    def __init__(self, ecoSystemName: _Optional[str] = ..., dataStoreName: _Optional[str] = ...) -> None: ...
