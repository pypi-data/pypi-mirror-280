"""
This is an example of a CLI script. It demonstrates what is passed to the script in the
4 positional arguments of the process() function.

Example usage:

  praetorian chariot list seeds --script hello-world

"""

def process(controller, cmd, cli_kwargs, output):
    print('Entering the process() function. It received 4 positional arguments. Inspecting them:\n')

    # Inspect the controller object. Here, we print the username in the
    # keychain.ini file.
    print(f'username = {controller.keychain.username}.\n')

    # Inspect the command that is issued to the CLI. It is organized in
    # 'product': which Praetorian product?
    # 'action': which action, e.g., 'get', 'list', 'update', etc?
    # 'type': which type of objects is it operating on?
    print(f'cmd = {cmd}.\n')

    # Inspect further arguments supplied to the CLI. It is organized in
    # a keyword argument dictionary. These are the options suuplied to
    # the CLI command, such as '--details', '--term', '--page all', etc.
    print(f'cli_kwargs = {cli_kwargs}.\n')

    # Inspect the output of the CLI command. This is the output this function
    # receives and processes
    print('output =')
    print(output)

    print('\nExiting the process() function')
