import pandas as pd
import numpy as np
data={"Maths":[50,49,48,47],"Science":[49,48,47,46],"History":[48,47,46,45],"English":[47,46,45,44]}
student=pd.DataFrame(data)
student.index=["adhil","akash","ajay","agash"]
print(student)
maths=np.mean(student["Maths"])
print(maths)
science=np.mean(student["Science"])
print(science)
history=np.mean(student["History"])
print(history)
english=np.mean(student["English"])
print(english)
if maths>science:
    if maths>history:
        if maths>english:
            print("The Maths has the highest average of ",maths)
if science>maths:
    if science>history:
        if science>english:
            print("The Science has the highest average of ",science)
arr=student.to_numpy()
arr.shape=(4,4)
print(arr)

