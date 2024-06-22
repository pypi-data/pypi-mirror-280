# Performance Review CLI Assistant
## Installation

To install `pr-assistant`, run the following commands in your terminal:

```bash
chmod +x install.sh
./install.sh
```
## Getting Started
The application is run using the following command:
```pr-assistant {--arg}```
## Arguments
* ```init``` initializes the assistant, makes the nominations and saves them to state.
* ```list``` lists the nominations 
* ```email``` allows for sending emails. User is prompted to approve each email before it is sent. 
## Options for email approval
* ```y``` - approve and send email
* ```n``` - do not send the email
* ```change email``` - change the email address to whom the email is sent
* ```x``` - close execution


