# Executing the NCA Execution process

## Python Environment
While it's not required, we suggest setting up a virtual environment with your favorite tool.

Example.  From the project root issue the following command (in mac, linux or windows shell subsystem)
```shell
python -m venv .venv
source ./.venv/bin/activate
```

Install the required packages 
```shell
# (from the project root)
pip install -r ./docs/samples/python/aplos_nca/requirements.txt

# or if you are in the aplos_nca directory
pip install -r ./requirements.txt
```


## Required Environment Vars

The following environment variables are required for execution.  We're using environment vars so that nothing gets accidentally saved into git.

If executing the functions via the command line, you need to create the environment variables so that they are available at runtime, like the following.

Mac & Linux
```shell
export APLOS_API_URL="<api-gateway-url>"
export COGNITO_CLIENT_ID="<client-id>"
export COGNITO_USER_NAME="<email-address>"
export COGNITO_PASSWORD="<password>"
export COGNITO_REGION="<region>"
```
Windows
```shell
SET APLOS_API_URL="<api-gateway-url>"
SET COGNITO_CLIENT_ID="<client-id>"
SET COGNITO_USER_NAME="<email-address>"
SET COGNITO_PASSWORD="<password>"
SET COGNITO_REGION="<region>"
```
If you are using the debugger, you can create a `.env` file locally and enter the environment vars there.

```shell
APLOS_API_URL="<api-gateway-url>"
COGNITO_CLIENT_ID="<client-id>"
COGNITO_USER_NAME="<email-address>"
COGNITO_PASSWORD="<password>"
COGNITO_REGION="<region>"
```



## Required Files for execution (analysis submission)
To submit something for an analysis, you will need 2 required files and one optional file.  
- Input File (analysis file)
- Configuration File (configurations on how to run the analysis)
- Meta Data (optional)

Technically only the analysis file is submitted as a file.  

The other two (configuration and metadata) are submitted as JSON/dictionary objects.  However to make things easier for this demo they are stored as files, then read in at runtime and submitted in their normal dictionary form.

The files are located `./files` directory of this project.


## Outputs
Currently, we are outputting the files in a hidden directory (`.output`) which is also excluded from the git commits.  This can easily be overridden to your choosing.

Located in `./.output`


## Run and Execution
Assuming you've set the correct environment variables, you can run the main.py file as w/o any parameters and it will run the default execution.

From the project you you can 
`python .<project-path>/main.py`

or navigate to the folder
`python ./main.py`

## Arguments

|short|long|description|
|---|---|---|
|-s|--skip|Skip prompts if required values have defaults|
|-u|--username|Your login username|
|-p|--password|Your login password|
|-f|--analyis-file|Path to the analysis file|
|-c|--config-file|Path to the configuration file|
|-m|--metadata-file|Path to the metadata file|
|-a|--api-url|The api url|
|-i|--client-id|The client id to cognito|

### The `-s` argument (skipping prompts when defaults are available)
If you have default values specified in code or a `.env` file, specify the `-s` will skip prompting for any parameters that are required but have an associated matching default value.


### Scripting
You can create scripts to launch several analyses by providing the runtime arguments. WARNING: you should be careful when exposing your username and password to others.
For automation, it's best to store them as a secret and retrieve the secret at runtime.


## Examples:
Let's assume you have your username, password, and API settings in environment vars.  You can use the `-s` to skip those prompts and supply the config, meta, and analysis for different runs.

```shell
# execution

python main.py -s -c <config-file> -f <analysis-file> -m <meta-file>

```

```shell

python ./main.py \
    -s \
    -f ./files/single_ev.csv \
    -c ./files/configuration_single_ev.json \
    -m ./files/meta_data.json

```