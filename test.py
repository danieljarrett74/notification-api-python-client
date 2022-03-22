from notification_api_client import AwsSignedClient
from notification_api_client.models import Message, SendResponse, Error, MessageSubstitutions, GetSenderResponse, Sender, DeleteSenderResponse
from notification_api_client.api.default import send, get_sender, delete_sender
from notification_api_client.types import Response
   
   
message_substitutions: MessageSubstitutions = MessageSubstitutions()
client = AwsSignedClient(base_url="https://735kt66zjk.execute-api.us-east-1.amazonaws.com/production", region='us-east-1')



request = Message(
    template_id="CustomDomainVerifyDns",
    substitutions=message_substitutions,
    recipient_email="danieljarrett74@gmail.com"
)
response: SendResponse = send.sync_detailed(client=client,json_body=request)
print(response)



response: GetSenderResponse = get_sender.sync_detailed(client=client,sender_id="123123")
print(response)



response: DeleteSenderResponse = delete_sender.sync_detailed(client=client,sender_id="123123")
print(response)

