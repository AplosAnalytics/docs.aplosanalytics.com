# Update Password
 Users and user managers have the ability to update their password.  You'll need to provide the password, the confirmation of the password as well as the previous password.

## Payload

```json
{
    "password": "",
    "password_confirmed": "",
    "previous_password": "",
}
```

|key|description|type|requried|mutable|
|-|-|-|-|-|
|password_new|the users new password|str|yes|yes|
|password_new_confirmed|the confirmed users new password|str|yes|yes|


## Flow
The passwords will be verified that they match and the preivous password will be validated that it was correct prior to changing the password.

## Responses
A successful response will be as follows:
TBD

## Errors

Errors from validation or other issues will be as follows

TBD