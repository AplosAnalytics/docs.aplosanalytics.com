
export COGNITO_USER_NAME="REPLACE_WITH_YOUR_USER_NAME"
export COGNITO_PASSWORD="REPLACE_WITH_YOUR_PASSWORD"
export COGNITO_CLIENT_ID="REPLACE_WITH_YOUR_CLIENT_ID"

output=$(./amazon-cognito-jwt.sh)

echo "curl results"
echo $output