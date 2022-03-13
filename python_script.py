import git
import os

class ProgressPrinter(git.RemoteProgress):
    def line_dropped(self, line):
        print("line dropped : " + str(line))
print("Repo before")
repo = git.Repo('')
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
  print(repo.remotes.origin.push(progress=ProgressPrinter()))
else:
  print("No Changes")
