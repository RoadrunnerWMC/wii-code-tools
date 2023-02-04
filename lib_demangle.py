import lib_demangle_correct
import lib_demangle_nvidia


def demangle(sym: str, *, nvidia: bool = False) -> str:
    """
    Demangle a symbol using either Nvidia's broken algorithm, or a
    correct algorithm.
    """
    if nvidia:
        return lib_demangle_nvidia.demangle(sym)
    else:
        return lib_demangle_correct.demangle(sym)
