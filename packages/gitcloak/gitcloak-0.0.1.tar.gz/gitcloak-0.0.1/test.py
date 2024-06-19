from gitcloak.classes.git import Git

repo = "https://github.com/privatecoffee/transfer.coffee"
git = Git(repo)
print(git.get_directory_structure("public/"))

file_path = "public/dist/js/webtorrent.LICENSE"
content = git.get_file_content(file_path)
print(f"Type of content: {type(content)}")
content = content.decode('utf-8')
print(f"\nContent of {file_path}:\n{content}")