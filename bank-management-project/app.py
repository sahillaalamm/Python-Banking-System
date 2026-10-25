import json
import secrets
import string
import hashlib
import hmac
from pathlib import Path
from datetime import datetime

import streamlit as st

# -------------------- Configuration --------------------
DATA_FILE = Path(__file__).with_name("data.json")
MAX_DEPOSIT = 10_000
PIN_LENGTH = 4


# -------------------- Storage helpers --------------------
def load_accounts():
    """Load accounts from JSON. Create an empty database if it doesn't exist."""
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]", encoding="utf-8")
        return []

    try:
        content = DATA_FILE.read_text(encoding="utf-8").strip()
        if not content:
            return []
        accounts = json.loads(content)
        if not isinstance(accounts, list):
            raise ValueError("The database must contain a JSON list.")
        return accounts
    except (json.JSONDecodeError, OSError, ValueError) as exc:
        st.error(f"Could not read the account database: {exc}")
        return []


def save_accounts(accounts):
    """Write JSON atomically to reduce the risk of a partially written file."""
    temp_file = DATA_FILE.with_suffix(".tmp")
    temp_file.write_text(json.dumps(accounts, indent=2), encoding="utf-8")
    temp_file.replace(DATA_FILE)


def hash_pin(pin):
    """Hash a PIN before saving it. This is still a demo, not production banking security."""
    return hashlib.sha256(pin.encode("utf-8")).hexdigest()


def verify_pin(account, pin):
    saved_pin = account.get("pin_hash")
    # Support older records that may still contain a plain-text 'pin'.
    if saved_pin:
        return hmac.compare_digest(saved_pin, hash_pin(pin))
    old_pin = str(account.get("pin", ""))
    return hmac.compare_digest(old_pin, pin)


def generate_account_number(accounts):
    """Generate a unique 10-digit account number."""
    existing = {str(account.get("account_number", "")) for account in accounts}
    while True:
        number = "".join(secrets.choice(string.digits) for _ in range(10))
        if number not in existing:
            return number


def find_account(accounts, account_number, pin):
    for account in accounts:
        if str(account.get("account_number", "")) == account_number and verify_pin(account, pin):
            return account
    return None


def money(value):
    return f"₹{value:,.2f}"


def validate_pin(pin):
    return len(pin) == PIN_LENGTH and pin.isdigit()


# -------------------- Streamlit UI --------------------
st.set_page_config(page_title="Simple Bank", page_icon="🏦", layout="centered")

st.title("🏦 Welcome to Streamlit Bank")
st.caption("A beginner-friendly banking project built with Python, JSON, and Streamlit.")
st.warning(
    "Demo only: this app stores data in a local JSON file. It is not suitable for real money, "
    "real customer information, or production banking. Use a database and stronger authentication "
    "before deploying."
)

accounts = load_accounts()

page = st.sidebar.radio(
    "Choose an action",
    [
        "Create account",
        "Deposit money",
        "Withdraw money",
        "View account",
        "Update details",
        "Delete account",
    ],
)

if page == "Create account":
    st.header("Create a new account")
    with st.form("create_account_form"):
        name = st.text_input("Full name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        email = st.text_input("Email address")
        pin = st.text_input("Create a 4-digit PIN", type="password", max_chars=4)
        confirm_pin = st.text_input("Confirm PIN", type="password", max_chars=4)
        submitted = st.form_submit_button("Create account", type="primary")

    if submitted:
        if not name.strip():
            st.error("Please enter your name.")
        elif age < 18:
            st.error("You must be at least 18 years old to create an account.")
        elif not email.strip() or "@" not in email or "." not in email.split("@")[-1]:
            st.error("Please enter a valid email address.")
        elif not validate_pin(pin):
            st.error("PIN must contain exactly 4 digits.")
        elif pin != confirm_pin:
            st.error("The PINs do not match.")
        elif any(a.get("email", "").lower() == email.strip().lower() for a in accounts):
            st.error("An account with this email address already exists.")
        else:
            account = {
                "name": name.strip(),
                "age": int(age),
                "email": email.strip(),
                "pin_hash": hash_pin(pin),
                "account_number": generate_account_number(accounts),
                "balance": 0.0,
                "created_at": datetime.now().isoformat(timespec="seconds"),
            }
            accounts.append(account)
            save_accounts(accounts)
            st.success("Account created successfully!")
            st.info(f"Your account number is **{account['account_number']}**. Save it securely.")
            st.metric("Opening balance", money(0))

elif page in ("Deposit money", "Withdraw money"):
    is_deposit = page == "Deposit money"
    st.header("Deposit money" if is_deposit else "Withdraw money")
    with st.form("transaction_form"):
        account_number = st.text_input("Account number")
        pin = st.text_input("4-digit PIN", type="password", max_chars=4)
        amount = st.number_input(
            "Amount (₹)",
            min_value=0.0,
            max_value=1_000_000.0,
            value=100.0,
            step=100.0,
        )
        submitted = st.form_submit_button("Deposit" if is_deposit else "Withdraw", type="primary")

    if submitted:
        account = find_account(accounts, account_number.strip(), pin)
        if not account:
            st.error("Account number or PIN is incorrect.")
        elif amount <= 0:
            st.error("Amount must be greater than ₹0.")
        elif is_deposit and amount > MAX_DEPOSIT:
            st.error(f"For this demo, each deposit must be ₹{MAX_DEPOSIT:,} or less.")
        elif not is_deposit and amount > float(account.get("balance", 0)):
            st.error("Insufficient balance.")
        else:
            if is_deposit:
                account["balance"] = round(float(account.get("balance", 0)) + amount, 2)
                message = "Money deposited successfully."
            else:
                account["balance"] = round(float(account.get("balance", 0)) - amount, 2)
                message = "Money withdrawn successfully."
            save_accounts(accounts)
            st.success(message)
            st.metric("Updated balance", money(account["balance"]))

elif page == "View account":
    st.header("View account details")
    with st.form("view_account_form"):
        account_number = st.text_input("Account number")
        pin = st.text_input("4-digit PIN", type="password", max_chars=4)
        submitted = st.form_submit_button("Show details", type="primary")

    if submitted:
        account = find_account(accounts, account_number.strip(), pin)
        if not account:
            st.error("Account number or PIN is incorrect.")
        else:
            st.subheader("Account information")
            st.write(f"**Name:** {account.get('name', '')}")
            st.write(f"**Age:** {account.get('age', '')}")
            st.write(f"**Email:** {account.get('email', '')}")
            st.write(f"**Account number:** `{account.get('account_number', '')}`")
            st.metric("Available balance", money(float(account.get("balance", 0))))
            if account.get("created_at"):
                st.caption(f"Created: {account['created_at']}")

elif page == "Update details":
    st.header("Update account details")
    with st.form("update_account_form"):
        account_number = st.text_input("Account number")
        pin = st.text_input("Current 4-digit PIN", type="password", max_chars=4)
        new_name = st.text_input("New name (leave blank to keep current)")
        new_email = st.text_input("New email (leave blank to keep current)")
        new_pin = st.text_input("New 4-digit PIN (leave blank to keep current)", type="password", max_chars=4)
        submitted = st.form_submit_button("Update details", type="primary")

    if submitted:
        account = find_account(accounts, account_number.strip(), pin)
        if not account:
            st.error("Account number or PIN is incorrect.")
        elif new_email.strip() and (
            "@" not in new_email or "." not in new_email.split("@")[-1]
        ):
            st.error("Please enter a valid email address.")
        elif new_email.strip() and any(
            a is not account and a.get("email", "").lower() == new_email.strip().lower()
            for a in accounts
        ):
            st.error("Another account already uses that email address.")
        elif new_pin and not validate_pin(new_pin):
            st.error("New PIN must contain exactly 4 digits.")
        elif not new_name.strip() and not new_email.strip() and not new_pin:
            st.info("No changes entered.")
        else:
            if new_name.strip():
                account["name"] = new_name.strip()
            if new_email.strip():
                account["email"] = new_email.strip()
            if new_pin:
                account["pin_hash"] = hash_pin(new_pin)
                account.pop("pin", None)
            save_accounts(accounts)
            st.success("Account details updated successfully.")

elif page == "Delete account":
    st.header("Delete account")
    st.error("Deleting an account permanently removes its record from this local demo.")
    with st.form("delete_account_form"):
        account_number = st.text_input("Account number")
        pin = st.text_input("4-digit PIN", type="password", max_chars=4)
        confirm = st.checkbox("I understand this action cannot be undone.")
        submitted = st.form_submit_button("Delete account", type="primary")

    if submitted:
        account = find_account(accounts, account_number.strip(), pin)
        if not account:
            st.error("Account number or PIN is incorrect.")
        elif not confirm:
            st.error("Please confirm that you want to delete the account.")
        else:
            accounts.remove(account)
            save_accounts(accounts)
            st.success("Account deleted successfully.")
