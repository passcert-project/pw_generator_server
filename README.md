# Jasmin Password Generator as a Service

RESTful service that exposes a verified password generator (coded in [Jasmin](https://github.com/jasmin-lang/jasmin) and proved in [Easycrypt](https://www.easycrypt.info)).

## Instructions
To use the service and test the service, you can follow the steps:

1. Clone this repository:
```
git clone https://github.com/passcert-project/pw_generator_server
```

2. Install all the Python requirements:

```
pip install -r requirements.txt
```

3. Run the service: 

```
python webserver.py
```
The server is now ready. To see it functioning, you can use a tool like [Postman](https://www.postman.com/) to send a POST request. 
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

## To use the Bitwarden Generator script

1. Run the command `npm install -g @bitwarden/cli`

2. Install python if you don't have. I recommend [pyenv](https://github.com/pyenv/pyenv).

3. Run the command `./generate_bw_passwords.py <number_of_passwords_you_want> <the_file_you_want_to_output_to>`

**Example**: `./generate_bw_passwords.py 10 10passwordsbw.txt` will generate 10 passwords to the file `10passwordsbw.txt` 

**NOTE:** This script may take a while. For 100 pw, it takes about 1 minute. For 1000 pw, it takes about 10 minutes.


## To use the Jasmin Generator script

1. Install python if you don't have. I recommend [pyenv](https://github.com/pyenv/pyenv).

2. Run the command `./generate_jasmin_passwords.py <number_of_passwords_you_want> <password_policy> <the_file_you_want_to_output_to>`

**Example**: `./generate_jasmin_passwords.py 10 14 1 14 1 14 1 14 1 14 10passwordsbw.txt` will generate 10 passwords to the file `10passwordsbw.txt` that comply with the policy `minlength: 10; required: upper; required: lower; required: digit; required: special;`

# To use the Policy Compliance Check script

1. Install python if you don't have. I recommend [pyenv](https://github.com/pyenv/pyenv).

2. Run the command `./policy_compliance_check.py <path_to_the_folder_with_test_data> <the_policy_to_check_against>`

**Example:** `./policy_compliance_check.py test_data/jasmin_default 14 1 14 1 14 1 14 1 14` will check the folder `./test_data/jasmin_default` against the policy `minlength: 10; required: upper; required: lower; required: digit; required: special;`.

**NOTE:** The minlength attribute in these examples is always fulfilled, since `14`, the length of the generated passwords, is always greater than `minlength = 10` 
