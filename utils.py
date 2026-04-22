import pandas as pd
from config import USERS_PATH


def load_users():
    df = pd.read_csv(USERS_PATH)

    # Ensure required columns exist
    required_cols = {
        "old_password": "",
        "role": "user",
        "status": "active",
        "failed_login_count": 0,
        "locked": 0,
        "created_at": ""
    }

    for col, default_val in required_cols.items():
        if col not in df.columns:
            df[col] = default_val

    # Clean text columns
    df["username"] = df["username"].astype(str).str.strip()
    df["password"] = df["password"].astype(str).str.strip()
    df["old_password"] = df["old_password"].astype(str).str.strip()
    df["status"] = df["status"].astype(str).str.strip()
    df["role"] = df["role"].astype(str).str.strip()

    # Numeric columns
    df["failed_login_count"] = pd.to_numeric(
        df["failed_login_count"],
        errors="coerce"
    ).fillna(0).astype(int)

    df["locked"] = pd.to_numeric(
        df["locked"],
        errors="coerce"
    ).fillna(0).astype(int)

    return df


def save_users(df):
    df.to_csv(USERS_PATH, index=False)


def username_exists(username):
    username = str(username).strip()

    if username == "":
        return False

    df = load_users()
    return username in df["username"].values


def get_user(username):
    username = str(username).strip()

    df = load_users()

    row = df[df["username"] == username]

    if len(row) == 0:
        return None

    return row.iloc[0]


def reset_users():
    df = load_users()

    for i in range(len(df)):

        user = str(df.loc[i, "username"]).strip()

        if user.lower() == "admin":
            df.loc[i, "password"] = "Admin@123"
        else:
            df.loc[i, "password"] = "Cust@" + user[:4]

        df.loc[i, "old_password"] = ""
        df.loc[i, "status"] = "active"
        df.loc[i, "locked"] = 0
        df.loc[i, "failed_login_count"] = 0

    save_users(df)
