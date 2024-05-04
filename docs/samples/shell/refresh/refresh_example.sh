

export REFRESH_TOKEN="<REPLACE_WITH_YOUR_REFRESH_TOKEN>"
export COGNITO_CLIENT_ID="<REPLACE_WITH_YOUR_CLIENT_ID>"

output=$(./amazon-cognito-refresh-jwt.sh)

echo "refreshed jwt results"
echo $output