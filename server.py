from http.server import BaseHTTPRequestHandler
import socketserver as SocketServer

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pathList=self.path.strip()
        extension=pathList.split(".")[-1]
        if pathList=="/":
            message=open("index.html","r").read()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(message.encode('utf-8'))
        elif extension in ["html","css","js"]:
            message=open(pathList[1:],"r").read()
            self.send_response(200)
            self.send_header('Content-Type', 'text/'+extension+'; charset=utf-8')
            self.end_headers()
            self.wfile.write(message.encode('utf-8'))
        elif extension in ["jpeg","gif"]:
            message=open(pathList[1:],"rb").read()
            self.send_response(200)
            self.send_header('Content-Type', 'image/'+extension)
            self.end_headers()
            self.wfile.write(message)
        
        #api calls
        elif pathList[:4]=="/api":
            if not self.path.strip()[1:] in allowedApis:
                self.send_response(404)
                return            
            message=open(pathList[1:],"r").read()
            self.send_response(200)
            self.send_header('Content-Type', 'text/raw; charset=utf-8')
            self.end_headers()
            self.wfile.write(message.encode('utf-8'))            
        
    def do_POST(self):
        if not self.path.strip()[1:] in allowedApis:
            self.send_response(404)
            return
        payloadSize=int(self.headers['Content-Length'])
        payload=self.rfile.read(payloadSize)
        modifiable=open(self.path.strip()[1:],"a")
        modifiable.writelines(str(payload)[2:-1]+"\n")
        self.send_response(201)
    
allowedApis=["api/messages.txt"]    
httpd = SocketServer.TCPServer(("", int(666)), GetHandler)
httpd.serve_forever()