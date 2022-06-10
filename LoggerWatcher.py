
import inspect
from functools import wraps


def inject(target_object, target_function_name, safe=False):
    if safe and not hasattr(target_object, target_function_name):
        def _self_wrap(wrap_function):
            return wrap_function

        return _self_wrap

    def _wrap_original_function(original_function, new_function):
        @wraps(original_function)
        def _wrapped_function(*args, **kwargs):
            if type(original_function) is property:
                return new_function(original_function.fget, *args, **kwargs)
            else:
                return new_function(original_function, *args, **kwargs)

        if inspect.ismethod(original_function):
            if hasattr(original_function, '__self__'):
                return _wrapped_function.__get__(original_function.__self__, original_function.__self__.__class__)

            return classmethod(_wrapped_function)
        elif type(original_function) is property:
            return property(_wrapped_function)
        else:
            return _wrapped_function

    def _injected(wrap_function):
        original_function = getattr(target_object, target_function_name)
        setattr(target_object, target_function_name, _wrap_original_function(original_function, wrap_function))

        return wrap_function

    return _injected

import sims4
logger = sims4.log.Logger('loggerwatcher', default_owner='ebimonaca')

@sims4.commands.Command('loggerwathcer', command_type=sims4.commands.CommandType.Cheat)
def loggerwathcer_start(_connection=None):
    output = sims4.commands.CheatOutput(_connection)
    output("injecting...")
    sims4.log.Logger.log = log
    sims4.log.Logger.debug = debug
    sims4.log.Logger.info = info
    sims4.log.Logger.warn = warn
    sims4.log.Logger.error = error
    @inject(sims4.log.Logger,"log")
    def inject_and_print(original, self, *args, **kwargs):
        output = sims4.commands.CheatOutput(_connection)
        #output("ログ")
        output("[L]" + "ログ：" + args[0])
        return original(self, *args, **kwargs)
    output("warn injected")

    @inject(sims4.log.Logger, "debug")
    def inject_and_print(original, self, *args, **kwargs):
        output = sims4.commands.CheatOutput(_connection)
        # output("ログ")
        output("[D]" + "ログ：" + args[0])
        return original(self, *args, **kwargs)

    output("warn injected")

    @inject(sims4.log.Logger, "info")
    def inject_and_print(original, self, *args, **kwargs):
        output = sims4.commands.CheatOutput(_connection)
        # output("ログ")
        output("[I]" + "ログ：" + args[0])
        return original(self, *args, **kwargs)

    output("warn injected")

    @inject(sims4.log.Logger, "warn")
    def inject_and_print(original, self, *args, **kwargs):
        output = sims4.commands.CheatOutput(_connection)
        # output("ログ")
        output("[W]" + "ログ：" + args[0])
        return original(self, *args, **kwargs)

    output("warn injected")

    @inject(sims4.log.Logger, "error")
    def inject_and_print(original, self, *args, **kwargs):
        output = sims4.commands.CheatOutput(_connection)
        # output("ログ")
        output("[E]" + "ログ：" + args[0])
        return original(self, *args, **kwargs)

    output("warn injected")

@sims4.commands.Command('forcewarn', command_type=sims4.commands.CommandType.Cheat)
def forcewarn(_connection=None):
    logger.warn("warn!this is test message!")



#仮
def log(self, message, *args, level, owner=None, trigger_breakpoint=False):
    abc = 0
def debug(self, message, *args, owner=None, trigger_breakpoint=False):
    abc = 0
def info(self, message, *args, owner=None, trigger_breakpoint=False):
    abc = 0
def warn(self, message, *args, owner=None, trigger_breakpoint=False):
    abc = 0
def error(self, message, *args, owner=None, trigger_breakpoint=False, trigger_callback_on_error_or_exception=True):
    abc = 0
