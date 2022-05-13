from challenges.c094_partitioning import partition, partition_v2


def test_partition():
    assert partition(list("ABAABBBAAABBBA")) == "AAAAAAABBBBBBB"
    assert partition_v2(list("ABACCBBCAACCBBA")) == "AAAAABBBBBCCCCC"
