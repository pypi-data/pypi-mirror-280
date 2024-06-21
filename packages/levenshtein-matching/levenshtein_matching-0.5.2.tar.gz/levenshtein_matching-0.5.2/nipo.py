from levenshtein_string_matching import find_best_match_levenshtein
import pandas as pd
from sqlalchemy import create_engine 
from dotenv import load_dotenv
from typing import Optional
import os
from datetime import datetime
import time
from sqlalchemy import text
from tqdm import tqdm
from fuzzywuzzy import fuzz
import sys
from loguru import logger


def load_dataframe_from_db() -> pd.DataFrame:
    conn = get_connection()
    data = pd.read_sql("SELECT * FROM nipo", conn)
    return data

def load_total_orgs() -> pd.DataFrame:
    conn = get_connection()
    companies = pd.read_sql("SELECT org_nr, org_name FROM company", conn)
    return companies

def get_connection():
    ### DB
    dbname="nysno"
    user="sa" 
    password=os.getenv('DB_PASSWORD') 
    host="localhost"
    port="5432"
    connection_string = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
    db = create_engine(connection_string) 
    conn = db.connect() 
    return conn

def clean_df(patent_df: pd.DataFrame, col_drop: Optional[list] = None, col_keep: Optional[list] = None) -> pd.DataFrame:
    filtered_df = patent_df.copy()
    if col_drop is not None:
        filtered_df = filtered_df.drop(columns=col_drop)
    if col_keep is not None:
        filtered_df = filtered_df[col_keep]

    filtered_df['soker'] = filtered_df['soker'].str.split(',')
    
    filtered_df = filtered_df.explode('soker')
    
    return filtered_df

def summerize_df(filtered_df: pd.DataFrame) -> pd.DataFrame:
    summerized_df = filtered_df.groupby('soker').agg({
            'leveringsdato': lambda x: list(x),
            'patent_status': lambda x: list(x)
        }).reset_index()
    return summerized_df

def count(filtered_df: pd.DataFrame) -> pd.DataFrame:
    count_df = filtered_df.explode('leveringsdato').groupby('soker').size().reset_index(name='count')
    filtered_df = filtered_df.merge(count_df, on='soker', how='left')
    
    return filtered_df

def calculate_score(row):
    scores = []
    current_date = datetime.now()
    for date, status in zip(row['leveringsdato'], row['patent_status']):
        age_in_years = (current_date - date).days / 365.25 if isinstance(date, datetime) else (current_date - datetime.combine(date, datetime.min.time())).days / 365.25

        if 'Meddelt' in status:
            status_score = 1
        elif 'Under behandling' in status:
            status_score = 0.5
        else:
            status_score = 0
        if age_in_years > 0:
            score=status_score*10 / age_in_years
            scores.append(score)
        else:
            score=0
            scores.append(score)
    return sum(scores)

def merge_tables(df_org: pd.DataFrame, df_score: pd.DataFrame):
    """give the companies with score a score in the total org_nr table
    the rest get 0 score"""
    merged = df_org.merge(df_score, "left", on='org_nr')
    merged = merged.fillna(0)
    merged = merged.sort_values('nipo_score', ascending=False)
    merged.drop
    return merged

def matching_in_rust(patent_df: pd.DataFrame, companies: pd.DataFrame, threshold=0.9) -> pd.DataFrame:
    patent_soker = patent_df['soker']
    patent_score = patent_df['score']
    company_names = companies["org_name"]
    org_nr = companies['org_nr']
    match_org_nr, match_score = find_best_match_levenshtein(list(zip(company_names, org_nr)), list(zip(patent_soker, patent_score)), threshold)
    logger.info(f"Number of matches: {len(match_org_nr)}")
    return pd.DataFrame({
        "org_nr" : match_org_nr,
        "score" : match_score
    })

def matching_in_python(patent_df: pd.DataFrame, companies: pd.DataFrame, threshold=0.9) -> pd.DataFrame:
    patent_soker = patent_df['soker']
    best_matches = []
    # tqdm formatter for getting colored bar, and text.
    # Sourced from: https://stackoverflow.com/questions/65269314/how-to-change-text-color-from-a-python-module-tqdm-module-output-so-not-pyt
    read_bar_format = "%s{l_bar}%s{bar}%s{r_bar}" % (
                "\033[0;32m", "\033[0;32m", "\033[0;32m"
            )
    for soker in tqdm(patent_soker, desc="Processing Søkers", bar_format=read_bar_format):
        best_score = 0
        best_match = None
        for _, row in companies.iterrows():
            org_name = row['org_name']
            org_nr = row['org_nr']
            max_score = fuzz.ratio(soker, org_name)            
            if max_score == 100:
                best_match = (soker, org_nr, org_name, max_score)
                break  # End the loop if a perfect match is found
            if max_score > best_score:
                best_score = max_score
                best_match = (soker, org_nr, org_name, best_score)

        if best_match and best_match[-1] >= threshold:
            best_matches.append(best_match)
    logger.info(f"Number of matches: {len(best_matches)}")
    matches_df = pd.DataFrame(best_matches, columns=['soker', 'org_nr', 'matched_name', 'match_score'])
    patent_df = pd.merge(patent_df, matches_df, on='soker', how='left')

    return patent_df

def update_scoring_db(df: pd.DataFrame) -> None:
    conn = get_connection()
    try:
        with conn.begin() as transaction:
            # tqdm formatter for getting colored bar, and text.
            # Sourced from: https://stackoverflow.com/questions/65269314/how-to-change-text-color-from-a-python-module-tqdm-module-output-so-not-pyt
            read_bar_format = "%s{l_bar}%s{bar}%s{r_bar}" % (
                "\033[0;32m", "\033[0;32m", "\033[0;32m"
            )
            for _, row in tqdm(df.iterrows(), total=df.shape[0], desc="Saving scores to database", bar_format=read_bar_format):
                org_nr = row['org_nr']
                score = row['score']
                update_query = text("""
                    UPDATE score
                    SET nipo_score = :score
                    WHERE org_nr = :org_nr
                """)
                conn.execute(update_query, {'score': score, 'org_nr': org_nr})
        print("")
        logger.info("Updated nipo scores")
    except Exception as e:
        logger.info(f"Error occurred: {e}")
        transaction.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    ### SETUP ###
    start_time = time.time()
    logger.remove()
    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD at HH:mm:ss} |{level}| {message}</green> ",
        level="INFO"
    )
    is_native = len(sys.argv) == 2 and sys.argv[1] == "native"
    if is_native:
        logger.info("Running With Native Python")
    else:
        logger.info("Running With Rust Library")
    load_dotenv()
    patents = load_dataframe_from_db()
    patents = clean_df(patents, col_drop=['soknads_nr', 'tittel', 'fullmektig', 'innehaver'])
    patents = summerize_df(patents)
    patents = count(patents)
    patents['score'] = patents.apply(calculate_score, axis=1)
    patents['leveringsdato'] = patents['leveringsdato'].apply(lambda dates: [date.strftime('%d.%m.%Y') for date in dates])


    companies = load_total_orgs()
    logger.info(f"Matching {patents['soker'].count()} patents, and {companies['org_name'].count()} companies")
    if is_native:
        matched = matching_in_python(patents, companies)
        update_scoring_db(matched)
        elapsed_time = time.time() - start_time
        logger.info(f"Python time elapsed: {round(elapsed_time, 2)} seconds")
    else:
        matched = matching_in_rust(patents, companies)
        update_scoring_db(matched)
        elapsed_time = time.time() - start_time
        logger.info(f"Rust library time elapsed: {round(elapsed_time, 2)} seconds")