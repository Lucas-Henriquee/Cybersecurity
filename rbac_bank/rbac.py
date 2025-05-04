# Defines which permissions are associated with each role
permissions = {
    "client": ["view_balance", "view_statement"],
    "manager": ["view_balance", "view_statement", "manage_accounts"],
    "admin": ["view_balance", "view_statement", "manage_accounts", "create_user"]
}


# Checks whether the specified role has permission to perform a given action.
def check_permission(role, action):
    allowed = action in permissions.get(role, [])
    if allowed:
        return allowed