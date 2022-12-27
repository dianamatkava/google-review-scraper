import xlsxwriter
import pandas as pd

def generate_xls(google_reviews):
    if google_reviews.reviews:
        writer = pd.ExcelWriter('reviews.xlsx', engine='xlsxwriter')
        df_data = dict()
        {
            df_data.update(
                {id: google_reviews.reviews[id].raw_review}
            ) for id in range(len(google_reviews.reviews))
        }
        df = pd.DataFrame.from_dict(df_data, orient='index')
        df.to_excel(writer, sheet_name='Review data')
        writer.close()


