import datetime
import itertools

import pandas as pd

__all__ = ['construct_network']


def construct_network(commit_table, field='file', output=None, skip_zero=False):
    """
    Construct a developer collaboration network from commit data.
    :param commit_table: pandas DataFrame of commits and their modified files, as returned by functions in mison.mine
    :param field: "file" or "service": whether the weight connecting two developers should be the amount of co-modified
        files or services, respectively
    :param output: (optional) str, filename to save the mined commits csv table; if "default", will use the default
        name with current timestamp
    :param skip_zero: if True, remove weights equal to 0
    :return: pandas DataFrame with weights for each pair of developers
    """

    assert field in ('file', 'service')

    devs = {}
    for row in commit_table.itertuples(index=False):
        dev = devs.setdefault(row.author_email, set())
        f = row.filename if field == 'file' else row.microservice
        if pd.notna(f):
            dev.add(f)

    ordered_pairs = itertools.product(devs.keys(), repeat=2)
    unordered_pairs = {(a,b) for (a,b) in ordered_pairs if a < b}

    filecounts = [(dev_a, dev_b, len(devs[dev_a] & devs[dev_b])) for dev_a, dev_b in unordered_pairs]
    filecounts = pd.DataFrame(filecounts, columns=['developer_a', 'developer_b', 'weight'])
    filecounts = filecounts[filecounts.weight != 0] if skip_zero else filecounts

    if output is not None:
        if output == 'default':
            output = f"mison_developer_network_{field}_{datetime.datetime.now().isoformat()}.csv"
        filecounts.to_csv(output, index=False)

    return filecounts
