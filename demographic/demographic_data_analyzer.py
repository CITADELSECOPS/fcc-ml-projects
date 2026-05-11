"""FCC Data Analysis #2 — Demographic Data Analyzer (adult.data.csv)."""
import pandas as pd


def calculate_demographic_data(print_data=False):
    df = pd.read_csv("adult.data.csv")
    race_count = df["race"].value_counts()
    average_age_men = round(df.loc[df["sex"] == "Male", "age"].mean(), 1)
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    higher_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    higher_education_rich = round(
        (df.loc[higher_education, "salary"] == ">50K").mean() * 100, 1
    )
    lower_education_rich = round(
        (df.loc[~higher_education, "salary"] == ">50K").mean() * 100, 1
    )
    min_work_hours = df["hours-per-week"].min()
    min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round((min_workers["salary"] == ">50K").mean() * 100, 1)

    by_country = df.groupby("native-country")["salary"].apply(
        lambda s: (s == ">50K").mean() * 100
    )
    highest_earning_country = by_country.idxmax()
    highest_earning_country_percentage = round(by_country.max(), 1)

    top_IN_occupation = df.loc[
        (df["native-country"] == "India") & (df["salary"] == ">50K"), "occupation"
    ].value_counts().idxmax()

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
