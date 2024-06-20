import argparse, yaml, os, subprocess
from time import sleep

def main():
    version = "1.0.0"
    # Create an arg parser to get cli args
    parser=argparse.ArgumentParser(prog='ffs-docker-compose',
                        description='A version of docker-compose that maps docker-compose file parameters to actual docker '
                                    'arguments. A subset of docker-compose parameters are supported. When running in detached '
                                    'mode, the containers are automatically started on boot via systemd.',
                        epilog='Because ffs docker-compose, why don\'t you behave like docker?!')
    parser.add_argument("compose_file", help="docker-compose.yml file. Only a subset of docker-compose params are actually read from the file. ", type=str, nargs="?", default=os.getcwd()+"/docker-compose.yml")
    parser.add_argument("command", help="start containers | stop & remove containers | pull latest image ", type=str, choices=["up", "down", "pull"])
    parser.add_argument("-d", "--detached", help="Run containers in a detached state. Containers are automatically started on boot by systemd.", action="store_true")

    args = parser.parse_args()
    processes = []

    if not args.compose_file.__contains__("/"):
        args.compose_file=os.getcwd()+"/"+args.compose_file

    try:
        with open(args.compose_file, "r") as f_cfg:
            compose_params = yaml.load(f_cfg, Loader=yaml.SafeLoader)
    except FileNotFoundError as e:
        print("Invalid path to docker-compose.yml: {}".format(args.compose_file))
        exit(1)

    if not compose_params['version'].__contains__('ffs'):
        print(f"No ffs version in {args.compose_file}. Make sure you acknowledge the limitations of this program, then add "
              f"\"ffs-\" to the version tag in your .yml file. ex. version: 'ffs-1.0'")
        exit(1)

    compose_params = compose_params["services"]
    run_commands = []
    keep_alive = []

    # Run this script at startup when run in detached mode. If a container exits for some reason, restart everything!
    # Register with system.d to make this happen.
    def register_startup():
        filename = f"/etc/systemd/system/ffsdockercompose.service"
        service_file = \
    f"""[Unit]
    Description=ffs-docker-compose
    After=network.target
    StartLimitIntervalSec=0
    [Service]
    Type=simple
    Restart=always
    RestartSec=1
    User={os.environ["USER"]}
    ExecStart=/usr/bin/python3 {os.path.dirname(os.path.realpath(__file__))}/ffs-docker-compose.py {args.compose_file} up
    [Install]
    WantedBy=multi-user.target"""
        for i in range(len(compose_params)):
            name = list(compose_params)[i]
            m_dict = compose_params[name]
            container_name = m_dict['container_name']
            print(f"Starting container {container_name} in the background")
        os.system(f"echo \"{service_file}\" | sudo tee -a {filename} > /dev/null 2>&1")
        os.system(f"sudo systemctl enable ffsdockercompose.service  > /dev/null 2>&1")
        os.system(f"sudo systemctl start ffsdockercompose.service  > /dev/null 2>&1")
        print_color("done")
        exit(0)

    def unregister_startup():
        try:
            filename = f"/etc/systemd/system/ffsdockercompose.service"

            os.system(f"sudo systemctl stop ffsdockercompose.service > /dev/null 2>&1")
            os.system(f"sudo systemctl disable ffsdockercompose.service > /dev/null 2>&1")
            os.system(f"sudo rm {filename} > /dev/null 2>&1")
        except Exception as e:
            print(e)

    def color_string(string):
        output = ""
        colors = ["\033[91m{}\033[00m", "\033[92m{}\033[00m", "\033[96m{}\033[00m", "\033[94m{}\033[00m"]
        for i in range(len(string)):
            output += colors[i % len(colors)].format(string[i])
        return output
    def print_color(string):

        print(color_string(string))

    print(color_string("~~~~") + f" ffs-docker-compose || " + color_string(f"v{version} ") + color_string("~~~~"))

    if args.detached:
        detached="-d"
        if args.command == "up":
            register_startup()
    else:
        detached=""

    if compose_params == None:
        print("No services in compose file")
        exit(1)
    for i in range(len(compose_params)):
        name = list(compose_params)[i]
        m_dict = compose_params[name]
        container_name = m_dict['container_name']
        image = m_dict['image']
        try:
            command = m_dict['command']
        except KeyError:
            try:
                command = m_dict['entrypoint']
            except KeyError:
                command = ""
        try:
            restart = m_dict['restart']
            if restart == "always":
                keep_alive.append(True)
            else:
                keep_alive.append(False)
        except KeyError:
            keep_alive.append(False)
        if args.command == "pull":
            docker_command = f"""docker pull {image}"""

        elif args.command == "up":
            print(f"Starting container {container_name}")
            docker_command = f"""docker run --rm --name {container_name} -h {container_name} --add-host {container_name}:127.0.0.1 --network host {detached} \\
                         {image} {'/bin/bash -c ' + command if command != '' else ''} """

        elif args.command == "down":
            docker_command = f"""docker kill {container_name} > /dev/null 2>&1"""
            print(f"Stopping & removing container {container_name}")

        else:
            print(f"Unknown command {args.command}")
            exit(1)
        run_commands.append(docker_command)
        processes.append(subprocess.Popen([docker_command], shell=True))

    if args.command == "down":
        unregister_startup()
    else:
        print("Waiting for processes to exit, press CTRL-c to kill...")

    try:
        while True:
            num_finished=0
            for i in range(len(processes)):
                if processes[i].poll() != None:
                    if keep_alive[i] and args.command == "up":
                        name = list(compose_params)[i]
                        m_dict = compose_params[name]
                        container_name = m_dict['container_name']
                        print(f"Restarting container {container_name}...")
                        processes[i] = subprocess.Popen([run_commands[i]], shell=True)
                    else:
                        num_finished+=1

            if num_finished == len(processes):
                break
            sleep(0.5)
    except KeyboardInterrupt:
        print(f"Caught ctrl-c, killing containers...")
        for p in processes:
            p.terminate()
        for i in range(len(compose_params)):
            name = list(compose_params)[i]
            os.system(f"docker kill {name}")

    print_color("done")
