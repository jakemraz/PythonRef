import boto3

def bulk_verification():

  client = boto3.client('ses')
  response = client.send_custom_verification_email(
    EmailAddress= "pinpoint2@yopmail.com",
    TemplateName= "VerificationTemplate"
  )
  print(response)


def create_custom_verification_email_template():

  client = boto3.client('ses')
  response = client.create_custom_verification_email_template(
    TemplateName= "VerificationTemplate",
    FromEmailAddress= "pinpoint1@yopmail.com",
    TemplateSubject= "Please confirm your email address",
    TemplateContent= '''
                      <html>
                      <head></head>
                      <body style='font-family:sans-serif;'>
                        <h1 style='text-align:center'>Ready to start sending 
                        email with ProductName?</h1>
                        <p>We here at Example Corp are happy to have you on
                          board! There's just one last step to complete before
                          you can start sending email. Just click the following
                          link to verify your email address. Once we confirm that 
                          you're really you, we'll give you some additional 
                          information to help you get started with ProductName.</p>
                      </body>
                      </html>
                      ''',
    SuccessRedirectionURL= "https://www.google.com",
    FailureRedirectionURL= "https://www.naver.com"
  )
  print(response)

bulk_verification()