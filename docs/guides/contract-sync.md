# Contract Sync

`make sync-contracts` fetches the Aeries support articles listed in `contracts/sources.json`, stores raw HTML snapshots, and writes normalized JSON that the generator can turn into Python modules.

Use this command when the upstream docs change or when you need to refresh the committed contract artifacts.

