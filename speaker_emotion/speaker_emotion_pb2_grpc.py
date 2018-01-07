# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import speaker_emotion_pb2 as speaker__emotion__pb2


class SpeakerEmotionStub(object):
  """Speaker Emotion service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Analyze = channel.stream_unary(
        '/speaker_emotion.SpeakerEmotion/Analyze',
        request_serializer=speaker__emotion__pb2.Request.SerializeToString,
        response_deserializer=speaker__emotion__pb2.Response.FromString,
        )


class SpeakerEmotionServicer(object):
  """Speaker Emotion service definition.
  """

  def Analyze(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SpeakerEmotionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Analyze': grpc.stream_unary_rpc_method_handler(
          servicer.Analyze,
          request_deserializer=speaker__emotion__pb2.Request.FromString,
          response_serializer=speaker__emotion__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'speaker_emotion.SpeakerEmotion', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
