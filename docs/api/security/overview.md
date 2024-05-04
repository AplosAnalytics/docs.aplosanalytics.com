# Overview

We use Amazon Cognito as our Identity Provider (`IdP`).  To secure our APIs, we use JSON Web Tokens (`JWTs`)

JWTs are a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed. JWTs can be signed using a secret (with the HMAC algorithm) or a public/private key pair using RSA or ECDSA.

## Structure of a JWT


A JWT is composed of three parts:

1. **Header**: The header typically consists of two parts: the token type, JWT, and the signing algorithm used, such as HMAC SHA256 or RSA.

2. **Payload**: The payload contains the claims. Claims are statements about an entity (typically, the user) and additional metadata. There are three types of claims: registered, public, and private. Registered claims are a set of predefined claims that are not mandatory but recommended, like `iss` (issuer), `exp` (expiration time), and `sub` (subject).

3. **Signature**: To create the signature part, you must take the encoded header, the encoded payload, a secret, and the algorithm specified in the header and sign it.

## How JWTs Work

- **Encoding**: When a JWT is created, the header, payload, and signature are encoded separately using Base64URL and concatenated with periods as separators.

- **Transmission**: JWTs are typically used in the authorization header of an HTTP request. The server decodes the JWT to retrieve the header and payload, and it can verify the integrity of the message by using the signature.

- **Security**: While the information in the JWT can be decoded and read, the signature verifies the token's integrity. If the token is modified, the signature validation will fail.


## Usage Scenarios

- **Authentication**: After the user logs in using their credentials, a JWT can be issued so the user can use this token for future requests. This allows the user to avoid logging in again until the token expires.

- **Information Exchange**: JWTs can securely transfer information between parties. Since they can be signed—for example, using public/private key pairs—you can be sure the senders are who they say they are and the contents haven't been tampered with.

## Advantages and Considerations

- **Industry Standard**: JWTs have become the industry standard for securing APIs.

- **Compact**: Because of their smaller size, JWTs can be sent through URLs, POST parameters, or inside HTTP headers.

- **Self-contained**: The payload contains all the required information about the user, avoiding the need to query the database more than once.

- **Security Risks**: Security relies on the token being kept confidential. If intercepted, it could allow access to the user's data. Additionally, if a server is not properly validating the JWT, it could be prone to several attacks.


JWTs offer a robust way to handle authorization and information exchange on the web and even some IoT applications, making them a valuable tool in modern API authentication landscapes.


## Next Steps
Now that you have a general idea of "what" a JWT is, you'll gain a better understanding by seeing it in action.  Let's move on working with JWTs in our system by diving deeper into JWTs with Amazon Cognito.
