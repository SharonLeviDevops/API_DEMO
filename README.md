# API_DEMO
To invoke a lambda function, passing it a file as a payload:
Create a file on your local system that stores valid json in the form of the event your lambda function expects.
Invoke the lambda function, passing it the file as the --payload parameter
Create a file called event.json with the following json in it:
{
  "num1": 10,
  "num2": 30
}
Open your terminal in the directory where you stored the event.json file. Then invoke the lambda function, passing it the event.json file as the --payload.
////
aws lambda invoke --SumFunction testFunction --cli-binary-format raw-in-base64-out --payload file://event.json response.json
////
Take a look at the response.json file to make sure the response matches your expectations.
