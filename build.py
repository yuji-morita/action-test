import yaml
import os
import git
import pymdownx.slugs

repo = git.Repo.clone_from("https://github.com/yuji-morita/action-test.git", "build")

tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)

versions = []
if tags:
    for tag in tags:
        versions.insert(0, { tag.name: "/action-test/" + tag.name})

f = open("build/mkdocs.yml", "r+")
data = yaml.load(f, Loader=yaml.FullLoader)


# master build
if tags:
    data["nav"][0]["ガイド"].append({"バージョン": versions})
    f = open("build/mkdocs.yml", "w")
    yaml.dump(data, f, default_flow_style=False, encoding="utf8", allow_unicode=True)

os.system("mkdocs build -f build/mkdocs.yml -d site")

# versions build
# if tags:
#     for tag in tags:
#         repo.git.checkout(".")
#         repo.git.checkout(tag)
#         data["nav"][0]["ガイド"].append({"バージョン": versions})
#         f = open("build/mkdocs.yml", "w")
#         yaml.dump(data, f, default_flow_style=False, encoding="utf8", allow_unicode=True)
#         os.system("mkdocs build -f build/mkdocs.yml -d site/" + tag.name)