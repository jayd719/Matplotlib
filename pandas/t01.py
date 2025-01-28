import pandas as pd
import numpy as np

s = pd.Series(list(range(20, 31)))
print(type(s))
print(s)

dates = pd.date_range("20220101", periods=10, freq="d")
print(type(dates))
print(dates)

COLS = ["n", "j", "s"]
df = pd.DataFrame(np.random.randn(len(dates), len(COLS)), index=dates, columns=COLS)
print(type(df))
print(df)
