import git
import os
print("Repo before")
repo = git.Repo('C:\ProgramData\Jenkins\.jenkins\workspace\git_python\task')
print("Repo after")
print('Remotes:')
for remote in repo.remotes:
    print(f'- {remote.name} {remote.url}')
print("remote after")
#comment
'''with repo.config_writer() as git_config:
    git_config.set_value('user', 'email', 'raysubham555@gmail.com')
    git_config.set_value('user', 'name', 'Ray-Shubham')
with repo.config_reader() as git_config:
    print(git_config.get_value('user', 'email'))
    print(git_config.get_value('user', 'name'))'''
if repo.is_dirty(untracked_files=True):
  print("Changes Detected")
  repo.git.add(all=True)
  repo.index.commit("Commit Done")
  print("pushing")
  print(repo.remotes.origin.push())
else:
  print("No Changes")
