

Error Message 0.1.0
```json

{
    "action": "get_user",
    "errors": [
        "Parameter validation failed:\nInvalid type for parameter Password, value: None, type: <class 'NoneType'>, valid types: <class 'str'>"
    ],
    "stack_traces": {
        "name": "traceback.format_exc()",
        "value": "Traceback (most recent call last):\n  File \"/var/task/app.py\", line 58, in lambda_handler\n    status_code, user = UserAccountServices().user_update_password(\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/opt/python/common/services/user_services/user_account_services.py\", line 197, in user_update_password\n    self.admin_reset_user_password(user)\n  File \"/opt/python/common/services/user_services/user_account_services.py\", line 218, in admin_reset_user_password\n    response = CognitoUtility().admin_set_user_password(\n               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/opt/python/common/cognito_utils/cognito_utility.py\", line 136, in admin_set_user_password\n    response = self.client.admin_set_user_password(\n               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/var/lang/lib/python3.11/site-packages/botocore/client.py\", line 553, in _api_call\n    return self._make_api_call(operation_name, kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/opt/python/wrapt/wrappers.py\", line 669, in __call__\n    return self._self_wrapper(self.__wrapped__, self._self_instance,\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/opt/python/aws_xray_sdk/ext/botocore/patch.py\", line 38, in _xray_traced_botocore\n    return xray_recorder.record_subsegment(\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/opt/python/aws_xray_sdk/core/recorder.py\", line 456, in record_subsegment\n    return_value = wrapped(*args, **kwargs)\n                   ^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/var/lang/lib/python3.11/site-packages/botocore/client.py\", line 962, in _make_api_call\n    request_dict = self._convert_to_request_dict(\n                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/var/lang/lib/python3.11/site-packages/botocore/client.py\", line 1036, in _convert_to_request_dict\n    request_dict = self._serializer.serialize_to_request(\n                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/var/lang/lib/python3.11/site-packages/botocore/validate.py\", line 381, in serialize_to_request\n    raise ParamValidationError(report=report.generate_report())\nbotocore.exceptions.ParamValidationError: Parameter validation failed:\nInvalid type for parameter Password, value: None, type: <class 'NoneType'>, valid types: <class 'str'>\n"
    },
    "authenticated_user_id": "30f91fe3-3910-466f-a4f8-00635f062780",
    "target_user_id": "391bdf01-2e9a-43eb-9370-f3d0681032ea",
    "diagnostics": {
        "context": {
            "memory_limit_in_mb": "128",
            "get_remaining_time_in_millis": 9502
        },
        "event": {
            "user_id": "30f91fe3-3910-466f-a4f8-00635f062780",
            "email": "eric.wilson@aplosanalytics.com"
        },
        "app_info": {
            "version": {
                "number": "v0.1.0-63-g4ce344af",
                "build_date": "2024-04-08T18:02:44Z"
            }
        }
    }
}

```