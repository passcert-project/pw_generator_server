# To use the webserver that generates random passwords using Passcert's Generator

1. Install python if you don't have. I recommend [pyenv](https://github.com/pyenv/pyenv).

2. Run the command `pip install flask`

3. Run the command `./webserver.py`. The server is now ready. 

4. To see it functioning, use a tool like [Postman](https://www.postman.com/), and send a POST request with the body of the request like:

```json
{"options": "14 1 14 1 14 1 14 1 14"}
```
The arguments are as follows:

- length
- lowercasemin
- lowercasemax
- uppercasemin
- uppercasemax
- numbersmin
- numbersmax
- specialmin
- specialmax

5. The server will return a `json` object, in the form of:

```json
{
    "generated_password": "<random_password>"
}
```

# To use the Bitwarden Generator script

1. Run the command `npm install -g @bitwarden/cli`

2. Install python if you don't have. I recommend [pyenv](https://github.com/pyenv/pyenv).

3. Run the command `./generate_bw_passwords.py <number_of_passwords_you_want> <the_file_you_want_to_output_to>`

**Example**: `./generate_bw_passwords.py 10 10passwordsbw.txt` will generate 10 passwords to the file `10passwordsbw.txt`

**NOTE:** This script may take a while. For 100 pw, it takes about 1 minute. For 1000 pw, it takes about 10 minutes.
