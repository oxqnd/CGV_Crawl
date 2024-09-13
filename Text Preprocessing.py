import re
import pandas as pd
from tqdm import tqdm


def text_preprocessing(text):
    # &로 시작하고 ;로 끝나는 패턴 제거
    pattern = r'&[^;\s]*;'
    cleaned_text = re.sub(pattern, '', text)

    # 숫자 제거
    cleaned_text = re.sub(r"\d+", '', cleaned_text)

    # 영어 약자 제거
    cleaned_text = re.sub(r'\b[A-Za-z]{2,}\b', '', cleaned_text)

    # 말줄임표 제거 (점이 2개 이상 이어지거나 '…' 문자가 있을 때)
    cleaned_text = re.sub(r"\.{2,}|…", '', cleaned_text)

    # 특수문자 제거
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)

    # 자음과 모음만으로 이루어진 패턴 제거 (한글 자음 범위: ㄱ-ㅎ, 모음 범위: ㅏ-ㅣ)
    cleaned_text = re.sub(r'[ㄱ-ㅎㅏ-ㅣ]+', '', cleaned_text)

    return cleaned_text


df = pd.read_csv("cgv_reviews.csv")

for idx, row in tqdm(df.iterrows(), total=df.shape[0]):
    text = row["리뷰내용"]
    text = text_preprocessing(text)

    df.at[idx, "리뷰내용"] = text

df.to_csv("preprocessed_cgv.csv", encoding="cp949", index=False)
