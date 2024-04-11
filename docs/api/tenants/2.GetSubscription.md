# Subscription



## Payload
```json


```

## Python

```python
self.monthly_executions: int = 0
self.type: str = None
"""
The Type of subscription: Early Access, Individual, Developer, Gold, Platinum, etc
"""
self.status: str = None
"""
The current status: active / disabled 
"""
self.start_date: str = None
"""
The start date
"""
self.end_date: str = None
"""
The end date
"""
self.next_renewal_date: str = None
"""
The next date this renewals
This needs to be updated once payments go through
"""
self.auto_renewal: bool = None
"""
Does it auto renew
"""
self.renewal_fee: str = None
"""
The renewal rate
"""
self.renewal_cadence: str = None
"""
What is the cadence Monthly, Quarterly, Yearly, etc
"""
self.id: str = None
"""
The current subscription / contract id
"""
self.user_allocation: int = 1
"""
The number of users they can have
"""

```

|key|description|type|requried|mutable|
|-|-|-|-|-|