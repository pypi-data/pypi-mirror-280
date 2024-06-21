import qrcode
import qrcode.image.svg

from ..exceptions import TranspilerExceptions, Warn
from ..module import Module
from ..types import *

class CommonQRCodeMod(Module):
    name="COMMONQR"
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

    
class QrSVGMod(CommonQRCodeMod):
    name="qr_svg"
    type = Module.MODULE_TYPES.FUNCTION

    def __init__(self, compiler_instance):
        super().__init__(compiler_instance)
        self.compiler_instance = compiler_instance

    def proc_tree(self, tree):
        values = self.base(tree)

        data = values[0]

        img = qrcode.make(data, image_factory=qrcode.image.svg.SvgPathImage)

        return String(img.to_string(encoding='unicode'))

    
_MODS = {
    "qr_svg": QrSVGMod
}

def build_funcs(c):
    functions = {}
    for f in _MODS:
        functions[f] = {
                "run_func": _MODS[f](c)
            }
    return functions