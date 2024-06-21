from _typeshed import Incomplete
from datasurface.api.api_pb2 import DataStoreRequest as DataStoreRequest
from datasurface.api.api_pb2_grpc import ProducerServiceServicer as ProducerServiceServicer, add_ProducerServiceServicer_to_server as add_ProducerServiceServicer_to_server
from datasurface.handler.action import GitHubCICD as GitHubCICD
from datasurface.handler.cicd import RepositorywithCICD as RepositorywithCICD
from datasurface.md import DDLTable as DDLTable, NullableStatus as NullableStatus, Schema as Schema
from datasurface.md.Governance import Datastore as Datastore, DatastoreCacheEntry as DatastoreCacheEntry, Ecosystem as Ecosystem
from threading import Thread

class ProducerServiceImpl(ProducerServiceServicer):
    eco: Incomplete
    def __init__(self, eco: Ecosystem) -> None: ...
    def getDatastore(self, request, context): ...

class DataSurfaceServer(Thread):
    port: Incomplete
    maxWorkers: Incomplete
    eco: Incomplete
    stop_server_event: Incomplete
    serverStarted_event: Incomplete
    server: Incomplete
    def __init__(self, eco: Ecosystem, port: int = 50051, maxWorkers: int = 10) -> None: ...
    def waitUntilStopped(self) -> None: ...
    def serveAPIs(self) -> None: ...
    def run(self) -> None: ...
    def waitForServerToStart(self) -> None: ...
    def signalServerToStop(self) -> None: ...
