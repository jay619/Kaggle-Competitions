import pandas as pd
import streamlit as st

FILE_PATH_TRAIN = 'https://raw.githubusercontent.com/jay619/Kaggle-Competitions/main/1-Titanic/titanic/train.csv'
FILE_PATH_TEST = 'https://raw.githubusercontent.com/jay619/Kaggle-Competitions/main/1-Titanic/titanic/train.csv'


def main():
    @st.cache(persist=True)
    def load_data():
        train_data = pd.read_csv(FILE_PATH_TRAIN)
        test_data = pd.read_csv(FILE_PATH_TEST)
        return train_data, test_data

    def plot_bar_chart(data, category, show_frequency=False):
        width = 1 / 1.5
        counts = data[category].value_counts(normalize=show_frequency).sort_index()
        # p = figure(
        #     x_range=list(map(str, counts.index.to_list())),
        #     title=f"Distribution of {category}",
        #     x_axis_label=f"{category}",
        #     y_axis_label="Frequency")
        # p.vbar(x=counts.index.tolist(), top=counts, width=0.5)
        # st.bokeh_chart(p, use_container_width=True)
        st.bar_chart(data=counts, use_container_width=True)

    def single_variable_eda(variables):
        """
        :type variables: list
        """
        col1, col2, col3 = st.columns(3)
        for var in variables:
            with col1:
                # if var == "PassengerId":
                #     st.subheader(var)
                #     st.write("Passenger ID doesn't provide much useful information and will not be used in EDA or "
                #              "modeling")

                if var == "Pclass":
                    st.subheader(var)
                    st.write("Missing Values: {}".format(train[var].isna().sum()))
                    plot_bar_chart(train, var, True)

                if var == "SibSp":
                    st.subheader(var)
                    st.write("Missing Values: {}".format(train[var].isna().sum()))
                    plot_bar_chart(train, var, True)

            with col2:
                if var == "Survived":
                    st.subheader(var)
                    st.write("Missing values: {}".format(train[var].isna().sum()))
                    plot_bar_chart(train, var, show_frequency=True)

                if var == "Parch":
                    st.subheader(var)
                    st.write("Missing Values: {}".format(train[var].isna().sum()))
                    plot_bar_chart(train, var, True)

            with col3:
                if var == "Sex":
                    st.subheader(var)
                    st.write("Missing values: {}".format(train[var].isna().sum()))
                    plot_bar_chart(train, var, show_frequency=True)

    st.title("Titanic - Machine Learning from disaster")
    train, test = load_data()

    st.sidebar.header("Options")
    view_raw_data = st.sidebar.checkbox(label="View raw data", key="view_raw_data")

    if view_raw_data:
        st.dataframe(train)

    options = st.sidebar.selectbox(label="EDA",
                                   options=["Single Variable", "Pairwise", "Correlation Matrix", "Modeling"],
                                   key="options")

    if options == "Single Variable":
        variables = st.sidebar.multiselect("Variables", options=train.columns, key="vars")
        single_variable_eda(variables)

    if options == "Modeling":
        model = st.sidebar.selectbox(label="Choose Model",
                                     options=["Logistic Regression", "Random Forest", "Bayes Classifier"],
                                     key="model")
        st.sidebar.subheader("Model Parameters")
        st.sidebar.button(label="Classify", key="classify")

        if model == "Logistic Regression":
            pass

        if model == "Random Forest":
            pass

        if model == "Bayes Classifier":
            pass


if __name__ == '__main__':
    main()
