import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    Max_value = employee["salary"].max()
    Lower_Values_df = employee["salary"][employee["salary"] < Max_value]
    Value = Lower_Values_df.max() if not Lower_Values_df.empty else None
    return_value_dict = {"SecondHighestsalary" : [Value]}
    new_df = pd.DataFrame(return_value_dict)
    return new_df