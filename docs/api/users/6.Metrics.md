# Metrics
Returns metric data for a user and their tenancy.

## User & Tenant

Metrics are broken into two categories.  Tenant and User.

In our General Multi-Tenant Account system, each user will have a unique `tenant_id` and `user_id`.  In this case it's a 1 to 1 relationshil and the metric values for a Tenant and a User will be the same.  The `tenant_id` and the `user_id` will also be the same.  

At this time the General Account will not allow multiple users in the same tenancy.  This is simply a choice for the account structure and may change in the future. 

Users who upgrade to a **Team Account** have the ability to add users to their team.  In this case, more users are attached to a specific tenant.  All users in this type of account will share the same `tenant_id`.


If this is a single user account the numbers for tenancy and user should always be the same.  If this is a multi-tenancy / team account the numbers will vary.  The tenancy number will be the tenancy as a whole, while the user completed number will reflect the individual users


## Metric: Completed 
The number of completed executions for the given month for the tenancy or user.  This number reflects the number of successfull completed executions which goes towards your monthly tokens for executions.


## Failed:
Failed executions which don't apply to your totals monthly allocations.

## Inflight 
Inflight is the number of executions that are in process.  This number is also used during the evaluation of running executions.  When something is inflight (queuing or being processed), it's calculated as part of your monthly allotment.  Once it hits a finished state of `complete` or `failed` it will then no longer appear as an `inflight` metric and will be added to the `complete` or `failed` metric


## Route
|item|description|
|---|---|
|route|/users/{user-id}/metrics|
|method|get|


## Response:

The following response shows a user with the same id for its tenancy.

As you will see all the metric values are the same.

The user has completed 4 and 2 inflight which is counted towards the allocated monthly of 1000 leave 994 remaining for the month.  Failed executions are not counted.


### Example Response

```json
{
    "tenant": {
        "id": "1111111111111111",
        "completed": "4",
        "failed": "3",
        "in_flight": "2",
        "allocated": "1000",
        "remaining": "994"
    },
    "user": {
        "id": "1111111111111111",
        "completed": "4",
        "failed": "3",
        "in_flight": "2",
        "allocated": "1000",
        "remaining": "994"
    }
}

```


### Example Response after completions

The next example is based on the pervious example (after 1 completed and 1 failed).

Only the `completed` is counted toward your monthly remaining.

```json
{
    "tenant": {
        "id": "1111111111111111",
        "completed": "5",
        "failed": "4",
        "in_flight": "0",
        "allocated": "1000",
        "remaining": "995"
    },
    "user": {
        "id": "1111111111111111",
        "completed": "5",
        "failed": "4",
        "in_flight": "0",
        "allocated": "1000",
        "remaining": "995"
    }
}

```

