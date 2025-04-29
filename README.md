# CODSOFT_2
## Simple Python Password Generator

## Description

This is a basic Python script that generates a random password of a specified length. It utilizes a combination of uppercase letters, lowercase letters, digits, and punctuation symbols to create complex passwords suitable for various security needs.

## Features

* Generates random passwords.
* Allows the user to specify the desired password length.
* Uses a character set including:
    * Uppercase letters (A-Z)
    * Lowercase letters (a-z)
    * Digits (0-9)
    * Punctuation symbols (e.g., !, @, #, $, %, etc.)
* Simple command-line interface.
* Basic error handling for non-numeric input.

## Prerequisites

* Python 3.x

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    ```
    *(Replace `your-username` and `your-repository-name` with your actual GitHub username and repository name)*

2.  **Navigate to the directory:**
    ```bash
    cd your-repository-name
    ```

## Usage

1.  Run the script from your terminal:
    ```bash
    python password_generator.py
    ```
    *(Assuming you saved the code as `password_generator.py`. Rename the command if you used a different filename.)*

2.  The script will prompt you to enter the desired length for the password:
    ```
    Enter the desired password length:
    ```

3.  Enter an integer (e.g., `16`) and press Enter.

4.  The script will output the generated password:
    ```
    Your generated password is: [Your Generated Password Here]
    ```

    **Example:**
    ```bash
    $ python password_generator.py
    Enter the desired password length: 12
    Your generated password is: #aB5@kLp$3!z
    ```

5.  If you enter non-numeric input, it will display an error message:
    ```bash
    $ python password_generator.py
    Enter the desired password length: twelve
    Invalid input. Please enter a number.
    ```

## Code Explanation

* **Imports:** The script uses the `random` module for generating randomness and the `string` module for accessing predefined character sets (`ascii_letters`, `digits`, `punctuation`).
* **`generate_password(length)` function:**
    * Defines the character sets to be used.
    * Combines these sets into a single string `characters`.
    * Uses a loop (`for i in range(length)`) and `random.choice(characters)` to select random characters one by one.
    * `''.join(...)` concatenates these random characters into the final password string.
    * Returns the generated password.
* **Main execution block (`try...except`):**
    * Prompts the user for the desired password length using `input()`.
    * Attempts to convert the input to an integer using `int()`.
    * Calls the `generate_password()` function with the provided length.
    * Prints the result.
    * Includes a `ValueError` exception handler to catch cases where the user enters non-integer input, printing an informative error message.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any bugs, please feel free to open an issue or submit a pull request.

## License

Consider adding a LICENSE file to your repository. The [MIT License](https://opensource.org/licenses/MIT) is a popular choice for simple projects like this.
