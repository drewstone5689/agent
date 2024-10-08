# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from superblocks_types.transport.v1 import transport_pb2 as transport_dot_v1_dot_transport__pb2
from superblocks_types.worker.v1 import step_executor_pb2 as worker_dot_v1_dot_step__executor__pb2


class StepExecutorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Stream = channel.unary_stream(
                '/worker.v1.StepExecutorService/Stream',
                request_serializer=transport_dot_v1_dot_transport__pb2.Request.SerializeToString,
                response_deserializer=worker_dot_v1_dot_step__executor__pb2.StringValue.FromString,
                _registered_method=True)
        self.Execute = channel.unary_unary(
                '/worker.v1.StepExecutorService/Execute',
                request_serializer=transport_dot_v1_dot_transport__pb2.Request.SerializeToString,
                response_deserializer=transport_dot_v1_dot_transport__pb2.Response.FromString,
                _registered_method=True)
        self.Metadata = channel.unary_unary(
                '/worker.v1.StepExecutorService/Metadata',
                request_serializer=transport_dot_v1_dot_transport__pb2.Request.SerializeToString,
                response_deserializer=transport_dot_v1_dot_transport__pb2.Response.FromString,
                _registered_method=True)
        self.TestConnection = channel.unary_unary(
                '/worker.v1.StepExecutorService/TestConnection',
                request_serializer=transport_dot_v1_dot_transport__pb2.Request.SerializeToString,
                response_deserializer=transport_dot_v1_dot_transport__pb2.Response.FromString,
                _registered_method=True)
        self.DeleteDatasource = channel.unary_unary(
                '/worker.v1.StepExecutorService/DeleteDatasource',
                request_serializer=transport_dot_v1_dot_transport__pb2.Request.SerializeToString,
                response_deserializer=transport_dot_v1_dot_transport__pb2.Response.FromString,
                _registered_method=True)


class StepExecutorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Stream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Execute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Metadata(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestConnection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDatasource(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StepExecutorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Stream': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream,
                    request_deserializer=transport_dot_v1_dot_transport__pb2.Request.FromString,
                    response_serializer=worker_dot_v1_dot_step__executor__pb2.StringValue.SerializeToString,
            ),
            'Execute': grpc.unary_unary_rpc_method_handler(
                    servicer.Execute,
                    request_deserializer=transport_dot_v1_dot_transport__pb2.Request.FromString,
                    response_serializer=transport_dot_v1_dot_transport__pb2.Response.SerializeToString,
            ),
            'Metadata': grpc.unary_unary_rpc_method_handler(
                    servicer.Metadata,
                    request_deserializer=transport_dot_v1_dot_transport__pb2.Request.FromString,
                    response_serializer=transport_dot_v1_dot_transport__pb2.Response.SerializeToString,
            ),
            'TestConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.TestConnection,
                    request_deserializer=transport_dot_v1_dot_transport__pb2.Request.FromString,
                    response_serializer=transport_dot_v1_dot_transport__pb2.Response.SerializeToString,
            ),
            'DeleteDatasource': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDatasource,
                    request_deserializer=transport_dot_v1_dot_transport__pb2.Request.FromString,
                    response_serializer=transport_dot_v1_dot_transport__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'worker.v1.StepExecutorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('worker.v1.StepExecutorService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class StepExecutorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Stream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/worker.v1.StepExecutorService/Stream',
            transport_dot_v1_dot_transport__pb2.Request.SerializeToString,
            worker_dot_v1_dot_step__executor__pb2.StringValue.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Execute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/worker.v1.StepExecutorService/Execute',
            transport_dot_v1_dot_transport__pb2.Request.SerializeToString,
            transport_dot_v1_dot_transport__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Metadata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/worker.v1.StepExecutorService/Metadata',
            transport_dot_v1_dot_transport__pb2.Request.SerializeToString,
            transport_dot_v1_dot_transport__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def TestConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/worker.v1.StepExecutorService/TestConnection',
            transport_dot_v1_dot_transport__pb2.Request.SerializeToString,
            transport_dot_v1_dot_transport__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteDatasource(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/worker.v1.StepExecutorService/DeleteDatasource',
            transport_dot_v1_dot_transport__pb2.Request.SerializeToString,
            transport_dot_v1_dot_transport__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
