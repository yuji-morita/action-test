import yaml
import git
import pymdownx.slugs

f = open("mkdocs.yml", "r+")
data = yaml.load(f, Loader=yaml.FullLoader)

repo = git.Repo('.')
tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)

if tags:
    versions = []
    for tag in tags:
        versions.insert(0, { tag.name: '/action-test/' + tag.name})

    data['nav'][0]['ガイド'].append({'バージョン': versions})

    f = open("mkdocs.yml", "w")
    yaml.dump(data, f, default_flow_style=False, encoding='utf8', allow_unicode=True)


