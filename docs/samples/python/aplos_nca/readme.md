# Analysis with Python

You can use 🐍 python to perform analysis with Aplos NCA using API calls via secure https requests. We have prepared sample scripts to illustrate how this analysis can be performed using python. 

This was created as a reusable library which was wrapped with commandline parsing.  You can use command line switches or simply run it and get prompted for the required input.

All the source code can be downloaded from our [docs repo](https://github.com/AplosAnalytics/docs.aplosanalytics.com/tree/main/docs/samples/python/aplos_nca).

>[!TIP] We use this for our demos
> We'll keep this maintained as we use it for our customer demos.  So keep coming back for new features.


## API Settings

> [!WARNING] A valid Aplos NCA Account is required.
> In order to run the executions and connect to our system, you will need a valid account with an active subscription.
>
> You'll need your username (email address and a password) a Cognito Client Id
> which allows the USER_PASSWORD_AUTH flow, and your API URL.  
> 
> The Client Id (aka Cognito Client Key) and API URL can be found in your user account.
> Your username is your email address and your password would have been provided to you during your
> onboarding or with a "forgot password" request and reset.

### Access your settings from the UI
![API Configuration](/docs/samples/images/API_Configuration_blur.png)


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


## Required Files for execution (analysis submission)
To submit something for an analysis, you will need 2 required files and one optional file.  
- Input File (analysis file)
- Configuration File (configurations on how to run the analysis)
- Meta Data (optional)

Technically only the analysis file is submitted as a file.  

The other two (configuration and metadata) are submitted as JSON/dictionary objects.  However to make things easier for this demo they are stored as files, then read in at runtime and submitted in their normal dictionary form.

The files are located `./files` directory of this demo project (`./samples/python/aplos_nca`).


## Outputs
Currently, we are outputting the files in a hidden directory (`.output`) which is also excluded from the git commits.  This can easily be overridden to your choosing.

Located in `./.output`


## Run the Execution

In order to run the execution you need to either:
- Add environment variables for the required parameter see [Environment Vars](/docs/samples/python-overview.html#environment-vars) later in this document
- Use the command switch arguments
- Or simply input the values as you are prompted.

> [!TIP] Tip! Use environment vars and override when needed.
> You can set the environment variables, but still override them during the prompts

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

> [!TIP]
> If you have certain values present the command line tool will prompt to see if you want to use the defaults or override them.
> If you want to skip the prompt, use `-s` as an argument.  This will skip the prompt for any value already set.

### Sample execution

If your username, password, client key and API URL are already set, then the only thing you need to do on each run is supply the configuration and the analysis file.  The meta-data file is optional.  Issuing the `-s` will skip all the extra prompts.

```shell
# single line execution example

python main.py -s -c <config-file> -f <analysis-file> -m <meta-file>

```

### Same example, on multiple lines and with example files

```shell

# break into multiple lines for easier readability
# NOTE: a copy paste of this from code samples doesn't always work right

python ./main.py \
    -s \
    -f ./files/single_ev.csv \
    -c ./files/configuration_single_ev.json \
    -m ./files/meta_data.json

```

## Environment Vars

To save time and typing you can use environment variables to "pre-load" your execution and then any "unknown" value will be asked by the command line utility.

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

> [!TIP]
> You can also create a `.env` file locally and enter the environment vars there.

```shell
APLOS_API_URL="<api-gateway-url>"
COGNITO_CLIENT_ID="<client-id>"
COGNITO_USER_NAME="<email-address>"
COGNITO_PASSWORD="<password>"
COGNITO_REGION="<region>"
```

## The Command Line in Action
In this example, I have all my settings preloaded in environment vars and I just hit enter several times to accept the defaults.

![Commandline App](/docs/samples/python/aplos_nca/images/aplos-nca-commandline-cropped.png)