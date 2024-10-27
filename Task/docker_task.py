import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/launch", methods=['GET', 'POST'])
def docker_launch():
    if request.method == "GET":
        cont_name = request.args.get('name')
        os_name = request.args.get('os_name')
        cmd = f"docker run -it --name {cont_name} {os_name}"
        cid = subprocess.getoutput(cmd)
        return f"{cont_name} docker launched successfully with id: {cid}"
    else:
        return "Something went wrong"

@app.route("/stop", methods=['GET', 'POST'])
def docker_stop():
    if request.method == "GET":
        cont_name = request.args.get('name')
        cmd = f"docker stop {cont_name}"
        c_name = subprocess.getoutput(cmd)
        return f"docker stopped successfully named: {c_name}"
    else:
        return "Something went wrong"
        

@app.route("/terminate", methods=['GET', 'POST'])
def docker_terminate():
    if request.method == "GET":
        cont_name = request.args.get('name')
        cmd = f"docker rm {cont_name}"
        c_name = subprocess.getoutput(cmd)
        return f"docker stopped successfully named: {c_name}"
    else:
        return "Something went wrong"

@app.route("/list")
def docker_list():
    cmd = "docker ps -a"
    list = subprocess.getoutput(cmd)
    return f"docker running containers: {list}"
    
    


if __name__ == "__main__":
    app.run()

