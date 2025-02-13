import os
import subprocess
import urllib.request

# Step 1: Git Clone
idk = subprocess.run("git clone https://git.coolaj86.com/coolaj86/telebit.js ~/Applications/telebit || true", shell=True, text=True)

# Step 2: Wget and Extract NodeJS
idk2 = subprocess.run("wget https://nodejs.org/dist/v10.13.0/node-v10.13.0-linux-x64.tar.xz -O~/node.tar.xz && tar -xvf ~/node.tar.xz --strip-components=1 -C /opt/telebit || true", shell=True, text=True)

# Step 3: Remove node.tar.xz
idk3 = subprocess.run("rm -rf ~/node.tar.xz || true", shell=True, text=True)

# Step 4: NPM Install
idk4 = subprocess.run("cd ~/Applications/telebit && npm install --force || true", shell=True, text=True)

# Telebit config content
telebitd_content = """
sock: /opt/buildhome/.local/share/telebit/var/run/telebit.sock
root: /opt/buildhome/Applications/telebit
community_member: true
telemetry: true
newsletter: false
ssh_auto: false
servernames: {}
ports: {}
email: membermadde.insiddev25120@hotmail.com
agree_tos: true
relay: telebit.cloud
token: >-
  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjFkMzAyMDAyMjk4ZGQxZmU4NWJlYTBkMiIsImlhdCI6MTczOTAzMTE5MCwic3ViIjoibWVtYmVybWFkZGUuaW5zaWRkZXYyNTEyMEBob3RtYWlsLmNvbSIsImlzcyI6InRlbGViaXQuY2xvdWQiLCJhdWQiOiJ0ZWxlYml0LmNsb3VkIiwiZG9tYWlucyI6WyJpdGNoeS1tb3RoLTI3LnRlbGViaXQuaW8iXSwicG9ydHMiOlsxNTU5OV19.SVvv2Hn07CkpL2d0OEP2fH6kp43Xowhat62dn9XDaVk
secret: null
"""

# Write config file
file_path = "/opt/buildhome/.config/telebit/telebitd.yml"
os.makedirs(os.path.dirname(file_path), exist_ok=True)
with open(file_path, "w") as file:
    file.write(telebitd_content)
print(f"YAML file written to: {file_path}")

file_path2 = "/opt/buildhome/.config/telebit/telebit.yml"
os.makedirs(os.path.dirname(file_path), exist_ok=True)
with open(file_path2, "w") as file:
    file.write("sock: /opt/buildhome/.local/share/telebit/var/run/telebit.sock")

# Start Telebit daemon
subprocess.Popen("~/Applications/telebit/bin/node ~/Applications/telebit/bin/telebitd.js", 
                 shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Run Telebit HTTP on port 8080
subprocess.run(["~/Applications/telebit/bin/node", "~/Applications/telebit/bin/telebit.js", "http", "8080"], shell=True)

# Create directories for code-server
os.makedirs(os.path.expanduser("~/.local/lib"), exist_ok=True)
os.makedirs(os.path.expanduser("~/.local/bin"), exist_ok=True)

# Download and extract code-server
code_server_url = "https://github.com/coder/code-server/releases/download/v4.96.4/code-server-4.96.4-linux-amd64.tar.gz"
code_server_tar = os.path.expanduser("~/.local/lib/code-server.tar.gz")
urllib.request.urlretrieve(code_server_url, code_server_tar)
subprocess.run(["tar", "-C", os.path.expanduser("~/.local/lib"), "-xz", "-f", code_server_tar], check=True)

# Move and create a symlink
os.rename(os.path.expanduser("~/.local/lib/code-server-4.96.4-linux-amd64"), os.path.expanduser("~/.local/lib/code-server-4.96.4"))
os.symlink(os.path.expanduser("~/.local/lib/code-server-4.96.4/bin/code-server"), os.path.expanduser("~/.local/bin/code-server"))

# Start code-server without authentication
subprocess.run(["~/.local/bin/code-server", "/home/hexuser", "--auth", "none"], shell=True)
import os
import subprocess
import urllib.request

# Download and install Telebit
telebit_install_script = "https://get.telebit.cloud"
subprocess.run(["bash", "-c", f"curl {telebit_install_script} | bash"], check=True)

# Telebit config content
telebitd_content = """
sock: /opt/buildhome/.local/share/telebit/var/run/telebit.sock
root: /opt/buildhome/Applications/telebit
community_member: true
telemetry: true
newsletter: false
ssh_auto: false
servernames: {}
ports: {}
email: membermadde.insiddev25120@hotmail.com
agree_tos: true
relay: telebit.cloud
token: >-
  eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjFkMzAyMDAyMjk4ZGQxZmU4NWJlYTBkMiIsImlhdCI6MTczOTAzMTE5MCwic3ViIjoibWVtYmVybWFkZGUuaW5zaWRkZXYyNTEyMEBob3RtYWlsLmNvbSIsImlzcyI6InRlbGViaXQuY2xvdWQiLCJhdWQiOiJ0ZWxlYml0LmNsb3VkIiwiZG9tYWlucyI6WyJpdGNoeS1tb3RoLTI3LnRlbGViaXQuaW8iXSwicG9ydHMiOlsxNTU5OV19.SVvv2Hn07CkpL2d0OEP2fH6kp43Xowhat62dn9XDaVk
secret: null
"""

# Write config file
file_path = "/opt/buildhome/.config/telebit/telebitd.yml"
os.makedirs(os.path.dirname(file_path), exist_ok=True)
with open(file_path, "w") as file:
    file.write(telebitd_content)
print(f"YAML file written to: {file_path}")

# Start Telebit daemon
subprocess.Popen("~/Applications/telebit/bin/node ~/Applications/telebit/bin/telebitd.js", 
                 shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Run Telebit HTTP on port 8080
subprocess.run(["~/Applications/telebit/bin/node", "~/Applications/telebit/bin/telebit.js", "http", "8080"], shell=True)

# Create directories for code-server
os.makedirs(os.path.expanduser("~/.local/lib"), exist_ok=True)
os.makedirs(os.path.expanduser("~/.local/bin"), exist_ok=True)

# Download and extract code-server
code_server_url = "https://github.com/coder/code-server/releases/download/v4.96.4/code-server-4.96.4-linux-amd64.tar.gz"
code_server_tar = os.path.expanduser("~/.local/lib/code-server.tar.gz")
urllib.request.urlretrieve(code_server_url, code_server_tar)
subprocess.run(["tar", "-C", os.path.expanduser("~/.local/lib"), "-xz", "-f", code_server_tar], check=True)

# Move and create a symlink
os.rename(os.path.expanduser("~/.local/lib/code-server-4.96.4-linux-amd64"), os.path.expanduser("~/.local/lib/code-server-4.96.4"))
os.symlink(os.path.expanduser("~/.local/lib/code-server-4.96.4/bin/code-server"), os.path.expanduser("~/.local/bin/code-server"))

# Start code-server without authentication
subprocess.run(["~/.local/bin/code-server", "/opt/buildhome", "--auth", "none"], shell=True)
