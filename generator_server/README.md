# Jasmin Password Generator as a Service

RESTful service that exposes a verified password generator (coded in [Jasmin](https://github.com/jasmin-lang/jasmin) and proved in [Easycrypt](https://www.easycrypt.info)).

## Setting up the server

### Docker 
1. Install [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/install/).

2. Run the command `docker-compose up`

The server is now running. 

### Running the script
1. Clone this repository:
```
git clone https://github.com/passcert-project/pw_generator_server
```

2. Install all the Python requirements:

```
pip install -r requirements.txt
```

Run the webserver: 

```
python webserver.py
```
The server is now running. 


## Generating Passwords With The Server

You can use a tool like [Postman](https://www.postman.com/) to send a POST request. 
The body of the request (raw option in [Postman](https://www.postman.com/)) should be similar to the following:

```json
{"pw_settings": "14 1 14 1 14 1 14 1 14"}
```
The arguments are as follows:

- length
- minimumLowercase
- maximumLowercase
- minimumUppercase
- maximumUppercase
- minimumNumbers
- maximumNumbers
- minimumSpecial
- maximumSpecial

The server will return a `json` object, in the form of:

```json
{
    "generated_password": "<random_password>"
}
```

**NOTE:** The Jasmin password generator included in this repository is a pre-compiled binary file (x86). If you want to create your own binary, you will have to [follow the instructions in Passcert's RPG repository](https://github.com/passcert-project/random-password-generator).
