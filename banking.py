
"""
Bank Account Simulation

Task:
- Manage simple bank accounts.
- Store accounts in dictionary { "account_number": {"name": str, "balance": float} }
- Deposit, withdraw, transfer between accounts.
- Use *args for batch deposits/withdrawals.
- Use **kwargs for flexible account creation (e.g., overdraft_limit).
"""

# Global accounts dictionary
accounts = {}

def create_account(account_number, name, **kwargs):
    """Create an account with optional features like overdraft_limit."""
    if account_number in accounts:
        return f"Account {account_number} already exists!"

    accounts[account_number] = {
        "name": name,
        "balance": 0.0
    }

    # Add optional features (like overdraft_limit)
    for key, value in kwargs.items():
        accounts[account_number][key] = value

    return f"Account created for {name} (#{account_number})."

def deposit(account_number, *amounts):
    """Deposit one or more amounts into an account."""
    if account_number not in accounts:
        return "Account not found!"

    total = sum(amounts)
    accounts[account_number]["balance"] += total
    return f"Deposited {total} into {accounts[account_number]['name']}'s account."

def withdraw(account_number, amount):
    """Withdraw money if balance (plus overdraft) is sufficient."""
    if account_number not in accounts:
        return "Account not found!"

    acc = accounts[account_number]
    limit = acc.get("overdraft_limit", 0)

    if acc["balance"] + limit >= amount:
        acc["balance"] -= amount
        return f"Withdrew {amount} from {acc['name']}'s account."
    else:
        return "Insufficient funds!"

def transfer(from_acc, to_acc, amount):
    """Transfer money between accounts if funds are sufficient."""
    if from_acc not in accounts or to_acc not in accounts:
        return "One or both accounts not found!"

    acc_from = accounts[from_acc]
    acc_to = accounts[to_acc]
    limit = acc_from.get("overdraft_limit", 0)

    if acc_from["balance"] + limit >= amount:
        acc_from["balance"] -= amount
        acc_to["balance"] += amount
        return f"Transferred {amount} from {acc_from['name']} to {acc_to['name']}."
    else:
        return "Insufficient funds!"

print(create_account("A001", "Alice", overdraft_limit=200))
print(create_account("A002", "Bob"))

print(deposit("A001", 500, 300))   # batch deposit
print(withdraw("A001", 600))
print(transfer("A001", "A002", 100))

print("\n--- Accounts Data ---")
print(accounts)

