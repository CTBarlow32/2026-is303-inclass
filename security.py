from ipaddress import ip_address

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Repos/Module 6/security_log.csv")

#1
#failed attempts
#percentage of failures
failures = df[df["status"] == "failed"]
print(len(failures))
print(f"{len(failures)/len(df)*100}%")

#2
#username with most failed attempts
#how many fails does that user have
print(failures.groupby("username")["attempts"].sum().idxmax())
print(failures.groupby("username")["attempts"].sum().max())

#3
#ip address with most failures
#what country is the ip from
print(failures.groupby("ip_address")["attempts"].sum().idxmax())

