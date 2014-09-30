Password protect static sites
=============================

Simple small python script to password protect static web content.

Needs Python 2 (can be easily fixed for Python 3) and Apache with `ExecCGI` and `mod_rewrite` enabled.

Usage
-----

Place `static-login.py` and `.htaccess` into any folder. Provide `index.html` and `login.html`. Login form should submit password via POST in a field called `password` (use any page for `action` in the form, probably `index.html`).

All content in this directory and all subdirectories will be available after entering a password. Unauthorized users will be redirected to the login page.

The default password is `changeme`. Change the password by editing `static-login.py`.

Note that `.css` and `.js` files can be accessed without providing a password (so that the login page be pretty).

Cookies are used to save the password in plaintext form for the duration of the session. If needed add path restrictions or expiration time for the cookie.

Disclaimer
----------

This was written in a few minutes for a simple static page that contains nothing of importance.

**Do not use for serious protection and security. Do not use in production enviroment.**
