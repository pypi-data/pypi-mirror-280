import sys

class Args:
    def __init__(self):
        self.arguments = {}
        self.no_args_function = None
        self.help_messages = {}  # Diccionario para almacenar los mensajes de ayuda

    def arg(self, names, help=None):
        def decorator(func):
            for name in names:
                self.arguments[name] = func
                if help:
                    self.help_messages[name] = help  # Almacenar el mensaje de ayuda
            return func
        return decorator

    def haveArgs(self, func):
        self.no_args_function = func
        return func

    def parse_args(self):
        cargs = sys.argv[1:]  # Get all arguments except the script name

        if not cargs and self.no_args_function:
            self.no_args_function()
            return

        decorated_args = set(arg for arg in self.arguments.keys())

        i = 0
        while i < len(cargs):
            arg_name = cargs[i]

            if arg_name in decorated_args:
                func = self.arguments[arg_name]
                arg_values = []

                i += 1  # Move to the next argument value

                while i < len(cargs) and cargs[i] not in decorated_args:
                    arg_values.append(cargs[i])
                    i += 1

                func(*arg_values)
            else:
                print("Unknown argument:", arg_name)
                i += 1

    def display_help(self, ljust = 20):
        print("Available arguments:")
        for arg, help_text in self.help_messages.items():
            print(f"{arg.ljust(20)} - {help_text}")
    
    def iterHelp(self, ljust = 20):
        for arg, help_text in self.help_messages.items():
            yield f"{arg.ljust(20)} - {help_text}"
