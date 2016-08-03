from tests.LocalBearTestHelper import verify_local_bear


# Sample code, replace with your own test code.

good_file = """
I wrote something with coala.
""".splitlines(keepends=True)


bad_file = """
Here I used Coala wrong.
""".splitlines(keepends=True)


# Add more test methods with settings and/or configuration files.
# Writing Tests documentation available at:
# http://coala.readthedocs.io/en/latest/Users/Tutorials/Testing_Bears.html

coalaCheckBearTest =verify_local_bear(
    coalaCheckBear,
    valid_files=(good_file,),
    invalid_files=(bad_file),)
