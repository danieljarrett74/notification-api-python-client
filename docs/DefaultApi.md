# swagger_client.DefaultApi

All URIs are relative to *https://${data.aws_region.current.name}.execute-api.${data.aws_region.current.name}.amazonaws.com/{basePath}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sender**](DefaultApi.md#delete_sender) | **DELETE** /sender/{senderId} | 
[**delete_sender_template**](DefaultApi.md#delete_sender_template) | **DELETE** /sender/{senderId}/template/{templateId} | 
[**delete_template**](DefaultApi.md#delete_template) | **DELETE** /template/{templateId} | 
[**get_sender**](DefaultApi.md#get_sender) | **GET** /sender/{senderId} | 
[**get_sender_template**](DefaultApi.md#get_sender_template) | **GET** /sender/{senderId}/template/{templateId} | 
[**get_sender_templates**](DefaultApi.md#get_sender_templates) | **GET** /sender/{senderId}/templates | 
[**get_template**](DefaultApi.md#get_template) | **GET** /template/{templateId} | 
[**put_sender**](DefaultApi.md#put_sender) | **POST** /sender | 
[**put_template**](DefaultApi.md#put_template) | **POST** /template | 
[**send**](DefaultApi.md#send) | **POST** /send | 

# **delete_sender**
> DeleteSenderResponse delete_sender(sender_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
sender_id = 'sender_id_example' # str | 

try:
    api_response = api_instance.delete_sender(sender_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_sender: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender_id** | **str**|  | 

### Return type

[**DeleteSenderResponse**](DeleteSenderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sender_template**
> DeleteSenderTemplateResponse delete_sender_template(template_id, sender_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
template_id = 'template_id_example' # str | 
sender_id = 'sender_id_example' # str | 

try:
    api_response = api_instance.delete_sender_template(template_id, sender_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_sender_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **sender_id** | **str**|  | 

### Return type

[**DeleteSenderTemplateResponse**](DeleteSenderTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> DeleteTemplateResponse delete_template(template_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
template_id = 'template_id_example' # str | 

try:
    api_response = api_instance.delete_template(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**DeleteTemplateResponse**](DeleteTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sender**
> GetSenderResponse get_sender(sender_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
sender_id = 'sender_id_example' # str | 

try:
    api_response = api_instance.get_sender(sender_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_sender: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender_id** | **str**|  | 

### Return type

[**GetSenderResponse**](GetSenderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sender_template**
> GetSenderTemplateResponse get_sender_template(template_id, sender_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
template_id = 'template_id_example' # str | 
sender_id = 'sender_id_example' # str | 

try:
    api_response = api_instance.get_sender_template(template_id, sender_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_sender_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **sender_id** | **str**|  | 

### Return type

[**GetSenderTemplateResponse**](GetSenderTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sender_templates**
> GetSenderTemplatesResponse get_sender_templates(sender_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
sender_id = 'sender_id_example' # str | 

try:
    api_response = api_instance.get_sender_templates(sender_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_sender_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender_id** | **str**|  | 

### Return type

[**GetSenderTemplatesResponse**](GetSenderTemplatesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> GetTemplateResponse get_template(template_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
template_id = 'template_id_example' # str | 

try:
    api_response = api_instance.get_template(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**GetTemplateResponse**](GetTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sender**
> PutSenderResponse put_sender(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Sender() # Sender | 

try:
    api_response = api_instance.put_sender(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_sender: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Sender**](Sender.md)|  | 

### Return type

[**PutSenderResponse**](PutSenderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_template**
> PutTemplateResponse put_template(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Template() # Template | 

try:
    api_response = api_instance.put_template(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Template**](Template.md)|  | 

### Return type

[**PutTemplateResponse**](PutTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send**
> SendResponse send(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Message() # Message | 

try:
    api_response = api_instance.send(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Message**](Message.md)|  | 

### Return type

[**SendResponse**](SendResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

