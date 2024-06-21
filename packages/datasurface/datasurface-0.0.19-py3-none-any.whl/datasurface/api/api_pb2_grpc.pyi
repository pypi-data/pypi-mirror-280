from _typeshed import Incomplete

class ProducerServiceStub:
    getDatastore: Incomplete
    def __init__(self, channel) -> None: ...

class ProducerServiceServicer:
    def getDatastore(self, request, context) -> None: ...

def add_ProducerServiceServicer_to_server(servicer, server) -> None: ...

class ProducerService:
    @staticmethod
    def getDatastore(request, target, options=(), channel_credentials: Incomplete | None = None, call_credentials: Incomplete | None = None, insecure: bool = False, compression: Incomplete | None = None, wait_for_ready: Incomplete | None = None, timeout: Incomplete | None = None, metadata: Incomplete | None = None): ...
