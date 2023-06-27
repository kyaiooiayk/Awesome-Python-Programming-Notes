import os
import pickle
import typer
import numpy as np
import pandas as pd
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy import text

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import KNNImputer
from sklearn.metrics import confusion_matrix


RARE_TITLES = {
    "Capt",
    "Col",
    "Don",
    "Dona",
    "Dr",
    "Jonkheer",
    "Lady",
    "Major",
    "Mlle",
    "Mme",
    "Ms",
    "Rev",
    "Sir",
    "the Countess",
}


class Passenger(BaseModel):
    pid: int
    pclass: int
    sex: str
    age: float
    family_size: int
    fare: float
    embarked: str
    is_alone: int
    title: str
    is_survived: int


def do_test(filename, data):
    if not os.path.isfile(filename):
        pickle.dump(data, open(filename, "wb"))
    truth = pickle.load(open(filename, "rb"))
    try:
        np.testing.assert_almost_equal(data, truth)
        print(f"{filename} test passed")
    except AssertionError as ex:
        print(f"{filename} test failed {ex}")


def do_pandas_test(filename, data):
    if not os.path.isfile(filename):
        data.to_pickle(filename)
    truth = pd.read_pickle(filename)
    try:
        pd.testing.assert_frame_equal(data, truth)
        print(f"{filename} pandas test passed")
    except AssertionError as ex:
        print(f"{filename} pandas test failed {ex}")


class SqlLoader:
    def __init__(self, connection_string):
        engine = create_engine(connection_string)
        self.connection = engine.connect()

    def get_passengers(self):
        query = text(
            """
            SELECT
                tbl_passengers.pid,
                tbl_passengers.pclass,
                tbl_passengers.sex,
                tbl_passengers.age,
                tbl_passengers.parch,
                tbl_passengers.sibsp,
                tbl_passengers.fare,
                tbl_passengers.embarked,
                tbl_passengers.name,
                tbl_targets.is_survived
            FROM
                tbl_passengers
            JOIN
                tbl_targets
            ON
                tbl_passengers.pid=tbl_targets.pid
        """
        )
        return pd.read_sql(query, con=self.connection)


class TestLoader:
    def __init__(self, passengers_filename, real_loader):
        self.passengers_filename = passengers_filename
        self.real_loader = real_loader
        if not os.path.isfile(self.passengers_filename):
            df = self.real_loader.get_passengers()
            df.to_pickle(self.passengers_filename)

    def get_passengers(self):
        return pd.read_pickle(self.passengers_filename)


class PassengerLoader:
    def __init__(self, loader, rare_titles=None):
        self.loader = loader
        self.rare_titles = rare_titles

    def get_passengers(self):
        passengers = []
        for data in self.loader.get_passengers().itertuples():
            # parch = Parents/Children, sibsp = Siblings/Spouses
            family_size = int(data.parch + data.sibsp)
            # Allen, Miss. Elisabeth Walton
            title = data.name.split(",")[1].split(".")[0].strip()
            passenger = Passenger(
                pid=int(data.pid),
                pclass=int(data.pclass),
                sex=str(data.sex),
                age=float(data.age),
                family_size=family_size,
                fare=float(data.fare),
                embarked=str(data.embarked),
                is_alone=1 if family_size == 1 else 0,
                title="rare" if title in self.rare_titles else title,
                is_survived=int(data.is_survived),
            )
            passengers.append(passenger)
        return passengers


class TitanicModel:
    def __init__(self):
        self.one_hot_encoder = OneHotEncoder(
            handle_unknown="ignore", sparse_output=False
        )
        self.knn_imputer = KNNImputer(n_neighbors=5)
        self.robust_scaler = RobustScaler()
        self.predictor = LogisticRegression(random_state=0)

    def train(self):
        pass

    def estimate(self, passengers):
        return 1


class TitanicModelCreator:
    def __init__(self, loader):
        self.loader = loader
        np.random.seed(42)

    def run(self):
        df = pd.DataFrame([v.dict() for v in self.loader.get_passengers()])
        targets = [int(v) for v in df["is_survived"]]

        X_train, X_test, y_train, y_test = train_test_split(
            df, targets, stratify=targets, test_size=0.2
        )

        # --- TRAINING ---
        model = TitanicModel()

        X_train_categorical = X_train[
            ["embarked", "sex", "pclass", "title", "is_alone"]
        ]

        model.one_hot_encoder.fit(X_train_categorical)
        X_train_categorical_one_hot = model.one_hot_encoder.transform(
            X_train_categorical
        )

        X_train_numerical = X_train[["age", "fare", "family_size"]]
        model.knn_imputer.fit(X_train_numerical)
        X_train_numerical_imputed = model.knn_imputer.transform(X_train_numerical)

        model.robust_scaler.fit(X_train_numerical_imputed)
        X_train_numerical_imputed_scaled = model.robust_scaler.transform(
            X_train_numerical_imputed
        )

        X_train_processed = np.hstack(
            (X_train_categorical_one_hot, X_train_numerical_imputed_scaled)
        )

        model.predictor.fit(X_train_processed, y_train)
        y_train_estimation = model.predictor.predict(X_train_processed)

        cm_train = confusion_matrix(y_train, y_train_estimation)

        # --- TESTING ---
        X_test_categorical = X_test[["embarked", "sex", "pclass", "title", "is_alone"]]
        X_test_categorical_one_hot = model.one_hot_encoder.transform(X_test_categorical)

        X_test_numerical = X_test[["age", "fare", "family_size"]]
        X_test_numerical_imputed = model.knn_imputer.transform(X_test_numerical)
        X_test_numerical_imputed_scaled = model.robust_scaler.transform(
            X_test_numerical_imputed
        )

        X_test_processed = np.hstack(
            (X_test_categorical_one_hot, X_test_numerical_imputed_scaled)
        )

        y_test_estimation = model.predictor.predict(X_test_processed)
        cm_test = confusion_matrix(y_test, y_test_estimation)

        print("cm_train", cm_train)
        print("cm_test", cm_test)

        do_test("../data/cm_test.pkl", cm_test)
        do_test("../data/cm_train.pkl", cm_train)
        do_test("../data/X_train_processed.pkl", X_train_processed)
        do_test("../data/X_test_processed.pkl", X_test_processed)

        ("../data/df_no_tickets.pkl", df)


def main(param: str = "pass"):
    titanic_model_creator = TitanicModelCreator(
        loader=PassengerLoader(
            loader=SqlLoader(connection_string="sqlite:///../data/titanic.db"),
            rare_titles=RARE_TITLES,
        )
    )
    titanic_model_creator.run()


def test_main(param: str = "pass"):
    titanic_model_creator = TitanicModelCreator(
        loader=PassengerLoader(
            loader=TestLoader(
                passengers_filename="../data/passengers_with_is_survived.pkl",
                real_loader=SqlLoader(connection_string="sqlite:///../data/titanic.db"),
            ),
            rare_titles=RARE_TITLES,
        )
    )
    titanic_model_creator.run()


if __name__ == "__main__":
    typer.run(test_main)
