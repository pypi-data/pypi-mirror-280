# coding=utf8
# Copyright 2020 Cognicept Systems
# Author: Jakub Tomasek (jakub@cognicept.systems)
# --> Configuration class handles Cognicept configuration

from dotenv import dotenv_values
from pathlib import Path
from Crypto.PublicKey import RSA
import subprocess
import os
import boto3
import re
import jwt
import requests
import getpass
import errno
import shutil
import yaml
import json

from cogniceptshell.common import bcolors


class Configuration:
    """
    A class to manage agent and Cognicept's configuration
    ...

    Parameters
    ----------
    None

    Methods
    -------    
    load_config(path):
        Loads and parses `runtime.env` file into `object.config` located at `path`.
    configure(args):
        Manages cognicept configuration based on values in `args`.
    save_config():
        Saves configuration into `runtime.env` file.
    get_cognicept_credentials():
        Checks and returns `COGNICEPT_ACCESS_KEY` from configuration.
    get_cognicept_api_uri():
        Checks and returns `COGNICEPT_API_URI` from configuration.
    get_cognicept_user_api_uri():
        Checks and returns `COGNICEPT_USER_APT_URI` from configuration.
    get_field():
        Returns single config value
    configure_ssh():
        Function to setup ssh access for the host machine given user input.
    is_ssh_enabled(args):
        Checks and returns value of `COG_ENABLE_SSH_KEY_AUTH` as bool.
    is_audio_enabled(args):
        Checks and returns value of `COG_ENABLE_AUDIO` as bool
    cognicept_key_rotate:
        Rotates AWS temporary keys retriving them from Cognicept API.
    init_config(args):
        Initiates runtime.env file with values from Cognicept API
    """
    config_path = os.path.expanduser("~/.cognicept/")
    env_path = config_path + "runtime.env"
    _regex_key = r"^([_A-Z0-9]+)$"
    _config_loaded = False

    def load_config(object, path):
        """
        Loads and parses `runtime.env` file into `object.config` located at `path`.

                Parameters:
                        path (str): Cognicept path, e.g. `~/.cognicept/`.                
        """
        object.config_path = os.path.expanduser(path)
        object.env_path = object.config_path + "runtime.env"
        file = Path(object.env_path)

        if ((not file.exists()) or (file.is_dir())):
            print("Configuration file `" + object.env_path + "` does not exist.")
            try:
                with open(object.env_path, 'w') as f:
                    pass
            except:
                print("Failed to initialize the robot: insufficient priviledges to create `/home/username/.cognicept/runtime.env file.")
                return False

        #object.config = dotenv_values(dotenv_path=file.name) if sys.version_info.minor > 5 else dotenv_values(dotenv_path=find_dotenv(), verbose=True)
        object.config = dotenv_values(
            dotenv_path=object.env_path, verbose=True)
        if(len(object.config) == 0):
            print("Configuration file `" + object.env_path +
                  "` is empty or could not be parsed.")
            return False
        object._config_loaded = True
        return True

    def get_docker_compose(object):
        if "COG_COMPOSE_FILE" in object.config:
            compose_file = os.path.expanduser(object.config["COG_COMPOSE_FILE"])
            compose_images = {}
            try:
                with open(compose_file, 'r') as stream:
                    docker_compose=yaml.safe_load(stream)
                    for container_name in docker_compose['services']:
                        compose_images[container_name] = docker_compose['services'][container_name]['image'] 
                return compose_images
            except (yaml.YAMLError,FileNotFoundError, IOError, TypeError):
                return {}
        else:
            return {}

    def configure(object, args):
        """
        Manages cognicept configuration based on values in `args`:
            * If `args.read` is True, then it prints all configuration,
            * If `args.add` is True, then it will add or modify a single value inputed by user,
            * Otherwise it will iterate through all values and asks for modifications.

                Parameters:
                        args: populated argument namespace returned by `argparse.parse_args()`            
        """
        if(args.ssh):
            if object.configure_ssh():
                print(
                    'SSH config done. To apply changes restart agents using `cognicept restart`.')
        elif(args.autocomplete):
            if object.configure_autocomplete():
                print('Autocomplete setup done')
        else:
            if(not object._config_loaded):
                return

            if (not os.access(object.env_path, os.W_OK)):
                print("Error: You don't have writing permissions for `" +
                    object.env_path + "`. Run as `sudo` or change file permissions.")
                return
            if(args.read):
                for key, value in object.config.items():
                    print(key + ': "' + value + '"')
            elif(args.add):
                new_key = ""
                while(new_key == ""):
                    new_key = input("Config name: ")

                    # if empty, exit
                    if(new_key == ""):
                        return
                    # check if matches key specs
                    matches = re.match(object._regex_key, new_key)
                    if matches is None:
                        print(
                            "Error: Key can be uppercase letters, digits, and the '_'. Try again.")
                        new_key = ""

                new_value = ""
                while(new_value == ""):
                    new_value = input("Value: ")
                    if(new_value == ""):
                        return
                    matches = re.match(r"^.*[\"].*$", new_value)
                    if matches is not None:
                        print("Error: Value cannot contain '\"'. Try again.")
                        new_value = ""

                object.config[new_key] = new_value        
            else:
                for key, value in object.config.items():
                    new_value = input(key + "[" + value + "]:")
                    matches = re.match(r"^.*[\"].*$", new_value)
                    if((new_value != "") and (matches == None)):
                        object.config[key] = new_value
            object.save_config()

    def save_config(object):
        """
        Saves configuration into `runtime.env` file

                Parameters:
                    None
        """
        # Try backing up configuration before saving
        backup_success = False
        try:
            shutil.copyfile(object.env_path, object.env_path+'.bk')
            backup_success = True
            print(bcolors.OKBLUE + "Backed up runtime configuration to: " + \
                object.env_path + ".bk" + bcolors.ENDC)
        except OSError as ex:
            if ex.errno == errno.ENOSPC:
                # Catch out of space exceptions
                print(bcolors.FAIL + "Could not back up runtime configuration." + \
                    " Aborting saving runtime configuration." + \
                    " No space left on device!" + bcolors.ENDC)
            else:
                # Raise all other exceptions
                print(bcolors.FAIL + "Could not back up runtime configuration." + \
                    " Aborting saving runtime configuration: " + ex.strerror + bcolors.ENDC)
        
        # If backup is success, try to save it
        if backup_success:
            try:
                with open(object.env_path, 'w') as file:
                    for key, value in object.config.items():
                        file.write(key + '=' + ("" if value is None else value) + '\n')
            except OSError:
                print(bcolors.FAIL + "Could not write into `" + object.env_path +
                    "`. Please check write permission or run with `sudo`." + bcolors.ENDC)        

    def get_cognicept_credentials(object):
        """
        Checks and returns `COGNICEPT_ACCESS_KEY` from configuration.

                Returns:
                    cognicept_access_key (str): value of `COGNICEPT_ACCESS_KEY`
        """
        if "COGNICEPT_ACCESS_KEY" in object.config:
            return object.config["COGNICEPT_ACCESS_KEY"]
        else:
            print('COGNICEPT_ACCESS_KEY missing')

    def get_cognicept_api_uri(object):
        """
        Checks and returns `COGNICEPT_API_URI` from configuration.

                Returns:
                    cognicept_api_uri (str): value of `COGNICEPT_API_URI`, defaults to "https://app.cognicept.systems/api/v1/"
        """
        if "COGNICEPT_API_URI" in object.config:
            return object.config["COGNICEPT_API_URI"]
        else:
            return "https://app.cognicept.systems/api/v1/"

    def get_cognicept_user_api_uri(object):
        """
        Checks and returns `COGNICEPT_USER_API_URI` from configuration.

                Returns:
                    cognicept_user_api_uri (str): value of `COGNICEPT_USER_API_URI`, defaults to "https://app.cognicept.systems/api/v1/"
        """
        if "COGNICEPT_USER_API_URI" in object.config:
            return object.config["COGNICEPT_USER_API_URI"] 
        else:
            return "https://app.cognicept.systems/api/v1/"

    def get_field(object, field_name):
        """
        Returns single config value

                Parameters:
                        field_name (str): name of config field
                Returns:
                        value (str): value
        """
        if field_name in object.config:
            return object.config[field_name]
        else:
            raise KeyError(field_name)

    def _interpret_bool_input(object, input_string):
        """
        Parses user input string bool value 

                Parameters:
                        input_string (str): input value
                Returns:
                        bool_value (bool): True if value is 'Y'
        """
        if(input_string == 'Y'):
            return True
        elif(input_string == 'n'):
            return False
        else:
            return None

    def configure_ssh(object):
        """
        Function to setup ssh access for the host machine given user input

                Parameters:
                        None
                Returns:
                        result (bool): True if some step didn't fail
        """
        print('SSH is used to access the host machine from the isolated docker environment of Cognicept agent.')

        enable_ssh = None
        while(enable_ssh == None):
            enable_ssh = object._interpret_bool_input(
                input("Enable SSH access? (Y/n):"))

        if(not enable_ssh):
            object.config["COG_ENABLE_SSH"] = "False"
            object.config["COG_ENABLE_SSH_KEY_AUTH"] = "False"
            object.config["COG_ENABLE_AUTOMATIC_SSH"] = "False"
            object.save_config()
            return True
        else:
            object.config["COG_ENABLE_SSH"] = "True"

        ssh_authorized_keys_path = os.path.expanduser(
            "~") + "/.ssh/authorized_keys"
        print("\n \nSSH key needs to be used for hosts with disabled password login. "
              "It can also simplify access so you don't need to input the password each time.\n"
              "This process will generate ssh key locally and mount it to the docker container. "
              "The public key is copied to `" + ssh_authorized_keys_path +
              "` to give access.  Root access is needed and you will be prompted for password."
              "The ssh key is neither sent nor stored to the Cognicept server. "
              "If you choose not to, manual password ssh access can be still used.")

        enable_ssh_key = None
        while(enable_ssh_key == None):
            enable_ssh_key = object._interpret_bool_input(
                input("Generate SSH key and give access? (Y/n):"))

        if(not enable_ssh_key):
            object.config["COG_ENABLE_SSH_KEY_AUTH"] = "False"
        else:
            object.config["COG_ENABLE_SSH_KEY_AUTH"] = "True"

        # generate the ssh key and write them in the file
        if object.config["COG_ENABLE_SSH_KEY_AUTH"] == "True":
            cognicet_ssh_directory = object.config_path + "ssh/"
            try:
                if not os.path.exists(cognicet_ssh_directory):
                    os.makedirs(cognicet_ssh_directory)
            except:
                print(
                    "Failed. Don't have privileges to create files/directories within the ssh directory.")
                return False

            # generate the keys
            ssh_key = RSA.generate(2048)
            private_key_path = cognicet_ssh_directory + "id_rsa"
            public_key_path = cognicet_ssh_directory + "id_rsa.pub"
            config_file_path = cognicet_ssh_directory + "config"
            with open(private_key_path, 'wb') as content_file:
                os.chmod(private_key_path, 0o600)
                content_file.write(ssh_key.exportKey('PEM'))
            pub_key = ssh_key.publickey().exportKey('OpenSSH')
            with open(public_key_path, 'wb') as content_file:
                content_file.write(pub_key)
            # add new line at the end of the file
            with open(public_key_path, 'a') as content_file:
                content_file.write("\n")

        default_user = getpass.getuser()
        user_exists = False
        ssh_directory_path = ""

        # retrieve the user name
        user_prompt_number = 0
        while not user_exists:
            user_name = input(
                "Name of the user to access ssh(if empty, defaults to `" + default_user + "`): ")
            if(user_name == ""):
                user_name = default_user
            object.config["COG_SSH_DEFAULT_USER"] = user_name
            
            if(user_name == "root"):
                ssh_directory_path = "/root/.ssh/"
            else:                
                ssh_directory_path = "/home/" + user_name + "/.ssh/"
            if os.path.exists(ssh_directory_path):
                user_exists = True
            else:
                print("User " + user_name +
                      " doesn't seem to exist or openssh server is not installed.")
                user_prompt_number = user_prompt_number + 1
                if(user_prompt_number > 2):
                    print("Failed to find user's openssh configuration directory.")
                    return False

        # copy the keys to authorized_keys file if automatic authentication was enabled
        if object.config["COG_ENABLE_SSH_KEY_AUTH"] == "True":
            authorized_keys_path = ssh_directory_path + "authorized_keys"
            try:
                print('Root access is needed to modify `' +
                      authorized_keys_path + '` and you will be prompted for password.')
                proc = subprocess.call(
                    ['sudo', 'sh', '-c', 'cat ' + public_key_path + ' >> ' + authorized_keys_path])
            except:
                print("Failed! Don't have access to " + authorized_keys_path)
                return

        enable_automatic_ssh = None
        while(enable_automatic_ssh == None):
            enable_automatic_ssh = object._interpret_bool_input(
                input("Enable automatic ssh access? (Y/n):"))

        if(not enable_automatic_ssh):
            object.config["COG_ENABLE_AUTOMATIC_SSH"] = "False"
        else:
            object.config["COG_ENABLE_AUTOMATIC_SSH"] = "True"

        object.save_config()
        return True

    def is_ssh_enabled(object):
        """
        Checks and returns value of `COG_ENABLE_SSH_KEY_AUTH` as bool

                Parameters:
                        None
                Returns:
                        ssh_enabled (bool): True if ssh is enabled
        """
        if(not "COG_ENABLE_SSH_KEY_AUTH" in object.config):
            return False

        return object.config["COG_ENABLE_SSH_KEY_AUTH"]

    def is_audio_enabled(object):
        """
        Checks and returns value of `COG_ENABLE_AUDIO` as bool

                Parameters:
                        None
                Returns:
                        sound enabled (bool): True if sound is enabled
        """
        if(not "COG_ENABLE_AUDIO" in object.config):
            return False

        return object.config["COG_ENABLE_AUDIO"]
    

    def fetch_aws_keys(object):
        """
        Fetch AWS temporary keys retriving them from Cognicept API.

                Parameters:
                        
                Returns:
                        result (json): AWS temporary credentials returned from Cognicept API
        """
        try:
            headers = {
                'Authorization': 'Basic ' + object.get_cognicept_credentials()
            }
            resp = requests.get(object.get_cognicept_api_uri(
            ) + 'aws/assume_role', headers=headers, timeout=5)
            if resp.status_code != 200:
                print('Login error: wrong credentials.')
                return False
            return resp.json()            
        except requests.exceptions.Timeout:
            print("Cognicept REST API error: time out.")
            return False
        except requests.exceptions.TooManyRedirects:
            print("Cognicept REST API error: Wrong endpoint.")
            return False
        except Exception as e:
            print("Cognicept REST API error" + str(e))
            return False
        object.save_config()

        return True

    def cognicept_key_rotate(object, args):
        """
        Rotates AWS temporary keys retriving them from Cognicept API.

                Parameters:
                        args: populated argument namespace returned by `argparse.parse_args()`
                Returns:
                        result (bool): True if succeeded
        """
        print("Updating cloud credentials.")
        try:
            response = object.fetch_aws_keys()
            if response==False:
                print("Error connecting Cognicept API. Please contact support@cognicept.systems")
                return False
            object.config["AWS_ACCESS_KEY_ID"] = response[
                "AccessKeyId"]
            object.config["AWS_SECRET_ACCESS_KEY"] = response[
                "SecretAccessKey"]
            object.config["AWS_SESSION_TOKEN"] = response[
                "SessionToken"]
            object.config["AWS_TOKEN_EXPIRATION"] = response[
                "Expiration"]
            print(bcolors.OKGREEN+"Cloud access keys rotated successfully!"+bcolors.ENDC)
        except requests.exceptions.Timeout:
            print("Cognicept REST API error: time out.")
            return False
        except requests.exceptions.TooManyRedirects:
            print("Cognicept REST API error: Wrong endpoint.")
            return False
        except Exception as e:
            print("Cognicept REST API error" + str(e))
            raise SystemExit()
        object.save_config()

        return True

    def pull_config_templates(object, args):
        """
        Pulls robot config templates from S3 bucket and stores them into the templates folder

                Parameters:
                        args: populated argument namespace returned by `argparse.parse_args()`
                Returns:
                        None
        """
        runtime_var = args.config.config
        robot_model = runtime_var['ECS_ROBOT_MODEL'].lower()
        
        bucket_name = 'robot-config-templates'
        templates_folder = os.path.expanduser(args.path + 'templates')

        try:
            s3 = boto3.client('s3')
            response = s3.list_objects_v2(Bucket=bucket_name,Prefix=robot_model)
            templates = response.get('Contents')
            
            for template in templates:
                template_key = template['Key']
                template_filename = os.path.basename(template_key)
                
                if template_filename.endswith(('.yaml', '.yml')):
                    destination_path = os.path.join(templates_folder, template_filename)
                    s3.download_file(bucket_name,template_key,destination_path)

            print(bcolors.OKGREEN+'All robot configuration templates have been successfully downloaded.'+bcolors.ENDC)

        except Exception:
            print(bcolors.WARNING +"Warning: Failed to retrieve template config files" + bcolors.ENDC)
            return False

    def check_user_api_version(object, api_uri):
        if 'v1' in api_uri:
            print("WARNING: COGNICEPT_USER_API is 'v1'. Initializing robot with robot_code and org_code will fail!")
            init_endpoint = "spinup/config/"
        else:
            init_endpoint = "robot_config/config/"
        return init_endpoint
    
    def switch_org(object, api_uri, org_id, headers):
        switch_org_uri = api_uri + "user/switch_org"
        switch_org_payload = {
             'organization_id': org_id,
             "blacklist": True
        }   
        switch_org_resp = requests.post(switch_org_uri, json=switch_org_payload, headers=headers, timeout=5)
        if switch_org_resp.status_code != 200:
            print(bcolors.FAIL + "Error in switching organization" + bcolors.ENDC)
            raise SystemExit(1)
        new_access_token = json.loads(switch_org_resp.content.decode())['access_token']
        return new_access_token

    def get_robot_id(object, api_uri, auth_key, robot_code, org_id):
        """
        Retrieves robot_id from Cognicept API to be resused in various functions across shell

                Parameters:
                        auth_key: Cognicept User API authentication key after login
                        robot_code: TBC
                        org_id: organization id of specified robot
                Returns:
                        robot_id(string): robot_id of specified robot
        """
        try:
            r = requests.get(api_uri + 'robot/organization_code', params={'organization_code': org_id, 'robot_code': robot_code}, headers={'Authorization': 'Bearer {}'.format(auth_key)})
            j = r.json()
            if 'robot_id' in j:
                robot_id = j['robot_id']
                return robot_id
            else:
                print("The robot_code input does not match a robot")
                return None
            
        except Exception as e:
            print("Cognicept API Error: " + str(e))
            return None
        
    def get_organization_id(object, api_uri, auth_key, org_code):
        """
        Retrieves robot_id from Cognicept API to be resused in various functions across shell

                Parameters:
                        auth_key: Cognicept User API authentication key after login
                        org_code: unique organization code
                Returns:
                        org_id(string): organization id of specified robot
        """
        try:
            get_organization_uri = api_uri + 'organization/?filter={{"organization_code": "{org_code}"}}'.format(org_code=org_code)
            r = requests.get(get_organization_uri, headers={'Authorization': 'Bearer {}'.format(auth_key)})
            j = r.json()
            if 'data' in j and isinstance(j['data'], list) and len(j['data']) > 0:
                org_id = j['data'][0]['organization_id']
                return org_id
            else:
                print("The org_code input does not match any organization")
                return None

        except Exception as e:
            print("Cognicept API Error: " + str(e))
            return None           
    
    def init_config(object, args):
        """
        Initiates runtime.env file with values from Cognicept API.

                Parameters:
                        args: populated argument namespace returned by `argparse.parse_args()`
                Returns:
                        result (bool): True if succeeded
        """
        username = input('Username: ')
        password = getpass.getpass('Password: ')
        api_uri = object.get_cognicept_user_api_uri()

        try:
            x = requests.post(api_uri + 'user/login', json={'username': username, 'password': password})
            if 'access_token' not in x.json():
                print('Failed to initialize the robot: Wrong credentials') 
            else:
                auth_key = x.json()["access_token"]
                # check whether whether user activate the 2FA
                decode_json = jwt.decode(auth_key, verify=False, algorithms=["HS256"])

                # False means 2FA Verification is activated by the user
                if decode_json['user_claims']['authorized'] == False:
                    new_key = object.mfa_verfication(api_uri,auth_key)
                    if new_key == auth_key:    
                        print("Failed to initialized robot: Invalid OTP entered 3 times")
                        return False
                    else:
                        auth_key=new_key
                
                #Check version of user api
                init_endpoint = object.check_user_api_version(api_uri)

                # Check if org code is available and get org id
                if not args.org_id:
                    org_id = object.get_organization_id(api_uri, auth_key, args.org_code)
                    if not org_id:
                        print("Failed to initialize the robot: Invalid org_code")
                        return False
                else:
                    org_id = args.org_id

                #Switch user ogranization based on org_id
                header={'Authorization': 'Bearer {}'.format(auth_key)}
                access_token = object.switch_org(api_uri, org_id, header)

                # Check if robot code is available and get robot id
                if not args.robot_id:
                    robot_id = object.get_robot_id(api_uri, access_token, args.robot_code, org_id)
                    if not robot_id:
                        print("Failed to initialize the robot: Invalid robot_code")
                        return False
                else:
                    robot_id = args.robot_id
                
                r = requests.get(api_uri + init_endpoint + org_id + '/' + robot_id, headers={'Authorization': 'Bearer {}'.format(access_token)})
                r.raise_for_status()
                j = r.json()
                if j:
                    for key in j:
                        object.config[key] = j[key]
                    object.update_robot_config()
                    object.save_config()
                    object.pull_config_templates(args)
                    print(bcolors.OKGREEN + "Successfully initialized configuration for the robot `" + robot_id + "`. To start agents run `cognicept start`"+ bcolors.ENDC)
                    return True
                else:
                    print("Failed to initialize the robot: ID `" + robot_id + "` in organization `" + org_id + "` not found")
                    return False
                
        except requests.exceptions.Timeout:
            print("Cognicept REST API error: time out.")
            return False
        except requests.exceptions.TooManyRedirects:
            print("Cognicept REST API error: Wrong endpoint.")
            return False
        except requests.exceptions.HTTPError as err:
            error_code = err.response.status_code
            if error_code != 400:
                print(f"Cognicept REST API error: {error_code} status code.\nPlease check configurations and report error if necessary.")
                raise SystemExit()
            else:
                print("Failed to initialize the robot: ID `" + robot_id + "` in organization `" + org_id + "` not found")
                return False
        except Exception as e:
            print("Cognicept REST API error" + str(e))
            raise SystemExit()

    def mfa_verfication(object,api_uri,auth_key):
        otp_trial = 3
        loop = True
        while loop:
            if otp_trial == 0:
                key = auth_key
                loop = False
            else:
                otp = getpass.getpass('OTP from Authenticator: ')
                x = requests.post(api_uri + 'user/mfa/verify', headers={'Authorization': 'Bearer {}'.format(auth_key)}, json={'otp': otp})
                if 'access_token' not in x.json():
                    print('Invalid OTP! Please try again...')
                else:
                    key = x.json()["access_token"]
                    loop = False
            otp_trial -= 1
        return key
             
    def configure_autocomplete(object):
        """

        Function to setup autcomplate functionality
                Parameters:
                        None
                Returns:
                        result (bool): True if some step didn't fail

        """

        enable_autocomplete = None
        while(enable_autocomplete == None):
            enable_autocomplete = object._interpret_bool_input(
                input("Enable Autocomplete? (Y/n):"))
        
        if (not enable_autocomplete):
            print("Autocomplete was not configured")
            return True

        bash_complete_path = "/etc/bash_completion.d/"
        tmp_path = os.path.expanduser("~") + "/.cognicept/"
        
        print("Root access is needed to place bash completition script at `" + bash_complete_path +
              "' you will be prompted for password.")

        allow_root_access = None
        while(allow_root_access == None):
            allow_root_access = object._interpret_bool_input(
            input("Generate script and give access? (Y/n):"))
        subprocess.call(['bash', '-c', 'activate-global-python-argcomplete --dest ' + tmp_path])
        subprocess.call(['sudo', 'bash', '-c', 'mv ' + tmp_path + "python-argcomplete" + " /etc/bash_completion.d/"])
        print("Please restart the terminal.....")
        return True

    def get_robot_config(object):
        """
            Pulls the robot config including properties data from /robot-config endpoint of COGNICEPT_API_URI

                    Parameters:
                            None
                    Returns:
                            The robot configuration as a dict
        """
        config_endpoint = "robot-config/"
        agent_api = object.get_cognicept_api_uri()
        config_api = f"{agent_api}{config_endpoint}"
        access_key = object.get_cognicept_credentials()
        print(f"Getting latest config from {config_api}")
        try:
            config_response = requests.get(config_api, headers={"Authorization": f"Basic {access_key}"})

            if config_response.status_code == 200:
                response_json = config_response.json()
                if response_json and response_json.get("PROPERTIES", None):
                    properties = response_json.get("PROPERTIES")
                    response_json.pop("PROPERTIES")
                    for item in properties:
                        response_json[item] = properties[item]["value"]
                return response_json
            else:
                print(bcolors.FAIL + f"No robot config found: {config_response.status_code}" + bcolors.ENDC)
                return {}
            
        except Exception as ex:
            print(bcolors.FAIL + f"Error getting config from cloud, {ex}" + bcolors.ENDC)
            return {}

    def update_robot_config(object):
        """
            Updates the configuration based on information pulled via `get_robot_config` method

                    Parameters:
                            None
                    Returns:
                            Bool : True if update success, False otherwise
        """
        config = object.get_robot_config()
        if config:
            for key in config:
                print(f"Updating {key}")
                object.config[key] = config[key]
            return True
        else:
            print(bcolors.WARNING + "No config recieved from agent API, will not update runtime.env" + bcolors.ENDC)
            return False