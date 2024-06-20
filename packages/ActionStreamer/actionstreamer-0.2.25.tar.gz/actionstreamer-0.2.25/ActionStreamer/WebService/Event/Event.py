import json

import ActionStreamer.CommonFunctions
import ActionStreamer.WebService.API
import ActionStreamer.Config

def get_pending_event_list(ws_config: ActionStreamer.Config.WebServiceConfig, device_name: str) -> ActionStreamer.WebService.API.WebServiceResult:

    ws_result = ActionStreamer.WebService.API.WebServiceResult(0, '', '', '', None)

    try:
        method = "POST"
        path = 'v1/event/list/pending'
        url = ws_config.base_url + path
        headers = {"Content-Type": "application/json"}
        parameters = ''

        json_post_data = {
            "deviceName": device_name
        }

        body = json.dumps(json_post_data)
        
        response_code, response_string = ActionStreamer.CommonFunctions.send_signed_request(ws_config, method, url, path, headers, parameters, body)
        
        ws_result.http_response_code = response_code
        ws_result.http_response_string = response_string
        ws_result.json_data = json.loads(response_string)

    except Exception as ex:
        ws_result.code = -1
        filename, line_number = ActionStreamer.CommonFunctions.get_exception_info()
        if filename is not None and line_number is not None:
            print(f"Exception occurred at line {line_number} in {filename}")
        print(ex)
        ws_result.description = str(ex)

    return ws_result 


def dequeue_event(ws_config: ActionStreamer.Config.WebServiceConfig, device_name: str, agent_type: str) -> ActionStreamer.WebService.API.WebServiceResult:

    ws_result = ActionStreamer.WebService.API.WebServiceResult(0, '', '', '', None)

    try:
        method = "POST"
        path = 'v1/event/dequeue'
        url = ws_config.base_url + path
        headers = {"Content-Type": "application/json"}
        parameters = ''

        json_post_data = {
            "deviceName": device_name,
            "agentType": agent_type
        }

        body = json.dumps(json_post_data)
        
        response_code, response_string = ActionStreamer.CommonFunctions.send_signed_request(ws_config, method, url, path, headers, parameters, body)
        
        ws_result.http_response_code = response_code
        ws_result.http_response_string = response_string
        ws_result.json_data = json.loads(response_string)

    except Exception as ex:
        ws_result.code = -1
        filename, line_number = ActionStreamer.CommonFunctions.get_exception_info()
        if filename is not None and line_number is not None:
            print(f"Exception occurred at line {line_number} in {filename}")
        print(ex)
        ws_result.description = str(ex)

    return ws_result 


def create_event(ws_config: ActionStreamer.Config.WebServiceConfig, device_name: str, agent_type: str, event_type: str, event_parameters: str, priority=1, max_attempts=0, expiration_epoch=0) -> ActionStreamer.WebService.API.WebServiceResult:

    ws_result = ActionStreamer.WebService.API.WebServiceResult(0, '', '', '', None)

    try:
        method = "POST"
        path = 'v1/event'
        url = ws_config.base_url + path
        headers = {"Content-Type": "application/json"}
        parameters = ''

        json_post_data = {
            "deviceName": device_name,
            "agentType": agent_type,
            "eventType": event_type,
            "eventParameters": event_parameters,
            "priority": priority,
            "maxAttempts": max_attempts,
            "expirationDate": expiration_epoch
        }

        body = json.dumps(json_post_data)
        
        response_code, response_string = ActionStreamer.CommonFunctions.send_signed_request(ws_config, method, url, path, headers, parameters, body)
        
        ws_result.http_response_code = response_code
        ws_result.http_response_string = response_string
        ws_result.json_data = json.loads(response_string)

    except Exception as ex:
        ws_result.code = -1
        filename, line_number = ActionStreamer.CommonFunctions.get_exception_info()
        if filename is not None and line_number is not None:
            print(f"Exception occurred at line {line_number} in {filename}")
        print(ex)
        ws_result.description = str(ex)

    return ws_result


def get_event_details(ws_config: ActionStreamer.Config.WebServiceConfig, event_id: int) -> ActionStreamer.WebService.API.WebServiceResult:

    ws_result = ActionStreamer.WebService.API.WebServiceResult(0, '', '', '', None)

    try:
        method = "GET"
        path = 'v1/event/' + event_id
        url = ws_config.base_url + path
        parameters = ''
        headers = {}
        body = ''
        
        response_code, response_string = ActionStreamer.CommonFunctions.send_signed_request(ws_config, method, url, path, headers, parameters, body)
        
        ws_result.http_response_code = response_code
        ws_result.http_response_string = response_string
        ws_result.json_data = json.loads(response_string)

    except Exception as ex:
        ws_result.code = -1
        filename, line_number = ActionStreamer.CommonFunctions.get_exception_info()
        if filename is not None and line_number is not None:
            print(f"Exception occurred at line {line_number} in {filename}")
        print(ex)
        ws_result.description = str(ex)

    return ws_result 


def update_event(ws_config: ActionStreamer.Config.WebServiceConfig, event_id: int, event_status: int, result: str, process_id: int, tag_string='', tag_number=0, attempt_number=1) -> ActionStreamer.WebService.API.WebServiceResult:

    ws_result = ActionStreamer.WebService.API.WebServiceResult(0, '', '', '', None)

    try:
        method = "PUT"
        path = 'v1/event' + event_id
        url = ws_config.base_url + path
        headers = {"Content-Type": "application/json"}
        parameters = ''

        json_post_data = {
            "eventStatus": event_status,
            "attemptNumber": attempt_number,
            "result": result,
            "processID": process_id,
            "tagString": tag_string,
            "tagNumber": tag_number
        }

        body = json.dumps(json_post_data)
        
        response_code, response_string = ActionStreamer.CommonFunctions.send_signed_request(ws_config, method, url, path, headers, parameters, body)
        
        ws_result.http_response_code = response_code
        ws_result.http_response_string = response_string
        ws_result.json_data = json.loads(response_string)

    except Exception as ex:
        ws_result.code = -1
        filename, line_number = ActionStreamer.CommonFunctions.get_exception_info()
        if filename is not None and line_number is not None:
            print(f"Exception occurred at line {line_number} in {filename}")
        print(ex)
        ws_result.description = str(ex)

    return ws_result