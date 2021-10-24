# Jasmin Password Generator as a Service

RESTful service that exposes a verified password generator (coded in [Jasmin](https://github.com/jasmin-lang/jasmin) and proved in [Easycrypt](https://www.easycrypt.info)).

To read the instructions for setting up the service, [click here](https://github.com/passcert-project/pw_generator_server/tree/main/generator_server)

## To use the Bitwarden Generator script

1. Run the command `npm install -g @bitwarden/cli`

2. Run the command `./generate_bw_passwords.py <number_of_passwords_you_want> <the_file_you_want_to_output_to>`

**Example**: `./generate_bw_passwords.py 10 10passwordsbw.txt` will generate 10 passwords to the file `10passwordsbw.txt` 

**NOTE:** This script may take a while. For 100 passwords, it takes about 1 minute. For 1000 passwords, it takes about 10 minutes.


## To use the Jasmin Generator script

Run the command `./generate_jasmin_passwords.py <number_of_passwords_you_want> <password_policy> <the_file_you_want_to_output_to>`

The policy has this structure:
- length
- minimumLowercase
- maximumLowercase
- minimumUppercase
- maximumUppercase
- minimumNumbers
- maximumNumbers
- minimumSpecial
- maximumSpecial

**Example**: `./generate_jasmin_passwords.py 10 14 1 14 1 14 1 14 1 14 10passwordsbw.txt` will generate 10 passwords to the file `10passwordsbw.txt` that comply with the policy `minlength: 10; required: upper; required: lower; required: digit; required: special;`

## To use the Policy Compliance Check script

Run the command `./policy_compliance_check.py <path_to_the_folder_with_test_data> <the_policy_to_check_against>`

**Example:** `./policy_compliance_check.py test_data/jasmin_default 14 1 14 1 14 1 14 1 14` will check the folder `./test_data/jasmin_default` against the policy `minlength: 10; required: upper; required: lower; required: digit; required: special;`.

**NOTE:** 
- The minlength attribute in these examples is always fulfilled, since `14`, the length of the generated passwords, is always greater than `minlength = 10`
- This Compliance Check Script was developed for Jasmin Generated Passwords. It is possible that this tool is not accurate for Bitwarden's Smartpasswords, because the policy is not describable in this format, e.g., this policy:

`minlength: 10; required: [a](1, 4); allowed: upper, digit; minclasses:2; blocklist:default;`

It's impossible to describe it accurately, because we can only use restrictions for `lowercase` and not characters themselves. The rough translation for this policy would be `10 1 4 0 10 0 10 0 0`. But this allows for a password to contain ***any*** lowercase letter.