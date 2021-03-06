# TEST DATA FOLDER

Each of these folders represent some kind of test.

The `bw_default` has 10000 passwords, separated by 10 files, using Bitwarden's default password generation recipe.
- 14 1 14 1 14 1 14 0 0

The `jasmin_default` has 10000 passwords, separated by 10 files, using Jasmin's default password generation recipe.
- 14 1 14 1 14 1 14 1 14

The `jasmin_min15` has 10000 passwords, separated by 10 files, allowing all ascii characters and length=15.
- 15 1 15 1 15 1 15 1 15

The `bw_special` has 10000 passwords, separated by 10 files, using Bitwarden's complete generation recipe: includes lower, upper, digit and special.
- 14 1 14 1 14 1 14 1 14

The `bw_special_dsl` has 1000 passwords - manually generated -, separated by 10 files, using Bitwarden's complete generation recipe: includes lower, upper, digit and special and our extension to Apple's DSL.

All passwords should be compliant, since they were generated using the our DSL.
- 14 1 14 1 14 1 14 1 14

**NOTE**: To test the `bw_special` and `bw_special_dsl`, you need to change the value of `SPECIAL_BW`, in the `policy_compliance_check.py` file.
The current set is the special characters included by Bitwarden. However, we tested against this policy:

`minlength: 8; required: lower; required: upper; required: digit; required: [!#$@];`

Thus, the compliance must check the special characters with the set that is required --- [!#$@]. 

With these changes, for `bw_special` the expected result is achieved: 26.71% of the passwords are non-compliant.
And for `bw_special_dsl` it is also achieved: 100% compliance.

## Manually collected passwords

For these tests, we manually generated 100 passwords for each policy. We used the [dummy-server](https://github.com/passcert-project/dummy-server) and just changed the policy accordingly.


### The `bw_3c8` batch 

Passwords were generated according to: 

- `minlength: 8; allowed: ascii-printable; minclasses: 3; blocklist:default;`

And should be checked against:
- `8 0 8 0 8 0 8 0 8 --minclasses 3`  -> 94% compliance.

However, since Bitwarden sets the default length of the password to 14 when the minlength given is lower than 14, there are 6 failing passwords according to this policy --- they have more than 8 lowercase/uppercase letters. The real policy these passwords should be:

- `14 0 14 0 14 0 14 0 14 --minclasses 3` -> 100% compliance.


### The `bw_all_classes_with_ranges` batch 

Passwords were generated according to: 

- `minlength: 10; required: upper(4, 10); required: lower(4, 6); required: digit(4, 8); required: special (4, 10);`

And should be checked against:
- `16 4 6 4 10 4 8 4 10` -> 100% compliance.


### The `bw_required_and_allowed_ranges` batch 

Passwords were generated according to: 

- `minlength: 14; required: lower(5, 10); required: digit(5, 10); allowed: upper(0, 4), special; minclasses: 3;`

And should be checked against:
- `14 5 10 0 4 5 10 0 14 --minclasses 3` -> 100% compliance.
- `14 5 10 0 4 5 10 0 14 --minclasses 3 --blocklist` -> 91% compliance. The passwords were not generated with a `blocklist:default;` rule.


### The `bw_required_and_allowed_ranges_blocklist` batch 

Passwords were generated according to: 

- `minlength: 14; required: lower(5, 10); required: digit(5, 10); allowed: upper(0, 4), special; minclasses: 3; blocklist:default;`

And should be checked against:
- `14 5 10 0 4 5 10 0 14 --minclasses 3` -> 100% compliance.
- `14 5 10 0 4 5 10 0 14 --minclasses 3 --blocklist` -> 100% compliance.


### The `bw_required_lower_or_digit_with_ranges` batch 

Passwords were generated according to: 

- `minlength: 14; required: lower(5, 10), digit(5, 10); allowed: upper, special;`

And should be checked against:
- `14 5 10 0 14 5 10 0 14` (including everything. all should fail) -> 0% compliance | 100% failed.
- `14 5 10 0 14 0 0 0 14` (including lower. some should pass) -> 51% compliance | 49% failed.
- `14 0 0 0 14 5 10 0 14` (including digits. total - passing with lower = passing with digits) -> 49% compliance | 51% failed.

This one required the check against three different policies because it has a disjunction: the password should have ***EITHER*** `lower` ***OR*** `digit`, but not both. 

1. So, we check that there's a 100% fail rate checking against a policy that forces the password to contain both `lower` and `digit` --- we know now that no password contains both.
2. Verify that there should be a considerable amount of passwords that contain `lower` but not `digit` --- 51% contains `lower`.
3. Lastly, ensure that the rest of the passwords contain `digit` but not `lower` --- 49% contains `digit`.

The choice to generate a password containing, in this case, `digit` or `lower` is made randomly. Thus, it is expected to see such close numbers between passwords that contain only `digit` and passwords that contain only `lower` 
