import os
import pickle
import time
from openai import OpenAI
import json
import smtplib
import argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import chevron

ASSISTANT_ID = "asst_2u0kWkMEL0rqxOAniSPo2AG5"
def show_json(obj):
    print(json.loads(obj.model_dump_json()))

# Pretty printing helper
def pretty_print(messages):
    result = ""
    for m in messages:
        line = f"{m.role}: {m.content[0].text.value}\n"
        #print(line, end="")
        result += line
    return result
    #client.beta.assistants.update(instructions='')
def submit_message(assistant_id, thread, user_message):
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=user_message
    )
    return client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )

def get_response(thread):
    return client.beta.threads.messages.list(thread_id=thread.id, order="asc")

def submit_and_run(user_input, thread):
    
    run = submit_message(ASSISTANT_ID, thread, user_input)
    return run

def wait_on_run(run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

PROMPT = open('prompt.txt', 'r').read()
#ASSISTANT_ID = "asst_4Mue7dtcWpBgwfeS9K99csSu"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def initiate_assistant_and_thread():
    assistant = client.beta.assistants.update(
        assistant_id=ASSISTANT_ID,
        instructions=PROMPT,
    )
    print('assistant initiated. name:', assistant.name)
    thread = client.beta.threads.create(
      messages=[
        {
          "role": "user",
          "content": "/init true",
        }
      ]
    )
    print('thread initiated. id:', thread.id)
    return assistant, thread









def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

def generate_review_list_and_email(thread):
    print('Generating review list')
    message = """
    /init true
    """
    run = submit_and_run(message, thread)
    run = wait_on_run(run, thread)
    
    return get_response(thread)

def parse_review_list_and_email(text):
    lines = text.split('\n')
    reviews = {}
    emails = {}
    current_member = None
    email_body = []
    email_mode = False

    for line in lines:
        line = line.strip()
        
        # Identify the start of an email
        if line.startswith("Dear "):
            if current_member and email_body:
                emails[current_member] = '\n'.join(email_body)
            current_member = line.split()[1].rstrip(',')
            email_body = [line]
            email_mode = True
        
        # Handle review assignments
        elif line.startswith("- Review:") or line.startswith("Please review"):
            email_body.append(line)
        
        # Handle the list of people to review
        elif line and not line.startswith("###") and not email_mode:
            if ":" in line:
                member, review_list = line.split(':')
                member = member.strip()
                review_list = [review.strip() for review in review_list.split(',')]
                reviews[member] = review_list
        
        # Collect email body
        elif email_mode:
            email_body.append(line)
    
    # Add the last email to the emails dictionary
    if current_member and email_body:
        emails[current_member] = '\n'.join(email_body)
    
    return reviews, emails

def generate_emails(thread):
    print('Generating Emails')
    message = """
    /email All
    """
    run = submit_and_run(message, thread)
    run = wait_on_run(run, thread)
    #print(pretty_print(get_response(thread)))
    return get_response(thread)
import re
import json

def extract_json_from_text(text):
    # Use regex to find the JSON object in the text
    match = re.search(r'```json\n({.*?})\n```', text, re.DOTALL)
    
    if match:
        json_text = match.group(1)
        try:
            # Parse the JSON text
            data = json.loads(json_text)
            return data
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
            return None
    else:
        print("No JSON object found in the text.")
        return None

def parse_emails(json_data):
    emails = json_data.get("emails", {})
    parsed_emails = []
    
    for name, details in emails.items():
        email_info = {
            "name": name,
            "address": details.get("address"),
            "subject": details.get("subject"),
            "body": details.get("body")
        }
        parsed_emails.append(email_info)
    
    return parsed_emails
def main():
    parser = argparse.ArgumentParser(description='Peer Review Email CLI')
    parser.add_argument('command', choices=['init', 'list', 'email'], help='Choose command to execute: init, list, or email')
    parser.add_argument('--init', action='store_true', help='Initialize the assistant and thread')
    parser.add_argument('--list', nargs='?', const=True, metavar='name', help='List reviews for all or specific employee')
    parser.add_argument('--email', action='store_true', help='Show email and ask for approval to send')
    filename = "local_storage.txt"
    filename_emails = "local_storage_emails.txt"

    args = parser.parse_args()
    if args.command == 'init':
        with open(filename, "r+") as file:
            file.truncate(0)
        with open(filename_emails, "r+") as file:
            file.truncate(0)
        assistant, thread = initiate_assistant_and_thread()
        review_list_and_email = generate_review_list_and_email(thread)
        with open(filename, "w") as file:
            # Write the string to the file
            file.write(pretty_print(review_list_and_email))
        emails = generate_emails(thread)
        print('Emails generated.')
        email_list = list(emails)
        with open(filename_emails, "w") as file:
            # Write the string to the file
            file.write(email_list[4].content[0].text.value)
        print('Initiation complete.\nKindly use --list to view nominations and --email to send emails.')
        
    if  args.command == 'list':
        with open(filename, "rb") as file:
            # Read the string from the file
            saved_list = file.read()
            if not saved_list:
                print("Please run init first to generate the review list.")
            else: 
                review_list = list(saved_list)
                #print(saved_list)
                
    
    if  args.command == 'email':
        with open(filename_emails, "r") as file:
            # Read the string from the file
            saved_emails = file.read()
            if not saved_emails:
                print("Please run init first to generate the emails.")
            else: 
                email_list = list(saved_emails)
                data = (extract_json_from_text(saved_emails))
                for name, info in data['emails'].items():
                    arggs = {
                    'template': "Dear {{> name}},<br><br>You have been selected to review the following peers:<br><br>{{> reviewers}}<br><br>Best Regards<br><br> <small>This is an auto-generated email. Please contact ahmad.akilan@beno.com for any questions.</small>",
                    
                    'partials_dict': {
                        'name': name,
                        'reviewers': info['body']
                    }
                    }

                    print(f"Name: {name}")
                    print(f"Email Address: {info['address']}")
                    print(f"Subject: {info['subject']}")
                    print(f"Body:\n{chevron.render(**arggs)}")
                    print("\n")
                    approval = input("Send this email? ((y)es/(n)o/e(x)it/(c)hange mail): ")
                    if approval.lower() == 'x' or approval.lower() == 'exit':
                        break
                    elif approval.lower() == 'y' or approval.lower() == 'yes':
                            send_email(info['subject'], chevron.render(**arggs), sender='ahmed.saad@beno.com',  recipients='ahmed.saad@beno.com', password='Beno@ajm12')
                            print(f"Email sent to {info['address']}.")
                    elif approval.lower() == 'n' or approval.lower() == 'no':
                        print(f"Email not sent to {info['address']}.")
                    elif approval.lower() == 'c' or approval.lower() == 'change mail':
                            new_mail = input("Enter new mail: ")
                            info['address'] = new_mail
                            print(f"Name: {name}")
                            print(f"Email Address: {info['address']}")
                            print(f"Subject: {info['subject']}")
                            print(f"Body:\n{chevron.render(**arggs)}")
                            print("\n")
                            reapproval = input("Send this email? ((y)es/(n)o)/e(x)it: ")
                            if reapproval.lower() == 'y' or reapproval.lower() == 'yes':
                                send_email(info['subject'], info['body'], sender='ahmed.saad@beno.com',  recipients='ahmed.saad@beno.com', password='Beno@ajm12') #change recepient to new_mail
                            elif reapproval.lower() == 'n' or reapproval.lower() == 'no':
                                print(f"Email not sent to {info['address']}.")
                            elif reapproval.lower() == 'x' or reapproval.lower() == 'exit':
                                break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()