def validate_records(df):
    return df.dropna().filter("patient_id IS NOT NULL")
