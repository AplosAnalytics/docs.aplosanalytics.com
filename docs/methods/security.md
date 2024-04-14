# Security
Security is an essential part of Aplos NCA, and there are multiple layers to ensure the security of all data and information in the user account. 

## User Accounts
Each authorized user account will have a username (email address) and password. Those are held by Amazon Cognito. Aplos Analytics does not access to any passwords for users of Aplos NCA. Users can reset their passwords directly with Amazon Cognito. \
(need link and instructions on how to do that)

## Professional vs Team/Enterprise Accounts
Professional accounts are created in a multi-tenant environment, while Team and Enterprise accounts are single tenant environments. An analogy is that Professional accounts are like apartment units in a large apartment building. There is a single roof, but each apartment unit has it's own security lock. Aplos Analytics restricts Professional accounts to a single user. So only 1 person per apartment.

Team and Enterprise accounts are like single-family homes. Each home has it's own roof. Within the home, there are multiple rooms for different people to stay, but the owner of the home is allowed to visit all of the rooms inside the house. Thus Team and Enterprise accounts permit some users to be designated as administrators with the capability to see data and results from other users in their account.

## Administrators
Team and Enterprise accounts have the capability of assigning users as administrators. Administrators have the ability to manage user accounts (create, suspend, delete), and manage data for their account (delete analysis datasets and results). Administrators cannot modify any data or results, nor can they change any audit trail information. Deletion of analysese will be recorded in the audit trail with the name of the administrator that performed the deletion, and the date and time of deletion.

## Encryption
All data and files are encrypted in transit (i.e. transfer between user computer and Aplos NCA server) and while at rest (i.e. stored on server). The only time data is not encrypted is when it is in memory during the calculation of PK parameters. Aplos Analytics uses AWS KMS encryption methodology ([learn more here](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)).

## Storage
All uploaded files and results files are stored in AWS S3 buckets that are logically assigned to each user. These files are stored using the unique file identifiers and unique analysis identifiers created during the API processes for uploading files and analyzing data, respectively. Users only have access to the data through the API. Direct access to S3 buckets is not allowed.

## Regional Data Isolation
Enterprise Accounts have the ability to assign users to specific geographic regions for data storage and calculations. For example, a global company may want data from users in North America to stay in North America, and data from users in Europe to stay in the European Union. Aplos Analytics can work with your team to ensure that regional data isolation rules are respected for each user.
