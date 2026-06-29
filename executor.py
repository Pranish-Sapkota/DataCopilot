import io
import sys
import traceback
import contextlib

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


SAFE_BUILTINS = {
    "print": print, "len": len, "range": range, "enumerate": enumerate,
    "zip": zip, "list": list, "dict": dict, "set": set, "tuple": tuple,
    "sorted": sorted, "sum": sum, "min": min, "max": max, "abs": abs,
    "round": round, "int": int, "float": float, "str": str, "bool": bool,
    "isinstance": isinstance, "type": type, "hasattr": hasattr,
    "getattr": getattr, "True": True, "False": False, "None": None,
    "Exception": Exception, "ValueError": ValueError,
    "KeyError": KeyError, "TypeError": TypeError,
}

SAFE_GLOBALS = {
    "pd": pd, "plt": plt, "sns": sns, "np": np,
    "__builtins__": SAFE_BUILTINS,
}


def execute_analysis(code, df, chart_path):
    stdout_capture = io.StringIO()
    error_msg = ""
    local_vars = {"df": df.copy(), "chart_path": chart_path}

    try:
        with contextlib.redirect_stdout(stdout_capture):
            exec(code, dict(SAFE_GLOBALS), local_vars)
    except Exception:
        error_msg = traceback.format_exc(limit=5)
    finally:
        plt.close("all")

    return {"output": stdout_capture.getvalue(), "error": error_msg}
