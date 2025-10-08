# python-ecryption-introduction

This is a project I made to help me learn encryption.
I build this project in Python to help me level up my Python experience.

## What is Fernet?

Fernet is a symmetric encryption algorithm.
It uses a shared secret key to encrypt and decrypt data.

## Why did I use Fernet?

I chose Fernet because it is a symmetric encryption algorithm.
This means that the same key is used for both encryption and decryption.
This makes it easier to use and understand.

## How do I use Fernet?

To use Fernet, you first need to generate a key.
You can do this by calling the `Fernet.generate_key()` method.
This method will generate a random key and return it.

You can then use the key to create a `Fernet` instance.
The `Fernet` instance is used to encrypt and decrypt data.
You can create a `Fernet` instance by calling the `Fernet(key)` method.
The `key` parameter is the generated key.

Once you have a `Fernet` instance, you can use it to encrypt and decrypt data.
To encrypt data, you can call the `encrypt(data)` method on the `Fernet` instance.
To decrypt data, you can call the `decrypt(data)` method on the `Fernet` instance.

Sources:

- https://www.geeksforgeeks.org/python/how-to-encrypt-and-decrypt-strings-in-python/
- https://stackoverflow.com/questions/11063458/python-script-to-copy-text-to-clipboard
