#coding:utf-8
from conf import SSL_KEY_PEM , SAAS_PORT, SAAS_HOST


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


def server(saas, handler):
    processor = saas.Processor(handler)

#    from thrift.transport.TSSLSocket import TSSLServerSocket as  TServerSocket
#    transport = TServerSocket(SAAS_HOST, port=SAAS_PORT, certfile=SSL_KEY_PEM)
    
    from thrift.transport import TSocket 
    transport = TSocket.TServerSocket(SAAS_HOST, port=SAAS_PORT)

    tfactory  = TTransport.TBufferedTransportFactory()
    pfactory  = TBinaryProtocol.TBinaryProtocolFactory()

    server    = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    # server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
    # server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)
    server.serve()