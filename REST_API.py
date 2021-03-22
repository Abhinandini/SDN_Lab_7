from flask import Flask, request, url_for, send_from_directory, redirect, render_template, flash
import json
import http.client
import shlex
import subprocess


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title='index.html')

@app.route('/static_routing', methods=['GET', 'POST'])
def static_routing():
    if request.method == 'POST':
        class StaticFlowPusher(object):
            def __init__(self, server):
                self.server = server
            def set(self, data):
                ret = self.rest_call(data, 'POST')
                return ret[0] == 200
            def rest_call(self, data, action):
                path = '/wm/staticflowpusher/json'
                headers = {
                    'Content-type': 'application/json',
                    'Accept': 'application/json',
                }
                body = json.dumps(data)
                conn = http.client.HTTPConnection(self.server, 8080)
                conn.request(action, path, body, headers)
                response = conn.getresponse()
                ret = (response.status, response.reason, response.read())
                print (ret)
                conn.close()
                return ret
        pusher = StaticFlowPusher('192.168.56.109')

        DPID = request.form["DPID"]
        name = request.form["name"]
        priority = request.form["priority"]
        In_port = request.form ["In-port"]
        Eth_Type = request.form ["Eth-Type"]
        Dest_IP = request.form ["Dest IP"]
        Action = request.form ["Action"]
        flow1 = { "switch": DPID, "name" : name, "priority":priority,"cookie":"0","In-port":In_port, "Eth-Type":Eth_Type,"active":"true","Action":Action}
        print (flow1)
        pusher.set(flow1)

        return redirect(url_for('index'))
    return render_template('static_routing.html')

@app.route('/firewall_form', methods=['GET', 'POST'])
def firewall_form():
    if request.method == 'POST':
        r= '''curl http://localhost:8080/wm/firewall/module/enable/json -X PUT -d '' '''
        args = shlex.split(r)
        process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        class StaticFlowPusher(object):
            def __init__(self, server):
                self.server = server
            def set(self, data):
                ret = self.rest_call(data, 'POST')
                return ret[0] == 200
            def rest_call(self, data, action):
                path = '/wm/staticflowpusher/json'
                headers = {
                    'Content-type': 'application/json',
                    'Accept': 'application/json',
                }
                body = json.dumps(data)
                conn = http.client.HTTPConnection(self.server, 8080)
                conn.request(action, path, body, headers)
                response = conn.getresponse()
                ret = (response.status, response.reason, response.read())
                print (ret)
                conn.close()
                return ret
        pusher = StaticFlowPusher('192.168.56.109')
        DPID = request.form["DPID"]
        priority = request.form["priority"]
        In_port = request.form ["In-port"]
        Eth_Type = request.form ["Eth-Type"]
        src_ip = request.form ["Src IP"]
        dst_ip = request.form ["Dest IP"]
        l4 = request.form ["L4-Protocol"]
        flow1 = { "switch": DPID,"priority":priority,"In-port":In_port, "Eth-Type":Eth_Type,"src-ip":src_ip, "dst-ip":dst_ip, "l4_protocol":l4}
        print (flow1)
        pusher.set(flow1)

        return redirect(url_for('index'))
    return render_template('firewall_form.html')



if __name__ == "__main__":
    app.run(threaded=True)
