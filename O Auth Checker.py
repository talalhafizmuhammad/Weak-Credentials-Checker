import paramiko
import telnetlib

def SSHLogin(host, port, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=username, password=password, timeout=5)
        ssh_session = ssh.get_transport().open_session()
        if ssh_session.active:
            print(f"SSH login successful on {host}:{port} with username {username} and password {password}")
        ssh.close()
    except Exception as e:
        print(f"SSH login failed for {username}:{password} -> {e}")

def TelnetLogin(host, port, username, password):
    user = (username + "\n").encode('utf-8')
    passwd = (password + "\n").encode('utf-8')
    
    try:
        tn = telnetlib.Telnet(host, port, timeout=5)
        
        response = tn.read_until(b"login: ", timeout=5)
        print(f"Response before login prompt: {response.decode()}")
        
        tn.write(user)
        
        response = tn.read_until(b"Password: ", timeout=5)
        print(f"Response before password prompt: {response.decode()}")
        
        tn.write(passwd)
        
        idx, match, text = tn.expect([b"Last login", b"login:", b"$", b"#"], timeout=5)
        
        if idx >= 0:
            print(f"Telnet login successful on {host}:{port} with username {username} and password {password}")
        else:
            print(f"Telnet login failed for {username}:{password}")
    except EOFError:
        print(f"Telnet connection closed unexpectedly for {username}:{password}")
    except Exception as e:
        print(f"Telnet error for {username}:{password} -> {e}")
    finally:
        try:
            tn.close()
        except:
            pass

host = "127.0.0.1"
with open("defaults.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            username, password = line.split(":", 1)
        else:
            vals = line.split()
            if len(vals) < 2:
                print(f"Invalid line in defaults.txt: {line}")
                continue
            username, password = vals[0], vals[1]
        username = username.strip()
        password = password.strip()
        SSHLogin(host, 22, username, password)
        TelnetLogin(host, 23, username, password)
