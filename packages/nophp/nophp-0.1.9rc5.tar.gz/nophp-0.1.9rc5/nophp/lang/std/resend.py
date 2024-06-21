import resend
from ..exceptions import TranspilerExceptions, Warn
from ..module import Module
from ..types import *

class CommonResendMod(Module):
    name="COMMONRESEND"
    type = Module.MODULE_TYPES.FUNCTION

    def __init__(self, compiler_instance):
        super().__init__()
        self.compiler_instance = compiler_instance

    def base(self, tree, ref=False):
        values = []

        if 'FUNCTION_ARGUMENTS' not in tree:
            # Advanced handling
            for var in tree:
                value = self.ref_resolve(var) if ref else self.safely_resolve(var)
                values.append(value)
        else:
            if 'POSITIONAL_ARGS' in tree['FUNCTION_ARGUMENTS']:
                for var in tree['FUNCTION_ARGUMENTS']['POSITIONAL_ARGS']:

                    value = self.ref_resolve(var) if ref else self.safely_resolve(var)

                    values.append(value)

        return values


# resend_set_key($value) -> Bool
class SetSecretMod(CommonResendMod):
    name="resend_set_key"
    type = Module.MODULE_TYPES.FUNCTION

    def __init__(self, compiler_instance):
        super().__init__(compiler_instance)
        self.compiler_instance = compiler_instance

    def proc_tree(self, tree):
        values = self.base(tree)

        key = values[0]

        resend.api_key = key

        return Bool(True)
    
class ResendSendMod(CommonResendMod):
    name="resend"
    type = Module.MODULE_TYPES.FUNCTION

    def __init__(self, compiler_instance):
        super().__init__(compiler_instance)
        self.compiler_instance = compiler_instance

    def proc_tree(self, tree):
        values = self.base(tree)

        items = values[0]

        try:
            r = resend.Emails.send(items)
        except Exception as e:
            return String(f"Failed due to {e}")
    
_MODS = {
    "resend_set_key": SetSecretMod,
    "resend": ResendSendMod
}

def build_funcs(c):
    functions = {}
    for f in _MODS:
        functions[f] = {
                "run_func": _MODS[f](c)
            }
    return functions