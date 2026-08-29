## Using Gitignore Files in GitHub 

create two files:
1) .env.example
2) .env

both of these files will contain the following text:
```
API_KEY=your_api_key_here
DB_PASSWORD=your_db_password_here
```
The `.env` file will be used to store sensitive information such as API keys and database passwords. This file should not be committed to the repository to prevent exposing sensitive data.

To ensure that the `.env` file is not tracked by Git, we will create a `.gitignore` file in the root of the repository (if it doesn't already exist) and add the following line to it:

```
*/.env
Labs/CodeQL-Demo-App/.env
```