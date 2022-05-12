import pandas as pd
import numpy as np
import streamlit as st

FILE_PATH_TRAIN = 'https://raw.githubusercontent.com/jay619/Kaggle-Competitions/main/1-Titanic/titanic/train.csv'
FILE_PATH_TEST = 'https://raw.githubusercontent.com/jay619/Kaggle-Competitions/main/1-Titanic/titanic/train.csv'


def main():


    @st.cache
    def load_data():
        train_data = pd.read_csv(FILE_PATH_TRAIN)
        test_data = pd.read_csv(FILE_PATH_TEST)
        return train_data, test_data

    @st.cache
    def single_variable_eda(data):
        pass

    st.title("Titanic - Machine Learning from disaster")
    train, test = load_data()

    st.sidebar.header("Model Selection & Settings")
    view_raw_data = st.sidebar.checkbox(label="View raw data", key="view_raw_data")

    if view_raw_data:
        st.dataframe(train)

    eda = st.sidebar.selectbox(label="EDA", options=["Single Variable", "Pairwise", "Correlation Matrix"], key="eda")

    if eda == "Single Variable":
        variables = st.sidebar.multiselect("Variables", options=train.columns, key="vars")
        single_variable_eda(variables)


if __name__ == '__main__':
    main()
