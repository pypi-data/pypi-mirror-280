# GitCloak

GitCloak is a simple web frontend that lets you browse GitHub repositories and view their contents. It provides an easy-to-use interface to navigate directories, view files, and also renders `README.md` files. It is still a work in progress, but the basic functionality is there.

Instead of using the GitHub API or screen scraping, GitCloak interfaces directly with the GitHub repository using the git protocol. This should make it more resilient to changes on the GitHub side, and also allows future modifications or forks to support other git hosting services like Forgejo or GitLab instances.

## Features

- Browse directories and files in GitHub repositories.
- View the content of files directly in the browser.
- Responsive design with Bootstrap for a clean and professional look.

## Getting Started

### Prerequisites

- Python 3 (tested with 3.12)
- pip
- venv (optional but recommended)

### Production

1. Set up a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

2. Install GitCloak from PyPI:

   ```sh
   pip install gitcloak
   ```

3. Run the GitCloak server:

   ```sh
    gitcloak
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:8107/
   ```

### Development

1. Clone the repository:

   ```sh
   git clone https://git.private.coffee/PrivateCoffee/gitcloak
   cd gitcloak
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the Python package:

   ```sh
   pip install -Ue .

   ```

4. Run the development server:

   ```sh
   gitcloak
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:8107/
   ```

### Configuration

GitCloak currently supports the following environment variables:

- `PORT`: The port number to run the server on. Default is `8107`.
- `HOST`: The host to bind the server to. Default is `127.0.0.1`.

### Usage

- **Landing Page**: The landing page provides information about the app and instructions on how to use it.

  ```
  http://localhost:8107/
  ```

- **Browse Repository**: To browse a repository, use the following URL format:

  ```
  http://localhost:8107/<owner>/<repo>/
  ```

- **View Subdirectory**: To view a specific directory, use the following URL format:

  ```
  http://localhost:8107/<owner>/<repo>/tree/main/<path>
  ```

- **View File Content**: To view the raw content of a specific file, use the following URL format:
  ```
  http://localhost:8107/<owner>/<repo>/raw/main/<file_path>
  ```

## Contributing

We welcome contributions to improve GitCloak! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request to merge your changes into the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - A lightweight WSGI web application framework in Python.
- [Bootstrap](https://getbootstrap.com/) - A powerful front-end framework for faster and easier web development.
- [markdown2](https://github.com/trentm/python-markdown2) - A fast and complete implementation of Markdown in Python.
- [Phosphor Icons](https://phosphoricons.com/) - Beautifully designed icons for use in web projects.
