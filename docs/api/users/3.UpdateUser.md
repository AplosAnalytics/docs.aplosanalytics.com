# Update a Users Profile
Users have the ability to update their profile information. And Tentant Admins have the ability to update users with in their tenancy.

## Route
`/users/{id}`

## Payload

```json
{    
    "email_address": "john.doe@aplosanalytics.com",
    "first_name": "johnny",
    "id": "391bdf01-2e9a-43eb-9370-f3d0681032ea",
    "last_name": "doe",
    "phone_numbers": ["919-555-5555"],            
}
```

|key|description|type|requried|mutable|
|-|-|-|-|-|
|id|the users id|str|yes|no|
|email_address|the users email address|str|yes|yes|
|first_name|the users first name|str|yes|yes|
|last_name|the users last name|str|yes|yes|
|phone_number|the users phone numbers|array/list|no|yes

## Requirements

We currently require the user's id in the route and the payload.  We may remove this requirement in the future.  Currently it's just used as a double-check in validation routines

