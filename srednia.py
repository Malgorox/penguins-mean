import pandas as pd

df = pd.read_csv("penguins.csv")
Srednie = df.groupby("species")[["body_mass_g","flipper_length_mm"]].mean()
Srednie.to_csv("wynik.csv")