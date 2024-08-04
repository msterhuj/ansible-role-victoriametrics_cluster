def test_binary(host):
    bins = [
        "/usr/local/bin/vmstorage-prod",
        "/usr/local/bin/vminsert-prod",
        "/usr/local/bin/vmselect-prod",
    ]
    for bin in bins:
        b = host.file(bin)
        assert b.exists
        assert b.is_file
