import sys, os, base64, datetime, hashlib, hmac 
import boto3

def sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

def get_signature_key(key, dateStamp, regionName, serviceName):
    kDate = sign(('AWS4' + key).encode('utf-8'), dateStamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, 'aws4_request')
    return kSigning

def get_auth_header(method:str, host:str, region:str, request_parameters:str, canonical_uri:str = '/', payload:str = None) -> str:

    service = 'execute-api'

    session = boto3.Session()
    credentials = session.get_credentials()
    current_credentials = credentials.get_frozen_credentials()
    
    access_key = current_credentials.access_key
    secret_key = current_credentials.secret_key
    session_token = current_credentials.token
    # print("current credentials access_key: %s" % access_key)
    # print("current credentials secret_key: %s" % secret_key)
    # print("current credentials token: %s" % session_token)


    t = datetime.datetime.utcnow()
    amzdate = t.strftime('%Y%m%dT%H%M%SZ')
    datestamp = t.strftime('%Y%m%d') 
    canonical_querystring = request_parameters
    canonical_headers = 'host:' + host + '\n' + 'x-amz-date:' + amzdate + '\n'
    signed_headers = 'host;x-amz-date'

    if payload is not None:
        payload_hash = hashlib.sha256(payload.encode('utf-8')).hexdigest()
    else:
        payload_hash = hashlib.sha256(('').encode('utf-8')).hexdigest()

    canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash
    algorithm = 'AWS4-HMAC-SHA256'
    credential_scope = datestamp + '/' + region + '/' + service + '/' + 'aws4_request'
    string_to_sign = algorithm + '\n' +  amzdate + '\n' +  credential_scope + '\n' +  hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()
    signing_key = get_signature_key(secret_key, datestamp, region, service)
    signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()
    authorization_header = algorithm + ' ' + 'Credential=' + access_key + '/' + credential_scope + ', ' +  'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature

    print("canonical_request:%s" % canonical_request)

    print("string_to_sign:%s" % string_to_sign)

    print("payload:%s" % payload)
    if session_token is None:
        return {'x-amz-date':amzdate, 'Authorization':authorization_header}
    else:
        return {'x-amz-security-token': session_token, 'x-amz-date':amzdate, 'Authorization':authorization_header}