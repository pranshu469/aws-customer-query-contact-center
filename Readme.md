1.	In this prototype, customer signs-up/signs-in to a web application and presented with a form to enter user-details like Name, contact info and their query.
2.	API Gateway GET endpoint is used to display the form.
3.	Upon submitting these details, an API Gateway (REST API) is invoked which has a POST method integrated to a Lambda function as a proxy integration.
4.	Lambda function fetches these details and stores them in DynamoDB and sends an acknowledgement to customer that their data has been successfully stored and they will get a call from our call center representative.
5.	We have used another Lambda function and added the DDB as a trigger, which will initiate an outbound call using start-outbound-voice-contact API provided by Amazon Connect.
6.	In StartOutboundVoiceContact we’ll specify contact flow id, which contains a dedicated queue for holding these contacts and calls will be made as per agent staffing in call center.

Architecture : 
