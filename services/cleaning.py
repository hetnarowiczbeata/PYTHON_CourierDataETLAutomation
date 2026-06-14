def clean_data(df):
    df = df.drop(columns=[
        'Pouch No',

        'Sender Phone',
        'Sender Address',
        'Sender City',
        'Sender State',
        'Sender Pincode',
        'Sender GSTIN',

        'Paperwork',
        'Sender Signature',
        'Sender Date',

        'Recipient Phone',
        'Recipient Address',
        'Recipient City',
        'Receiver State',
        'Receiver Pincode',

        'Description',
        'Value Added Services',

        'Booking Code',
        'Recipient GSTIN',

        'Receiver Name',
        'Relationship',
        'Company Stamp',
        'Receiver Signature',

        'Expiry Date'
    ])

    text_cols=['Origin','Destination',]
    for col in text_cols:
        df[col]=df[col].str.strip().str.title().fillna('Unknown')
    return df

    
