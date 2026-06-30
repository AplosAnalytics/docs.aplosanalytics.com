#!/bin/bash
set -e

echo building for branch: ${GIT_BRANCH_NAME}
python --version

if [ -n "$PYTHON_312_VERSION" ]; then echo "Switching to Python version ${PYTHON_312_VERSION} - using environment var for version"; pyenv global "${PYTHON_312_VERSION}"; fi

python --version

echo hello 👋 from aplos-nca-docs

# Extract the stack name from CODEBUILD_INITIATOR
echo Extracting stack name from CODEBUILD_INITIATOR
echo $CODEBUILD_INITIATOR

STACK_NAME=$(echo $CODEBUILD_INITIATOR | cut -d'/' -f2)
echo Stack name is $STACK_NAME
echo $(pwd)
export WORKING_DIRECTORY=$(pwd)
echo $WORKING_DIRECTORY

# Log into AWS CodeArtifact
DOMAIN="aplos-nca"
REPOSITORY="python"
REGION="us-east-1"
aws codeartifact login --tool pip --domain $DOMAIN --repository $REPOSITORY --region $REGION

pip install --upgrade pip
pip install -r ./devops/cdk/requirements.txt

# Upgrade node
n 20

npx cdk --version

# Install npm dependencies
echo "Installing npm dependencies..."
npm ci || npm install

# Build the VitePress documentation site
echo "Building VitePress site..."
npm run build

# Verify build output exists
if [ ! -d ".vitepress/dist" ]; then
  echo "ERROR: .vitepress/dist/ directory not found after build. Exiting."
  exit 1
fi

echo ".vitepress/dist/ directory verified successfully"

# Navigate to the cdk directory and run synth
cd ./devops/cdk

pip install -r ./requirements.txt

# Resolve HOSTED_ZONE_ID from SSM if not already set
if [ -z "$HOSTED_ZONE_ID" ] && [ -n "$TARGET_HOSTED_ZONE_ID_SSM_PARAMETER_NAME" ]; then
  export HOSTED_ZONE_ID=$(python -m cdk_factory.utilities.ssm_resolver \
    --parameter-name "$TARGET_HOSTED_ZONE_ID_SSM_PARAMETER_NAME" \
    --role-arn "$TARGET_ACCOUNT_ROLE_ARN")
fi

npx cdk synth
echo CDK Synth Complete
