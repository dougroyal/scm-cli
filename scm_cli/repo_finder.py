from operator import itemgetter


def find_repos(scm_clients, repo_pattern):
    """ Search all the scm_clients to find repos that match the repo_pattern.

    Args:
        scm_clients -- dict of modules
            The keys are host names, such as github, or bitbucket.

        repo_pattern -- string
            A string used to try and find matching repos


    Returns:
        list -- list of dicts, where each dict contains:

            [ {name: some-repo-name, host: github, scm_type: hg}

            {name: some-other-repo-name, host: bitbucket, scm_type: hg} ]
    """
    scm_hosts = {}

    for name in scm_clients:
        scm_hosts[name] = {}
        scm_hosts[name]['client'] = scm_clients[name]
        scm_hosts[name]['repos'] = scm_clients[name].get_repos()

    return _filter_repos(repo_pattern, scm_hosts)


def _filter_repos(pattern, scm_hosts):
    filtered_repos = []

    for host in scm_hosts:
        if scm_hosts[host]['repos'] == None:
            continue

        for repo in scm_hosts[host]['repos']:
            # TODO enable more advanced matches, such as * to match all
            if pattern.lower() in repo['name'].lower():
                filtered_repos.append({
                    'host': host,
                    'name': repo['name'],
                    'clone_url': repo['clone_url'],
                    'scm_type': repo['scm_type']
                })

    return sorted(filtered_repos, key=itemgetter('name'))
