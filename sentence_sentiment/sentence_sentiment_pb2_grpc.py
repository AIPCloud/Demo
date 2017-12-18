# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import sentence_sentiment_pb2 as sentence__sentiment__pb2


class SentenceSentimentStub(object):
  """Prime factors service definition.
  We have a method called `PrimeFactors` which takes
  parameter called `Request` and returns the message `Response`
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Analyze = channel.unary_unary(
        '/sentence_sentiment.SentenceSentiment/Analyze',
        request_serializer=sentence__sentiment__pb2.Request.SerializeToString,
        response_deserializer=sentence__sentiment__pb2.Response.FromString,
        )


class SentenceSentimentServicer(object):
  """Prime factors service definition.
  We have a method called `PrimeFactors` which takes
  parameter called `Request` and returns the message `Response`
  """

  def Analyze(self, request, context):
    """The stream keyword is specified before both the request type and response
    type to make it as bidirectional streaming RPC method.

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SentenceSentimentServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Analyze': grpc.unary_unary_rpc_method_handler(
          servicer.Analyze,
          request_deserializer=sentence__sentiment__pb2.Request.FromString,
          response_serializer=sentence__sentiment__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'sentence_sentiment.SentenceSentiment', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
