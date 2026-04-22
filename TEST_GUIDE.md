# TEST GUIDE

0. Reset Data

Use button:

Reset Test Accounts

Recommended before testing.

1. Login Success

Username: admin
Password: Admin@123

Expected: Login success

2. Login Wrong Password

Username: admin
Password: wrong123

Expected: Wrong password

3. Login User Not Found

Username: ghost
Password: 123

Expected: Username does not exist

4. Register Success

Username: truongdev
Password: abc123
Confirm: abc123

Expected: Account created successfully

5. Register Duplicate Username

Username: admin
Password: abc123
Confirm: abc123

Expected: Username already exists

6. Change Password Success

Username: admin
Current Password: Admin@123
New Password: Admin@999
Confirm: Admin@999

Expected: Password updated successfully

7. Login With New Password

Username: admin
Password: Admin@999

Expected: Login success

8. Change To Previous Password

Username: admin
Current Password: Admin@999
New Password: Admin@123
Confirm: Admin@123

Expected: New password cannot equal previous password

9. Forgot Password Success

Username: admin
Previous Password: Admin@123
New Password: Hello@555

Expected: Password recovered successfully

10. Login After Recovery

Username: admin
Password: Hello@555

Expected: Login success

11. Forgot Password Reuse Old Password

Username: admin
Previous Password: Admin@123
New Password: Admin@123

Expected: New password cannot equal previous password

If Testing Becomes Messy

Use:

Reset Test Accounts
