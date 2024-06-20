import json

import ActionStreamer.CommonFunctions
from ActionStreamer import CommonFunctions
import ActionStreamer.WebService.API
import ActionStreamer.Config


def create_health(ws_config: ActionStreamer.Config.WebServiceConfig, device_name: str, health_json: str) -> ActionStreamer.WebService.API.WebServiceResult:
    
    ws_result = ActionStreamer.WebService.API.WebServiceResult(0, '', '', '', None)

    try:
        method = "POST"
        path = 'v1/devicehealth'
        url = ws_config.base_url + path
        headers = {"Content-Type": "application/json"}
        parameters = ''

        json_post_data = {
            "deviceName": device_name,
            "healthJSON": health_json
        }

        body = json.dumps(json_post_data)
        
        response_code, response_string = ActionStreamer.CommonFunctions.send_signed_request(ws_config, method, url, path, headers, parameters, body)
        
        ws_result.http_response_code = response_code
        ws_result.http_response_string = response_string
        ws_result.json_data = json.loads(response_string)

    except Exception as ex:
        ws_result.code = -1
        filename, line_number = CommonFunctions.get_exception_info()
        if filename is not None and line_number is not None:
            print(f"Exception occurred at line {line_number} in {filename}")
        print(ex)

    return ws_result


def update_health(ws_config: ActionStreamer.Config.WebServiceConfig, device_name: str, health_json: str) -> ActionStreamer.WebService.API.WebServiceResult:

    ws_result = ActionStreamer.WebService.API.WebServiceResult(0, '', '', '', None)

    try:
        method = "PUT"
        path = 'v1/devicehealth'
        url = ws_config.base_url + path
        headers = {"Content-Type": "application/json"}
        parameters = ''

        json_post_data = {
            "deviceName": device_name,
            "healthJSON": health_json
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

    return ws_result